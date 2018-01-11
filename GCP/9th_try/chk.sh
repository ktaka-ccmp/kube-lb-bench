#!/bin/bash


for file in */*3*.log ; do echo -n $file ': '; egrep Request $file  |awk '{print $2}'|tr '\n' ' ';echo; done

