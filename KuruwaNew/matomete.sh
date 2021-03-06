#!/bin/bash


#DIRS="Try01_bbr Try01_cubic Try02_bbr Try02_cubic Try03_bbr Try03_cubic"
#DIRS="Try01_bbr Try03_bbr Try03_cubic Try02_bbr Try02_cubic"
#DIRS="Try02_cubic Try02_bbr Try01_bbr Try03_cubic Try03_bbr"
#DIRS=Try01_cubic
#DIRS="Try02_cubic_lvstun Try01_cubic_lvstun"
#DIRS="Try02_cubic_iptablesdnat Try01_cubic_lvstun"
#DIRS="Try01_cubic_lvstun"
DIRS="Try02_cubic_lvsnat_on_node Try02_cubic_lvstun_on_node"
log=exec.log

for dir in $DIRS ; do 
	echo -n $dir" started on .... "
	date
	(cd $dir && ./setup.sh -e && ./setup.sh > $log && time ./bench.sh >> $log 2>&1 )
done

