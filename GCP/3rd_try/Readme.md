flannel: flannel vxlan mode 

LB:

CPU:
Intel(R) Xeon(R) CPU @ 2.20GHz x 16
Mem:
16470340 kB

WEB Node: 6

CPU:
Intel(R) Xeon(R) CPU @ 2.20GHz x 16
Mem:
16470340 kB

NIC Queue 16
ktaka@kt-lvs002:~$ egrep virtio1-in  /proc/interrupts  | tr -s ' '
 41: 208125 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.0
 43: 168032 211 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.1
 45: 196431 0 125 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.2
 47: 165742 0 0 157 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.3
 49: 188490 0 0 0 126 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.4
 51: 166088 0 0 0 0 126 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.5
 53: 178709 0 0 0 0 0 190 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.6
 55: 187563 0 0 0 0 0 0 2998 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.7
 57: 167909 0 0 0 0 0 0 0 107 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.8
 59: 158759 0 0 0 0 0 0 0 0 239 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.9
 61: 184877 0 0 0 0 0 0 0 0 0 1466 0 0 0 0 0 PCI-MSI-edge virtio1-input.10
 63: 175880 0 0 0 0 0 0 0 0 0 0 1203 0 0 0 0 PCI-MSI-edge virtio1-input.11
 65: 171335 0 0 0 0 0 0 0 0 0 0 0 181 0 0 0 PCI-MSI-edge virtio1-input.12
 67: 163596 0 0 0 0 0 0 0 0 0 0 0 0 166 0 0 PCI-MSI-edge virtio1-input.13
 69: 170083 0 0 0 0 0 0 0 0 0 0 0 0 0 161 0 PCI-MSI-edge virtio1-input.14
 71: 163871 0 0 0 0 0 0 0 0 0 0 0 0 0 0 115 PCI-MSI-edge virtio1-input.15

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

