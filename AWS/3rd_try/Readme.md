flannel: flannel vxlan mode 

WEB: m4.4xlarge
LB: m4.4xlarge

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

/etc/modprobe.d/ixgbevf.conf
 options ixgbevf InterruptThrottleRate=0 RSS=16

sudo update-initramfs -u

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

