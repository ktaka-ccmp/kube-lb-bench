#/bin/bash

anal(){

echo \"# of pods\",\"Req/sec\"
egrep "podnum|Requ" $file \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -E -e 's/podnum=//g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal_outer(){
for i in $(seq -w 2 2 16) ; do 
	file=ipvs_lv$i.log
	anal > ipvs_lv$i.csv 

	file=ipt_lv$i.log
	anal > ipt_lv$i.csv 
done 
}

anal_outer


