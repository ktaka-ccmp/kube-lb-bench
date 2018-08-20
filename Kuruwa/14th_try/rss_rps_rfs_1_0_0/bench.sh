#!/bin/bash

wait=10

con=800
thr=40
dur=60s

echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries

kbctl="kubectl -s 192.168.0.104:8080 "

bench(){
	echo wrk -c$con -t$thr -d$dur $url 
	echo podnum=$repl >> $file
	echo -n "Start time: " >> $file
	date +%s >> $file
	echo wrk -c$con -t$thr -d$dur $url >> $file
	while ! wrk -c$con -t$thr -d$dur $url >> $file ; do
		sleep $wait
		echo Retrying ....
	done
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
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
sleep 3
}

set_px16(){
url=http://10.254.0.10:81/
file=proxy_cpu16$num.log
ip route replace 10.254.0.10/32 via 192.168.0.111
ip route flush cache
sleep 3
}

bench_set(){
#kubectl scale rc/coffee-rc --replicas=1 -s 192.168.0.104:8080
#set_sg ; bench

cids=$($kbctl get po -o wide |grep ipvs| cut -f 1 -d ' ')

for repl in 1 $(seq 2 2 20) 25 30 35 40 ; do 

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

for i in {1..1}; do
bench_set
done

