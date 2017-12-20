#/bin/bash

anal(){

echo \"Epoch\",\"Req/sec\"
egrep "Start time: |Requ" $file \
|awk '/^Start/ { printf("%s,", $0); next } 1' \
| sed -E -e 's/Start time: //g' -e 's/Requests\/sec:[[:space:]]+//g'
}

anal_outer(){
for file in *.log ; do 
	echo 	"anal > ${file%.log}.csv "
	anal > ${file%.log}.csv
done 

}

for dir in rss_* ; do 
echo $dir 
(cd $dir 
anal_outer 
)
done

