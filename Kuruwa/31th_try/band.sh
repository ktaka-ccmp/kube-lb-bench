#/bin/bash

anal(){

echo \"Payload size\",\"Req/sec\",\"Byte/sec\"
egrep "size|Requests/sec|Transfer/sec" $file \
| awk '/^Requests/ { printf("%s,", $0); next } 1' \
| awk '/^size/ { printf("%s,", $0); next } 1' \
| sed -E -e 's/size=//g' -e 's/Requests\/sec:[[:space:]]+//g' -e 's/Transfer\/sec:[[:space:]]+//g' -e 's/MB//g'

}

anal_outer(){
for i in pod40 ; do 
	file=${prefix}cpu16_${i}.log
	anal > ${prefix}cpu16_${i}.csv 
done 

}

for dir in rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs_ ; anal_outer 
)
done

