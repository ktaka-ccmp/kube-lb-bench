#!/bin/bash


for file in */*.log ; do echo -n $file ': '; egrep Request $file  |awk '{print $2}'|tr '\n' ' ';echo; done

