#!/bin/bash

wait=1

con=2000
thr=100
dur=30s
#dur=15s
#dur=3s

ulimit -n 65536

echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries

kbctl="kubectl -s 192.168.0.102:8080 "

bench(){
	dstat_begin

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

	dstat_end
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

set_xlb(){
url=http://10.1.1.2/
file=xlb_$num.log
}

set_iptd(){
url=http://10.254.0.10:81/
file=iptd_$num.log
}

pod_check(){
echo -n "pod_check : "
	sleep $wait
	running=$($kbctl get po |egrep tea |egrep Running | wc -l)
	not_running=$($kbctl get po |egrep tea |egrep -v Running | wc -l)
	echo "$running , $not_running"
	if [ $running != $repl ] || [ $not_running != 0 ] ; then
		pod_check
	fi
}


dstat_begin(){
script=./cpuidle.sh
dur2=${dur%?}

lvs_hosts=$($kbctl get node --show-labels|grep lvs=yes|cut -f 1 -d " ")
for hst in $lvs_hosts ; do
cat <<EOF | ssh $hst "cat - > $script "
#!/bin/bash

rm -f dstat_$repl.csv
dstat -Tcn -N eth0,docker0,veth31e08a5 --output dstat_$repl.csv -i 1 $((dur2*2+5)) > /dev/null 2>&1
EOF

ssh $hst "chmod +x $script  &&  $script" &                                                
done
}

dstat_end(){
	wait
	scp $hst:~/dstat_$repl.csv ./$file.dstat_$repl.csv
}

bench_set(){

#for try in 0 8 9 ; do
for try in {0..9} ; do
for ipvs in {1..1}; do
for repl in 1 $(seq 2 2 20) $(seq 25 5 60) ; do

echo start measurement for $repl
$kbctl scale deploy/tea-rc --replicas=1
$kbctl scale deploy/tea-rc --replicas=$repl

sleep 3
$kbctl scale deploy/tea-rc --replicas=$repl

pod_check
sleep 3


num=${ipvs}_$try

#set_xlb ; bench
set_iptd ; bench 

echo end measurement for try= $try, ipvs= $ipvs , repl= $repl
echo 
done
done
done
}

bench_set_set(){
	echo "Measurement for RSS=$RSS;RPS=$RPS;RFS=$RFS;XPS=$XPS "
	echo "Start time: $(date)"
	start=$(date +%s)

	lvs_hosts=$($kbctl get node --show-labels|grep lvs=yes|cut -f 1 -d " ")
	for hst in $lvs_hosts ; do echo "RSS=$RSS;RPS=$RPS;RFS=$RFS;XPS=$XPS" | \
	ssh $hst  "cat - > /etc/service/irq_set/env" ; done

	sleep 6

	dir=cpuidle_rss_rps_rfs_xps_${RSS}_${RPS}_${RFS}_${XPS}
	mkdir -p $dir && \
	cat /dev/null > $dir/irq_chk.status && \
	for hst in $lvs_hosts ; do echo echo $hst >> $dir/irq_chk.status ; ssh $hst ./irq_chk.sh >> $dir/irq_chk.status ; done && \
	(cd $dir ; bench_set)

	echo -n "Elapsed time: "
	date -d@$(($(date +%s) - $start))  -u +%H:%M:%S
	echo
}

RSS=0;RPS=0;RFS=0;XPS=0 ; bench_set_set

