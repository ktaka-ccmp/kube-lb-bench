flannel: flannel vxlan mode 

LB: m4.10xlarge

CPU:
Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz x 40
Mem:
165386596 kB

WEB: m4.4xlarge

CPU:
Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz x 16
Mem:
66099728 kB

WEB Node : 6

NIC Queue: 8
admin@ip-10-0-0-101:~$ egrep eth /proc/interrupts  | tr -s ' '
 266: 1065 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-TxRx-0
 267: 6 1315 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-TxRx-1
 268: 12 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0



admin@ip-10-0-0-101:~$ sudo ethtool -i eth0
driver: ixgbevf
version: 2.16.4
firmware-version: N/A
bus-info: 0000:00:03.0
supports-statistics: yes
supports-test: yes
supports-eeprom-access: no
supports-register-dump: yes
supports-priv-flags: no



