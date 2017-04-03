#!/bin/bash

wait=30

con=800
thr=40
dur=60s

bench(){
	echo wrk -c$con -t$thr -d$dur $url 
	echo podnum=$repl >> $file
	echo -n "Start time: " >> $file
	echo wrk -c$con -t$thr -d$dur $url >> $file
	date +%s >> $file
	wrk -c$con -t$thr -d$dur $url >> $file
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

set_lv02(){
url=http://10.0.255.2:8888/coffee
file=lvs_cpu02.log
}

set_lv04(){
url=http://10.0.255.4:8888/coffee
file=lvs_cpu04.log
}

set_lv06(){
url=http://10.0.255.6:8888/coffee
file=lvs_cpu06.log
}

set_lv08(){
url=http://10.0.255.8:8888/coffee
file=lvs_cpu08.log
}

set_lv10(){
url=http://10.0.255.10:8888/coffee
file=lvs_cpu10.log
}

set_lv12(){
url=http://10.0.255.12:8888/coffee
file=lvs_cpu12.log
}

set_lv14(){
url=http://10.0.255.14:8888/coffee
file=lvs_cpu14.log
}

set_lv16(){
url=http://10.0.255.16:8888/coffee
file=lvs_cpu16.log
}

bench_set(){
for repl in 1 $(seq 2 2 20) 25 30 35 40 ; do 

kubectl scale rc/coffee-rc --replicas=0 -s 10.0.0.100:8080

echo start measurement for $repl

kubectl scale rc/coffee-rc --replicas=$repl -s 10.0.0.100:8080
sleep $wait

for lv in $(seq -w 2 2 016) ; do 
	ssh -i ~/.ssh/id_rsa_v200 kt-lvs$lv sudo svc -t /etc/service/ipvs 
done
sleep $wait

set_lv02 ; bench
set_lv04 ; bench
#set_lv06 ; bench
set_lv08 ; bench
#set_lv10 ; bench
set_lv12 ; bench
#set_lv14 ; bench
set_lv16 ; bench

echo end measurement for $repl
echo 

done
}

for i in {1..10}; do
bench_set
done

