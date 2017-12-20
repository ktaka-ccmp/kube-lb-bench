#!/bin/bash

wait=3

con=800
thr=40
dur=30s

sudo sh -c "echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries"

kbctl="kubectl -s 10.0.0.100:8080 "

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

ALL_NODE="kt-v101 kt-v102 kt-v103 kt-v104 kt-v105 kt-v106 kt-v107 kt-v108 kt-v109 kt-v110 kt-v111 kt-v112 kt-v113 kt-v114 kt-v115 kt-v116 kt-v117 kt-v118 kt-v119 kt-v120"

unlabel(){
	for nd in $NODES ; do echo $nd; $kbctl label node $nd web- --overwrite; done
}

label(){
	for nd in $NODES ; do echo $nd; $kbctl label node $nd web=yes --overwrite; done
}

set_gcplb(){
url=http://35.197.33.30/
file=gcplb$num.log
}

bench_set(){

for repl in 1 $(seq 2 2 20) 25 30 35 40 ; do 

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

pod_check

for try in {0..0} ; do
num=_$try
set_gcplb ; bench
done

echo end measurement for $repl
echo 
done
}

bench_set_set(){
	echo "Start time: $(date)"
	start=$(date +%s)

	dir=node_num
	mkdir -p $dir && \
	(cd $dir ; bench_set)

	echo -n "Elapsed time: "
	date -d@$(($(date +%s) - $start))  -u +%H:%M:%S
	echo
}

bench_set_set

