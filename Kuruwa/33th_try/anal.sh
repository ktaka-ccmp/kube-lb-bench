#/bin/bash

anal(){
	echo \"Percentile\",\"Latency [msec]\"
	sed -n -e '/podnum='$podnum'$/,/End time/p' $file |egrep percentile |sed -e 's/^percentile,//g' 
}

anal_outer(){
for i in {0..1} ; do 
	file=${prefix}cpu16_${i}.log
	for podnum in $(egrep podnum= $file|sed -e 's/^podnum=//g') ;  do
		anal > latency_${prefix}${podnum}_${i}.csv
	done
done 
}

for dir in rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs_ ; anal_outer 
prefix=proxy_ ; anal_outer 
)
done

