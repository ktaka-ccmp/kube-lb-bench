#!/bin/bash

wait=1

con=2000
thr=100
dur=30s

ulimit -n 65536

echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries

kbctl="kubectl -s 192.168.0.102:8080 "

bench(){
	chk_url

	echo wrk -c$con -t$thr -d$dur $url 
	echo podnum=$repl >> $file
	echo -n "Start time: " >> $file
	date +%s >> $file
	echo wrk -c$con -t$thr -d$dur $url >> $file
	while ! wrk -c$con -t$thr -d$dur $url >> $file ; do
		chk_url
	done
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

chk_url(){
	ip route flush cache
	sleep $wait
	while ! curl $url ; do
		ip route flush cache
		sleep $wait
		echo Retrying ....
	done
}

set_ipvs(){
#url=http://10.1.1.1:8888/
url=http://10.1.1.1:80/
file=ipvs$num.log
}

ipvsctr_check(){
	running=$($kbctl get po |egrep ipvs-controller |egrep Running | wc -l)
	not_running=$($kbctl get po |egrep ipvs-controller |egrep -v Running | wc -l)
	if [ $running != $ipvs ] || [ $not_running != 0 ] ; then
		sleep $wait
		ipvsctr_check
	fi
}

pod_check(){
	sleep $wait
	running=$($kbctl get po |egrep tea |egrep Running | wc -l)
	not_running=$($kbctl get po |egrep tea |egrep -v Running | wc -l)
	if [ $running != $repl ] || [ $not_running != 0 ] ; then
		pod_check
	fi
}

ipvs_check(){
cids=$($kbctl get po -o wide |grep ipvs|egrep Runn |cut -f 1 -d ' ')
for cid in $cids ; do 
	workers=$($kbctl exec -it $cid -c server -- ipvsadm -L -n -f 2 |egrep :80|wc -l)
	if [ $workers != $repl ]; then
		sleep $wait
		ipvs_check
	fi
done
}


bench_set(){

for try in {0..9} ; do
#for ipvs in {1..4}; do
for ipvs in {1..1}; do
for repl in 1 $(seq 2 2 40) $(seq 44 4 100) ; do 
#for repl in 120 140 160 180 200 ; do 

echo start measurement for $repl
$kbctl scale deploy/tea-rc --replicas=0
$kbctl scale deploy/tea-rc --replicas=$repl

$kbctl scale deploy/ipvs-controller --replicas=0
$kbctl scale deploy/ipvs-controller --replicas=$ipvs

sleep 3
$kbctl scale deploy/tea-rc --replicas=$repl
$kbctl scale deploy/ipvs-controller --replicas=$ipvs

ipvsctr_check
pod_check
ipvs_check

num=${ipvs}_$try
set_ipvs ; bench

echo end measurement for try= $try, ipvs= $ipvs , repl= $repl
echo 
done
done
done
}

bench_set_set(){
	echo "Measurement for RSS=$RSS;RPS=$RPS;RFS=$RFS;XPS=$XPS "
	echo "Start time: $(date)"
	start=$(date +%s)

	lvs_hosts=$($kbctl get node --show-labels|grep lvs=yes|cut -f 1 -d " ")
	for hst in $lvs_hosts ; do echo "RSS=$RSS;RPS=$RPS;RFS=$RFS;XPS=$XPS" | \
	ssh $hst  "cat - > /etc/service/irq_set/env" ; done

	sleep 6

	dir=rss_rps_rfs_xps_${RSS}_${RPS}_${RFS}_${XPS}
	mkdir -p $dir && \
	cat /dev/null > $dir/irq_chk.status && \
	for hst in $lvs_hosts ; do echo echo $hst >> $dir/irq_chk.status ; ssh $hst ./irq_chk.sh >> $dir/irq_chk.status ; done && \
	(cd $dir ; bench_set)

	echo -n "Elapsed time: "
	date -d@$(($(date +%s) - $start))  -u +%H:%M:%S
	echo
}

RSS=0;RPS=1;RFS=1;XPS=1 ; bench_set_set

