#!/bin/bash

for dir in [A-Z] ;  do 
(cd $dir ; \
for file in */*.log ; do echo -n $dir ': '; egrep Request $file  |awk '{print $2}'|tr '\n' ' ';echo; done \
)
done

