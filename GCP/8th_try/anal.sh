#!/bin/bash

anal(){
echo \"\# of client\",\"Throughpu [req/s]\"

for i in {1..11}; do
	total=0
	echo -n $i","
	egrep Requests  gcplb.$i.log |\
	(while read dummy line ; do 
 		total=$( bc <<< "$total + $line")
	done 
	echo $total)
done
}

anal_outer(){
	echo 	"anal > $dir.csv "
	anal > $dir.csv
}

for dir in node[0-9]* ; do 
echo $dir 
(cd $dir 
anal_outer 
)
done

