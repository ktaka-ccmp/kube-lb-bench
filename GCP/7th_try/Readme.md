flannel: flannel vxlan mode 

Loadbalancer 

CPU:
kt-lvs002 - kt-lvs008 Intel(R) Xeon(R) CPU @ ? GHz x 16
kt-lvs010 - kt-lvs016 Intel(R) Xeon(R) CPU @ 2.2 GHz x 16
Mem:
16470336 kB

WEB Node: 6
CPU:
Intel(R) Xeon(R) CPU @ 2.20GHz x 16
Mem:
16470340 kB

NIC Queue 16

ktaka@kt-lvs002:~$ egrep virtio1-in  /proc/interrupts  | tr -s ' '|sed -e 's/\ 0/,/g'
 41: 8694456,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.0
 43: 8696850 5,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.1
 45: 9053534,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.2
 47: 8809370,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.3
 49: 9171097,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.4
 51: 7860297,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.5
 53: 8495512,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.6
 55: 8504987,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.7
 57: 8538342,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.8
 59: 8854363,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.9
 61: 9062685,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.10
 63: 8025329,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.11
 65: 8383083,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.12
 67: 8557581,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.13
 69: 8611593,,,,,,,,,,,,,,, PCI-MSI-edge virtio1-input.14
 71: 8023036,,,,,,,,,,,,,, 1 PCI-MSI-edge virtio1-input.15

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


