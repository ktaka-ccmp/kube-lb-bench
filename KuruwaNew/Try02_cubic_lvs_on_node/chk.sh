#!/bin/bash


for file in rss_rps_rfs_xps_1*/*.log ; do echo -n ${file##*/} ': '; egrep Request $file  |awk '{print $2}'|tr '\n' ' ';echo; done

