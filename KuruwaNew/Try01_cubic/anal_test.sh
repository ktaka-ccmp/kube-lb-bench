#/bin/bash

anal(){

echo \"# of pods\",\"Req/sec\"
egrep "podnum|Requ" $1 \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -E -e 's/podnum=//g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal2(){

egrep "podnum|time:|Requ" $1 \
|awk '/^podnum|^Start|^Requ/ { printf("%s ", $0); next } 1' \
|sed -E -e 's/podnum=//g' -e 's/Start time: //g' -e 's/End time: //g' -e 's/Requests\/sec:[[:space:]]+//g' \
|awk '{$2+=1;$4-=1;print}'
}


anal_outer(){
for file in ${prefix}*.log ; do 
	echo "anal2 $file > ${file%.log}.csv "
#	anal $file > ${file%.log}.csv

	echo \"# of pods\",\"Req/sec\",\"ave. cpu idle\" > ${file%.log}.csv
 	anal2 $file |
	while read pod t1 rps t2 ; do

#		echo "$pod $rps $t1 $t2"
		echo -n "$pod,$rps,"
		awk "/$t1/,/$t2/" dstat_$pod.csv | awk -F, '{sum+=$4} END {print sum/NR}'
	done >> ${file%.log}.csv

done 

}

for dir in cpuidle_rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs ; anal_outer 
prefix=iptd ; anal_outer 
)
done

