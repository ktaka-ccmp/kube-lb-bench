#!/bin/bash

wait=20

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
url=http://172.16.58.2/
file=single.log
}

set_lv02(){
url=http://10.0.1.2:8888/
file=lvs_cpu02.log
}

set_lv04(){
url=http://10.0.1.4:8888/
file=lvs_cpu04.log
}

set_lv08(){
url=http://10.0.1.8:8888/
file=lvs_cpu08.log
}

set_lv12(){
url=http://10.0.1.12:8888/
file=lvs_cpu12.log
}

set_lv16(){
url=http://10.0.1.16:8888/
file=lvs_cpu16.log
}

set_px02(){
url=http://10.254.0.10/
file=proxy_cpu02.log
ip route replace 10.254.0.10/32 via 10.0.1.2
sleep 3
}

set_px04(){
url=http://10.254.0.10/
file=proxy_cpu04.log
ip route replace 10.254.0.10/32 via 10.0.1.4
sleep 3
}

set_px08(){
url=http://10.254.0.10/
file=proxy_cpu08.log
ip route replace 10.254.0.10/32 via 10.0.1.8
sleep 3
}

set_px12(){
url=http://10.254.0.10/
file=proxy_cpu12.log
ip route replace 10.254.0.10/32 via 10.0.1.12
sleep 3
}

set_px16(){
url=http://10.254.0.10/
file=proxy_cpu16.log
ip route replace 10.254.0.10/32 via 10.0.1.16
sleep 3
}

bench_set(){
kubectl scale rc/coffee-rc --replicas=1 -s 10.0.1.1:8080
set_sg ; bench

for repl in 1 $(seq 2 2 30) 35 40 ; do 

kubectl scale rc/coffee-rc --replicas=0 -s 10.0.1.1:8080

echo start measurement for $repl

kubectl scale rc/coffee-rc --replicas=$repl -s 10.0.1.1:8080
sleep $wait

ipvs_restart(){
for lv in 2 4 8 12 16 ; do 
	ssh -i ~/.ssh/id_rsa_v200 v$(printf %03d $lv).k01 sudo svc -t /etc/service/ipvs 
done
sleep 10 ; ipvs_check
}

ipvs_check(){
for lv in 2 4 8 12 16 ; do 
	workers=$(ssh -i ~/.ssh/id_rsa_v200 v$(printf %03d $lv).k01 'sudo ipvsadm -L -n|egrep :80 |wc -l')
	if [ $workers != $repl ]; then
		ipvs_restart
	fi
done
}

ipvs_restart
sleep $wait

set_lv02 ; bench
set_lv04 ; bench
set_lv08 ; bench
set_lv12 ; bench
set_lv16 ; bench

set_px02 ; bench
set_px04 ; bench
set_px08 ; bench
set_px12 ; bench
set_px16 ; bench

echo end measurement for $repl
echo 

done
}

for i in {1..1}; do
bench_set
done

