#!/bin/bash

in=./lbnum.csv
out=./lbnum2.csv
delay=na
pd_prev=
tm_prev=
tm0=na
DURATION=72000

output(){
	echo $tm,$pd,$rt,$delay
}

IFS=, read -r tm0 pd rt < $in
#echo $tm0

while IFS=, read -r tm pd rt ; do

#[[ "$(( $tm - $tm0 ))" -gt "$DURATION" ]] && echo $tm >&2 
[[ "$(( $tm - $tm0 ))" -gt "$DURATION" ]] && break 

if [ "$pd" == "$rt" ] ; then

	if [ "$pd" != "$pd_prev" -a "$pd_prev" != "" ] ; then

		if [ "$tm" == "$tm_prev" ] ; then
			delay=0
		else
			delay=$(bc <<< $tm-$tm_prev-0.1 ) 
		fi

		output
		delay=na
	elif [ "$delay" != "na" -a "$delay" != "" ]; then
		tm_tmp=$tm
		tm=$tm1; pd=$pd1; rt=$rt1
		output
		tm=$tm_tmp
		delay=na
	else
		delay=na
	fi
	tm_prev=$tm
else
	if [ "$pd" != "$pd_prev" -a "$pd_prev" != "" ] ; then
		tm1=$tm; pd1=$pd; rt1=$rt
	fi

	if [ "$tm" == "$tm_prev" ] ; then
		delay=0
	else
		delay=$(bc <<< $tm-$tm_prev-0.1 ) 
	fi
fi

pd_prev=$pd

done  <  $in  > $out




