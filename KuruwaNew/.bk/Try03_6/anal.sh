#/bin/bash

anal(){

echo \"# of pods\",\"Req/sec\"
egrep "podnum|Requ" $1 \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -E -e 's/podnum=//g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal_outer(){
for file in ${prefix}*.log ; do 
	echo "anal $file > ${file%.log}.csv "
	anal $file > ${file%.log}.csv
done 

}

for dir in rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs ; anal_outer 
)
done

