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

set_lv16(){
url=http://10.0.255.16:8888/
file=cpu08_lv16.log
}

bench_set(){
for repl in 1 $(seq 2 2 20) 25 30 ; do 

kubectl scale rc/coffee-rc --replicas=0 -s 10.0.0.100:8080

echo start measurement for $repl

kubectl scale rc/coffee-rc --replicas=$repl -s 10.0.0.100:8080
sleep $wait

ipvs_restart(){
for lv in 016 ; do 
	ssh -i ~/.ssh/id_rsa_v200 kt-lvs$lv sudo svc -t /etc/service/ipvs 
done
sleep 10 ; ipvs_check
}

ipvs_check(){
for lv in 016 ; do 
        workers=$(ssh -i ~/.ssh/id_rsa_v200 kt-lvs$lv 'sudo ipvsadm -L -n|egrep :80 |wc -l')
        if [ $workers != $repl ]; then
                ipvs_restart
        fi
done
}

ipvs_restart
sleep $wait

for try in 1 2 3 4 5 6 7 8 ; do 
set_lv16 
file=cpu08_lv16_${try}.log
bench
done

echo end measurement for $repl
echo 

done
}

for i in {1..1}; do
bench_set
done

