#!/bin/bash

for j in 1 10 20 30 40 ; do 
	for i in 02 04 08 12 16 ; do 
		egrep "${j}," cpu${i}.csv|sed -e 's/'${j}',/'$i',/g' 
	done > pod${j}.csv 
done

