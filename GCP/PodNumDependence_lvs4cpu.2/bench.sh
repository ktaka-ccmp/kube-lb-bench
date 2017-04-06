#!/bin/bash

wait=20

con=800
thr=40
dur=60s

bench(){
	echo wrk -c$con -t$thr -d$dur $url 
	echo $repl >> $file
	echo wrk -c$con -t$thr -d$dur $url >> $file
	echo -n "Start time: " >> $file
	date +%s >> $file
	wrk -c$con -t$thr -d$dur $url >> $file
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

set_sg(){
url=http://172.16.20.3/coffee
file=single.log
}

set_px(){
url=http://10.254.0.10/coffee
file=proxy.log
}

set_ig(){
url=http://172.16.16.2/coffee
file=ingress.log
}

set_lv(){
url=http://10.0.255.12:8888/coffee
file=lvs.log
}

kubectl scale rc/coffee-rc --replicas=1 -s 10.0.0.100:8080
set_sg ; bench 

#for repl in {1..10} ; do 
for repl in 1 $(seq 2 2 40) ; do 

echo start measurement for $repl
kubectl scale rc/coffee-rc --replicas=$repl -s 10.0.0.100:8080
sleep $wait
ssh -i ~/.ssh/id_rsa_v200 kt-lvs012 sudo svc -t /etc/service/ipvs
#kubectl get pod -o wide -s 10.0.0.100:8080

set_px ; bench 
set_ig ; bench 
set_lv ; bench 
echo end measurement for $repl
echo 

done


