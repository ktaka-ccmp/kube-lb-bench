#!/bin/bash

wait=3

con=800
thr=40
dur=30s
lua_script=${PWD}/result.lua

echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries

kbctl="kubectl -s 192.168.0.104:8080 "

bench(){
	chk_url

	echo wrk -c$con -t$thr -d$dur -s$lua_script $url 
	echo podnum=$repl >> $file
	echo -n "Start time: " >> $file
	date +%s >> $file
	echo wrk -c$con -t$thr -d$dur -s$lua_script $url >> $file
	while ! wrk -c$con -t$thr -d$dur -s$lua_script $url >> $file ; do
		chk_url
	done
	echo -n "End time: " >> $file
	date +%s >> $file
	echo >> $file
}

chk_url(){
	ip route flush cache
	sleep $wait
	while ! curl $url ; do
		ip route flush cache
		sleep $wait
		echo Retrying ....
	done
}

set_sg(){
url=http://172.16.61.2/
file=single.log
}

set_ipvs(){
ipvs_addr=$($kbctl get po -o wide |grep ipvs|awk '{print $6}')
url=http://${ipvs_addr}:8888/
file=ipvs_cpu16$num.log
ip route replace ${ipvs_addr}/32 via 192.168.0.111
}

set_lv16(){
url=http://192.168.0.111:8888/
file=lvs_cpu16$num.log
}

set_px16(){
url=http://10.254.0.10:81/
file=proxy_cpu16$num.log
ip route replace 10.254.0.10/32 via 192.168.0.111
}

set_nginx(){
ipvs_addr=$($kbctl get po -o wide |grep nginx-ingress|awk '{print $6}')
url=http://${ipvs_addr}/
file=nginx_cpu16$num.log
ip route replace ${ipvs_addr}/32 via 192.168.0.111
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

lvs_restart(){
for lv in k11 ; do 
	ssh -i ~/.ssh/id_rsa_k12 $lv 'sudo svc -t /etc/service/ipvs ; sudo svc -t /etc/service/flanneld/ '
done
}

lvs_check(){
for lv in k11 ; do 
        workers=$(ssh -i ~/.ssh/id_rsa_k12 $lv 'sudo ipvsadm -L -n|egrep :80 |wc -l')
        if [ $workers != $repl ]; then
		ssh -i ~/.ssh/id_rsa_k12 $lv 'sudo svc -t /etc/service/ipvs ; sudo svc -t /etc/service/flanneld/ '
		sleep 15
                lvs_check
        fi
done
}

pod_check

for try in {0..1} ; do
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

