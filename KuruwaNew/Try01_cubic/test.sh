#!/bin/bash 

cat <<EOF | ssh k08 "cat - > ./test.sh " 
#!/bin/bash

dstat -Tcn -N eth0,docker0,veth31 -i 1 10 --output dstat.csv > /dev/null 2>&1

EOF

#ssh k08 'chmod +x ./test.sh && ./test.sh' &

#wait


script=./cpuidle.sh
hst=k08
dur=2
dur=0
repl=1
cat <<EOF | ssh $hst "cat - > $script "
#!/bin/bash

dstat -Tcn -N eth0,docker0,veth31 --output dstat$repl.csv -i 1 $((dur*3+5)) > /dev/null 2>&1
EOF

ssh $hst "chmod +x $script  &&  $script" &                                                

wait
