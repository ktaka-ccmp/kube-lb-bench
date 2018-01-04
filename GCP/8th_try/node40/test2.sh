#!/bin/bash

cmd="'hostname; wrk -c800 -t40 -d30s http://35.197.33.30/'"

measure(){
#parallel --will-cite -j 70 -u ssh {} "$cmd" 
parallel -j 70 ssh {} "$cmd" 
}

for j in {1..10} ; do
echo $j
	for ip in `seq 89 91` ; do echo 10.0.0.$ip; done | \
	measure |egrep Requ
echo

done

