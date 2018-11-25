#!/bin/bash

#mode=bbr
mode=cubic
proc_fs=/proc/sys/net/ipv4/tcp_congestion_control
kbctl="kubectl -s 192.168.0.102:8080 "

K8S="03 04 05 06 07 08 09 10 12 13 14"
WEB="03 04 05 06 13 14"
LVS="07 08 09"
ALL="$K8S 10 11"

set_param(){
	for hst in $ALL ; do 
		ssh k$hst "modprobe tcp_$mode
		echo $mode  > $proc_fs "
	done

	for hst in $K8S  ; do 
		$kbctl label node k$hst web- --overwrite 
		$kbctl label node k$hst lvs- --overwrite 
	done 

	for hst in $WEB ; do 
		$kbctl label node k$hst web=yes --overwrite 
	done 

	for hst in $LVS ; do 
		$kbctl label node k$hst lvs=yes --overwrite 
	done 
}

show_param(){
	for hst in $ALL ; do 
		echo -n k$hst": "
		cat $proc_fs
	done

	$kbctl get node --show-labels
}


if [ "$1" == "-e" ] ; then
	set_param
	echo
	show_param
else
	show_param 
	echo
	echo "Execute \"$0 -e\" , to set parameters"
fi

