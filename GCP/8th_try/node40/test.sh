#!/bin/bash

cmd="'hostname; wrk -c800 -t40 -d30s http://35.197.33.30/'"

measure(){
#parallel --will-cite -j 70 -u ssh {} "$cmd" 
parallel -j 70 ssh {} "$cmd" 
}

for i in {11..8} ; do
for j in {1..5} ; do
	echo $j" ;" $(seq 89 $((88 + i)))
	for ip in `seq 89 $((88 + i))` ; do echo 10.0.0.$ip; done | \
	measure > gcplb.$i.log
done
done

