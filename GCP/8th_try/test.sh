#!/bin/bash

cmd='hostname; wrk -c800 -t40 -d1s http://35.197.33.30/'

measure(){
#parallel --will-cite -j 70 -u ssh {} "$cmd" 
parallel --will-cite -j 70 ssh {} "$cmd" 
}

for i in {7..1} ; do
for j in {1..10} ; do
	echo $j" ;" $(seq 93 $((92 + i)))
	for ip in `seq 93 $((92 + i))` ; do echo 10.0.0.$ip; done | \
	measure > gcplb.$i.log
done
done

