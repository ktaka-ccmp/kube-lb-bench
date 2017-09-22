flannel: flannel vxlan mode 

CPU:
Intel(R) Xeon(R) CPU @ 2.20GHz x 8
Mem:
16470340 kB

WEB Node: 6

NIC Queue 16

ktaka@kt-lvs002:~$ egrep virtio1-in  /proc/interrupts  | tr -s ' '
 41: 105 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.0
 43: 34 77 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.1
 45: 18 0 70 0 0 0 0 0 PCI-MSI-edge virtio1-input.2
 47: 134 0 0 186 0 0 0 0 PCI-MSI-edge virtio1-input.3
 49: 178 0 0 0 550 0 0 0 PCI-MSI-edge virtio1-input.4
 51: 365 0 0 0 0 314 0 0 PCI-MSI-edge virtio1-input.5
 53: 122 0 0 0 0 0 272 0 PCI-MSI-edge virtio1-input.6
 55: 14 0 0 0 0 0 0 82 PCI-MSI-edge virtio1-input.7


ktaka@kt-lvs002:~$ sudo ethtool -i eth0
driver: virtio_net
version: 1.0.0
firmware-version:
bus-info: 0000:00:04.0
supports-statistics: no
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no

