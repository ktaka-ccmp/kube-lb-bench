#!/bin/bash 

wait=3

con=800
thr=40
dur=30s

repl=40

sudo sh -c "echo 3 >  /proc/sys/net/ipv4/tcp_syn_retries"

PROVIDER=$(cat /sys/class/dmi/id/bios_version| sed \
	-e 's/\(.*\)/\U\1/' -e 's/.*AMAZON.*/AWS/g' -e 's/.*AWS.*/AWS/g' -e 's/.*EC2.*/AWS/g' \
	-e 's/\(.*\)/\U\1/' -e 's/.*GOOGLE.*/GCP/g' -e 's/.*GCP.*/GCP/g' \
	)

case "$PROVIDER" in
	"GCP" )
	kbctl="kubectl -s 10.0.0.100:8080 " ;;
	"AWS" )
	kbctl="kubectl -s 10.0.0.10:8080 " ;;
esac

########## functions

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

pod_check(){
        sleep $wait
        running=$($kbctl get po |egrep tea |egrep Running | wc -l)
        not_running=$($kbctl get po |egrep tea |egrep -v Running | wc -l)
        if [ $running != $repl ] || [ $not_running != 0 ] ; then
                pod_check
        fi
}

######### Measurement

bench_set(){
routes=$($kbctl get pod -o wide |egrep ipvs-controller |awk '{print $7"+"$6}'|sort)

for route in $routes ; do 

	$kbctl scale deploy/tea-rc --replicas=$repl
	pod_check

	lvsip=${route#*+}
	node=${route%+*}
	nodeip=$(getent hosts $node |awk '{ print $1 }')
	url=http://$lvsip:8888/

	file=ipvs_on_$node.log

	if [ "$PROVIDER" == "GCP" ]; then
	if [ "$(gcloud compute routes describe $node  |yq -r .nextHopIp)" != "$nodeip" ] ; then
		gcloud compute routes delete $node -q 
		gcloud compute routes create $node --network ktaka-net \
		--destination-range=$lvsip --next-hop-address $nodeip --priority 100 
	fi
	fi

	if [ "$PROVIDER" == "AWS" ]; then
		echo sudo ip route replace ${lvsip}/32 via $nodeip
		sudo ip route replace ${lvsip}/32 via $nodeip
	fi

	bench
done 
}

RSS=0;RPS=1;RFS=0

for i in {1..100} ; do
	echo -n "n=" $i "; "
	date
	dir=rss_rps_rfs_${RSS}_${RPS}_${RFS}
	mkdir -p $dir && \
	(cd $dir ; bench_set)
done


