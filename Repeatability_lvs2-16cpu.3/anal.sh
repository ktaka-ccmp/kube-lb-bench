#/bin/bash

file=lvs_cpu${1}.log

egrep "podnum|Requ" $file \
|awk '/^podnum/ { printf("%s,", $0); next } 1' \
|egrep -v "podnum=.*,podnum" \
| sed -e 's/podnum=//g' -e 's/Requests\/sec:  //g'

