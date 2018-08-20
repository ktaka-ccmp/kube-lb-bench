#!/bin/bash

wait=10

con=800
thr=40
dur=30s

echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries

kbctl="kubectl -s 192.168.0.104:8080 "

bench(){

	chk_url

	echo wrk -c$con -t$thr -d$dur $url 
	echo podnum=$repl >> $file
	echo -n "Start time: " >> $file
	date +%s >> $file
	echo wrk -c$con -t$thr -d$dur $url >> $file
	while ! wrk -c$con -t$thr -d$dur $url >> $file ; do
		ip route flush cache
		sleep $wait
		echo Retrying ....
	done
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

chk_url(){
	while ! curl $url ; do
		ip route flush cache
		sleep 1
		echo Retrying ....
	done
}

set_sg(){
url=http://172.16.61.2/
file=single.log
}

set_lv16(){
ipvs_addr=$($kbctl get po -o wide |grep ipvs|awk '{print $6}')
url=http://${ipvs_addr}:8888/
file=lvs_cpu16$num.log
ip route replace ${ipvs_addr}/32 via 192.168.0.111
ip route flush cache
}

set_px16(){
url=http://10.254.0.10:81/
file=proxy_cpu16$num.log
ip route replace 10.254.0.10/32 via 192.168.0.111
ip route flush cache
}

bench_set(){
#kubectl scale rc/coffee-rc --replicas=1 -s 192.168.0.104:8080
#set_sg ; bench

cids=$($kbctl get po -o wide |grep ipvs| cut -f 1 -d ' ')

#for repl in 1 $(seq 2 2 20) 25 30 35 40 ; do 
for repl in 1 5 10 15 20 25 30 35 40 ; do 

$kbctl scale deploy/tea-rc --replicas=0

echo start measurement for $repl

$kbctl scale deploy/tea-rc --replicas=$repl

ipvs_restart(){
sleep $wait ; ipvs_check
}

ipvs_check(){
for cid in $cids ; do 
	workers=$($kbctl exec -it $cid -- ipvsadm -L -n |egrep :80|wc -l)
	if [ $workers != $repl ]; then
		ipvs_restart
	fi
done
}

sleep $wait
ipvs_check

for try in {0..0} ; do
num=_$try
set_px16 ; bench
done

for try in {0..0} ; do
num=_$try
set_lv16 ; bench
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
	ssh k11  "cat - > /etc/service/irq_set/env"

	sleep 6

	dir=rss_rps_rfs_${RSS}_${RPS}_${RFS}
	mkdir -p $dir && \
	ssh k11 ./irq_chk.sh > $dir/irq_chk.status && \
	(cd $dir ; bench_set)

	echo -n "Elapsed time: "
	date -d@$(($(date +%s) - $start))  -u +%H:%M:%S
	echo
}

RSS=0;RPS=1;RFS=0 ; bench_set_set
RSS=1;RPS=0;RFS=0 ; bench_set_set
RSS=0;RPS=0;RFS=0 ; bench_set_set

