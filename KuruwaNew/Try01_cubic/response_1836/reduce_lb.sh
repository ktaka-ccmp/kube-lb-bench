#!/bin/bash

in=./lbnum.csv

while IFS=, read -r tm pd rt ; do

	[[ "$rt" -gt "$pd" ]] && echo $tm,$pd,$rt

done  <  $in  



