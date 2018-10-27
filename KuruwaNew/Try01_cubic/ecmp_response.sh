#!/bin/bash

kbctl="kubectl -s 192.168.0.102:8080 "
wkdir=response_$(date +"%H%M")

set_ipvs(){
prev=1
echo $kbctl scale deploy/ipvs-controller --replicas=1
$kbctl scale deploy/ipvs-controller --replicas=1

while true ; do 
	for i in $(shuf -i 1-4); do
		[[ $i == $prev ]] && continue 
		prev=$i
		sleep 60
		echo $kbctl scale deploy/ipvs-controller --replicas=$i 
		$kbctl scale deploy/ipvs-controller --replicas=$i 
	done
done
}

get_rps(){
while true ; do
	start=$(date +%s)
	rps=$(wrk -c2000 -t40 -d4s http://10.1.1.1:8888/|egrep Request|awk '{print $2}')
	stop=$(date +%s)
	echo $(printf $(( ( $start + $stop)/2 ))),$rps
	sleep 0.0
done
}

get_ipvs(){
while true ; do
	start=$(date +%s)
	pod=$($kbctl get pod -o=wide |egrep ipvs-controller|egrep  Running|wc -l)
	route=$(ip route show 10.1.1.0/24|egrep via |wc -l)
	stop=$(date +%s)
	echo $(printf $(( ( $start + $stop)/2 ))),$pod,$route
	sleep 0.6
done
}

trap 'kill $(jobs -p)' EXIT

mkdir -p $wkdir
set_ipvs &
get_ipvs > $wkdir/lbnum.csv &
get_rps > $wkdir/rps.csv &

wait 
echo done

