#/bin/bash

anal(){

echo \"# of pods\",\"Req/sec\"
egrep "podnum|Requ" $file \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -E -e 's/podnum=//g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal_outer(){
for i in {0..0} ; do 
	file=${prefix}cpu16_${i}.log
	anal > ${prefix}cpu16_${i}.csv 
done 

}

for dir in rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs_ ; anal_outer 
prefix=lvs_ ; anal_outer 
prefix=proxy_ ; anal_outer 
)
done

