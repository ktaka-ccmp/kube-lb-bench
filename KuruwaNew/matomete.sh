#!/bin/bash


DIRS="Try01_bbr Try01_cubic Try02_bbr Try02_cubic Try03_bbr Try03_cubic"
log=exec.log

for dir in $DIRS ; do 
	echo -n $dir" started on .... "
	date
	(cd $dir && ./setup.sh -e && ./setup.sh > $log && time ./bench.sh >> $log 2>&1 )
done

