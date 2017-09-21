flannel: flannel vxlan mode 

LB: c4.8xlarge

CPU:
Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz x 36
Mem:
61962656 kB


WEB: m4.4xlarge

CPU:
Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz x 16
Mem:
66099728 kB

WEB Node : 6

NIC Queue: 2
admin@ip-10-0-0-102:~$ egrep eth /proc/interrupts  | tr -s ' '
 246: 444 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-TxRx-0
 247: 6 552 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0-TxRx-1
 248: 12 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 xen-pirq-msi-x eth0

admin@ip-10-0-0-102:~$ sudo ethtool -i eth0
driver: ixgbevf
version: 2.16.4
firmware-version: N/A
bus-info: 0000:00:03.0
supports-statistics: yes
supports-test: yes
supports-eeprom-access: no
supports-register-dump: yes
supports-priv-flags: no

/etc/modprobe.d/ixgbevf.conf
 options ixgbevf InterruptThrottleRate=0

sudo update-initramfs -u

