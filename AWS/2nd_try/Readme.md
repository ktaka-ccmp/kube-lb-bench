flannel: flannel vxlan mode 

CPU:
Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz x 16
Mem:
66099728 kB

WEB Node : 6

NIC Queue: 2
admin@ip-10-0-0-101:~$ egrep eth /proc/interrupts  | tr -s ' '
 146: 31696111 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-TxRx-0
 147: 25987572 975973 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-TxRx-1
 148: 14 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0

