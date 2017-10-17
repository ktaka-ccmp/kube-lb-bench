#/bin/bash

anal(){
	echo \"Percentile\",\"Latency [msec]\"
	sed -n -e '/podnum='$podnum'$/,/End time/p' $file |egrep percentile |sed -e 's/^percentile,//g' 
}

anal2(){
	echo -n $rate","
	sed -n -e '/podnum='$podnum'$/,/End time/p' $file \
	|egrep "^min"|sed -e 's/min=//g' -e 's/median=//g' -e 's/max=//g' -e 's/\[msec\]//g'	
}

anal_outer(){
for rate in {10000..200000..10000}  ; do 
	file=${prefix}cpu16_${rate}.log
	for podnum in $(egrep podnum= $file|sed -e 's/^podnum=//g') ;  do
		anal > latency_${prefix}${podnum}_${rate}.csv
	done

done 

for podnum in 5 10 20 30 40 ;  do
	echo \"Rate[rps]\",\"min [msec]\",\"median [msec]\",\"max [msec]\" > latency_${prefix}${podnum}.csv
	for rate in {10000..200000..10000}  ; do 
		file=${prefix}cpu16_${rate}.log
		anal2 >> latency_${prefix}${podnum}.csv
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

