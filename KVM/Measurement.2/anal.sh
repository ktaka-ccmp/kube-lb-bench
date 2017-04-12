#/bin/bash

anal(){
file=${prefix}cpu${1}.log

echo \"# of pods\",\"Req/sec\"
egrep "podnum|Requ" $file \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -E -e 's/podnum=//g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal_outer(){
for i in 02 04 08 12 16 ; do 
	anal $i > ${prefix}cpu$i.csv 
done 

for j in 1 10 20 30 40 ; do 
	echo \"# of cpu on LB\",\"Req/sec\" > ${prefix}pod${j}.csv
	for i in 02 04 08 12 16 ; do 
		egrep "${j}," ${prefix}cpu${i}.csv|sed -e 's/'${j}',/'$i',/g' 
	done >> ${prefix}pod${j}.csv 
done
}

prefix=lvs_ ; anal_outer
prefix=proxy_ ; anal_outer


