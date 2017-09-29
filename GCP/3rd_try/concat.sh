#/bin/bash

concat(){
egrep -v "^\"#" $file
}

concat_outer(){
echo \"# of pods\",\"Req/sec\" > ${prefix}cpu16_all.csv

for i in {0..19} ; do 
	file=${prefix}cpu16_${i}.csv
	concat >> ${prefix}cpu16_all.csv 
done 

}

for dir in rss_* ; do 
echo $dir 
(cd $dir 
prefix=ipvs_ ; concat_outer 
)
done

