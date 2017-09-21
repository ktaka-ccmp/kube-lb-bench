flannel: flannel vxlan mode 

LB: m4.16xlarge

CPU:
Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz x64
Mem:
264144576 kB

WEB: m4.4xlarge

CPU:
Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz x 16
Mem:
66099728 kB

WEB Node : 6

NIC Queue: 8
admin@ip-10-0-0-103:~$ egrep eth /proc/interrupts  | tr -s ' '
 435: 5902095 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-0
 436: 5897620 790 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-1
 437: 5863554 0 3102 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-2
 438: 5893524 0 0 245 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-3
 439: 5857584 0 0 0 1450 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-4
 440: 5842844 0 0 0 0 1151 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-5
 441: 5847239 0 0 0 0 0 2372 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-6
 442: 5840827 0 0 0 0 0 0 2352 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-Tx-Rx-7

admin@ip-10-0-0-103:~$ sudo ethtool -i eth0 
driver: ena
version: 1.0.2
firmware-version: 
expansion-rom-version: 
bus-info: 0000:00:03.0
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no


