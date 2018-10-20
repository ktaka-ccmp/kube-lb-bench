#!/bin/bash

egrep "Socket|requests"  Try0*/rss_rps_rfs_xps_*/ipvs*_*.log \
| egrep -B 1 Socket |sed -e 's/.*log:  \([0-9]*\)/Req \1/g' -e 's/requests.*//g' -e 's/.*Socket.*timeout /Err /g' \
|sed  -e 'N;N;s/\n/ /g' \
| awk '{q=$4/$2*100; if (q > 0.01) {printf; print " " q "%"} }'


