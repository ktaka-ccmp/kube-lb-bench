#!/bin/bash

in=./lbnum.csv
out=./lbnum2.csv
delay=
pd_prev=
tm_prev=

output(){
	echo $tm,$pd,$rt,$delay
}

while IFS=, read -r tm pd rt ; do

if [ "$pd" == "$rt" ] ; then

	if [ "$pd" != "$pd_prev" -a "$pd_prev" != "" ] ; then
		delay=$(( $tm - $tm_prev -1 )).5
		output
		delay=-1
	elif [ "$delay" != "-1" -a "$delay" != "" ]; then
		echo $tm,$pd1,$rt1,$delay
		delay=-1
	else
		delay=-1
#		output
	fi
	tm_prev=$tm
else
	if [ "$pd" != "$pd_prev" -a "$pd_prev" != "" ] ; then
		tm1=$tm; pd1=$pd; rt1=$rt
	fi
	delay=$(( $tm - $tm_prev -1)).5
#	output
fi

pd_prev=$pd

done  <  $in  > $out




