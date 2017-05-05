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
	if ! wrk -c$con -t$thr -d$dur $url >> $file ; then
		sleep $wait
		if ! wrk -c$con -t$thr -d$dur $url >> $file ; then
			sleep $wait
			wrk -c$con -t$thr -d$dur $url >> $file
		fi
	fi
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

set_sg(){
url=http://172.16.61.2/
file=single.log
}

set_lv16(){
url=http://192.168.0.111:8888/
file=lvs_cpu16.log
}

set_px16(){
url=http://10.254.0.10/
file=proxy_cpu16.log
ip route replace 10.254.0.10/32 via 192.168.0.111
sleep 3
}

bench_set(){
kubectl scale rc/coffee-rc --replicas=1 -s 192.168.0.104:8080
#set_sg ; bench

for repl in 1 $(seq 2 2 40) ; do 

kubectl scale rc/coffee-rc --replicas=0 -s 192.168.0.104:8080

echo start measurement for $repl

kubectl scale rc/coffee-rc --replicas=$repl -s 192.168.0.104:8080
sleep $wait

ipvs_restart(){
for lv in k11 ; do 
	ssh -i ~/.ssh/id_rsa_k12 $lv 'sudo svc -t /etc/service/ipvs ; sudo svc -t /etc/service/flanneld/ '
done
sleep 10 ; ipvs_check
}

ipvs_check(){
for lv in k11 ; do 
	workers=$(ssh -i ~/.ssh/id_rsa_k12 $lv 'sudo ipvsadm -L -n|egrep :80 |wc -l')
	if [ $workers != $repl ]; then
		ipvs_restart
	fi
done
}

ipvs_restart

set_lv16 ; bench

set_px16 ; bench

echo end measurement for $repl
echo 

done
}

for i in {1..1}; do
bench_set
done

