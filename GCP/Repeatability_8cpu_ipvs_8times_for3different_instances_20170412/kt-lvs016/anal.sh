#/bin/bash

anal(){
file=cpu08_lv16_${1}.log

echo \"# of pods\",\"Req/sec\"
egrep "podnum|Requ" $file \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -E -e 's/podnum=//g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal_outer(){
for i in {1..8} ; do 
	anal $i > cpu08_lv16_$i.csv 
done 

for j in 1 10 20 30 ; do 
	echo \"# of cpu on LB\",\"Req/sec\" > pod${j}.csv
	for i in {1..8} ; do 
		egrep "${j}," cpu08_lv16_${i}.csv|sed -e 's/'${j}',/'$i',/g' 
	done >> pod${j}.csv 
done
}

anal_outer


