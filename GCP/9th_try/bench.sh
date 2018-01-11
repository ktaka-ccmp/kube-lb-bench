#!/bin/bash

wait=3

con=800
thr=40
dur=30s

sudo sh -c "echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries"

kbctl="kubectl -s 10.0.0.100:8080 "
eval $($kbctl get po -o wide  |grep ipvs|awk '{print "ipvs_addr="$6"; LVS="$7}')

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
	sudo ip route flush cache
	sleep $wait
	while ! curl $url ; do
		sudo ip route flush cache
		sleep $wait
		echo Retrying ....
	done
}

set_ipvs(){
url=http://104.196.229.104:18888/
file=ipvs_cpu16$num.log
}

set_px16(){
url=http://35.185.254.238:30920/
file=proxy_cpu16$num.log
}

bench_set(){

for repl in 1 $(seq 2 2 20) 25 30 35 40 45 50; do 

$kbctl scale deploy/tea-rc --replicas=0

echo start measurement for $repl

$kbctl scale deploy/tea-rc --replicas=$repl

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
	sleep $wait
	workers=$($kbctl exec -it $cid -- ipvsadm -L -n |egrep :80|wc -l)
	if [ $workers != $repl ]; then
		ipvs_check
	fi
done
}

pod_check
ipvs_check

for try in {0..4} ; do
num=_$try
set_ipvs ; bench
set_px16 ; bench
done

echo end measurement for $repl
echo 
done
}

bench_set_set(){
	echo "Measurement for RSS=$RSS;RPS=$RPS;RFS=$RFS "
	echo "Start time: $(date)"
	start=$(date +%s)

	echo "RSS=$RSS;RPS=$RPS;RFS=$RFS" | \
	ssh $LVS 'sudo sh -c "cat - > /etc/service/irq_set/env"'

	sleep 6

	dir=rss_rps_rfs_${RSS}_${RPS}_${RFS}
	mkdir -p $dir && \
	ssh $LVS ./irq_chk.sh > $dir/irq_chk.status && \
	(cd $dir ; bench_set)

	echo -n "Elapsed time: "
	date -d@$(($(date +%s) - $start))  -u +%H:%M:%S
	echo
}

RSS=0;RPS=1;RFS=0 ; bench_set_set
#RSS=1;RPS=0;RFS=0 ; bench_set_set

