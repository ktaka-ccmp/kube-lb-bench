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

	echo \"# of pods\",\"Req/sec\",\"cpu idle\",\"siq\",\"eth0-rx\,\"eth0-tx\,\"docker0-rx\,\"docker0-tx\" > ${file%.log}.csv
 	anal2 $file |
	while read pod t1 rps t2 ; do

#		echo "$pod $rps $t1 $t2"
		echo -n "$pod,$rps,"
		awk "/$t1/,/$t2/" $file.dstat_$pod.csv \
		| awk -F, '{idle+=$4} {siq+=$7} {eth0_rx+=$8} {eth0_tx+=$9} {d0_rx+=$8} {d0_tx+=$9} END \
		{print idle/NR,siq/NR,eth0_rx/NR,eth0_tx/NR,d0_rx/NR,d0_tx/NR}' OFS=,  
	done >> ${file%.log}.csv

done 

}

for dir in cpuidle_rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs ; anal_outer 
prefix=ipvstun ; anal_outer 
#prefix=iptd ; anal_outer 
)
done

