#!/bin/bash

wait=30

con=800
thr=40
dur=60s

bench(){
	echo wrk -c$con -t$thr -d$dur $url 
	echo podnum=$repl >> $file
	echo -n "Start time: " >> $file
	date +%s >> $file
	echo wrk -c$con -t$thr -d$dur $url >> $file
	wrk -c$con -t$thr -d$dur $url >> $file
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

set_lv02(){
url=http://10.0.255.2:8888/
file=cpu08_lv02.log
}

set_lv04(){
url=http://10.0.255.4:8888/
file=cpu08_lv04.log
}

set_lv06(){
url=http://10.0.255.6:8888/
file=cpu08_lv06.log
}

set_lv08(){
url=http://10.0.255.8:8888/
file=cpu08_lv08.log
}

set_lv10(){
url=http://10.0.255.10:8888/
file=cpu08_lv10.log
}

set_lv12(){
url=http://10.0.255.12:8888/
file=cpu08_lv12.log
}

set_lv14(){
url=http://10.0.255.14:8888/
file=cpu08_lv14.log
}

set_lv16(){
url=http://10.0.255.16:8888/
file=cpu08_lv16.log
}

bench_set(){
for repl in 1 5 10 15 20 25 30 ; do 

kubectl scale rc/coffee-rc --replicas=0 -s 10.0.0.100:8080

echo start measurement for $repl

kubectl scale rc/coffee-rc --replicas=$repl -s 10.0.0.100:8080
sleep $wait

ipvs_restart(){
for lv in $(seq -w 2 2 016) ; do 
	ssh -i ~/.ssh/id_rsa_v200 kt-lvs$lv sudo svc -t /etc/service/ipvs 
done
sleep 10 ; ipvs_check
}

ipvs_check(){
for lv in $(seq -w 2 2 016) ; do 
        workers=$(ssh -i ~/.ssh/id_rsa_v200 kt-lvs$lv 'sudo ipvsadm -L -n|egrep :80 |wc -l')
        if [ $workers != $repl ]; then
                ipvs_restart
        fi
done
}

ipvs_restart
#sleep $wait


set_lv02 ; bench
set_lv04 ; bench
set_lv06 ; bench
set_lv08 ; bench
set_lv10 ; bench
set_lv12 ; bench
set_lv14 ; bench
set_lv16 ; bench

echo end measurement for $repl
echo 

done
}

for i in {1..1}; do
bench_set
done

