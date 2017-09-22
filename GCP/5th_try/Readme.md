flannel: flannel vxlan mode 

Loadbalancer 

CPU:
Intel(R) Xeon(R) CPU @ ? GHz x 32
Mem:
33016436 kB

WEB Node: 6
CPU:
Intel(R) Xeon(R) CPU @ 2.20GHz x 16
Mem:
16470340 kB

NIC Queue 16

ktaka@kt-lvs002:~$ egrep virtio1-in  /proc/interrupts  | tr -s ' '
 41: 135219 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.0
 43: 112586 48 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.1
 45: 129840 0 23 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.2
 47: 99949 0 0 758 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.3
 49: 130117 0 0 0 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.4
 51: 108635 0 0 0 0 26 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.5
 53: 116686 0 0 0 0 0 976 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.6
 55: 134146 0 0 0 0 0 0 79 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.7
 57: 94497 0 0 0 0 0 0 0 164 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.8
 59: 128838 0 0 0 0 0 0 0 0 58 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.9
 61: 128764 0 0 0 0 0 0 0 0 0 45 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.10
 63: 103810 0 0 0 0 0 0 0 0 0 0 36 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.11
 65: 116518 0 0 0 0 0 0 0 0 0 0 0 898 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.12
 67: 91641 0 0 0 0 0 0 0 0 0 0 0 0 62 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.13
 69: 105915 0 0 0 0 0 0 0 0 0 0 0 0 0 29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.14
 71: 130908 0 0 0 0 0 0 0 0 0 0 0 0 0 0 28 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.15
 73: 96855 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 33 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.16
 75: 107956 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 60 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.17
 77: 128724 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 59 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.18
 79: 123228 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 59 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.19
 81: 89908 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 26 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.20
 83: 100421 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 38 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.21
 85: 119368 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 43 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.22
 87: 101916 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 45 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.23
 89: 117908 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 112 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.24
 91: 98176 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 75 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.25
 93: 101412 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 41 0 0 0 0 0 PCI-MSI-edge virtio1-input.26
 95: 120336 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 41 0 0 0 0 PCI-MSI-edge virtio1-input.27
 97: 119744 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 42 0 0 0 PCI-MSI-edge virtio1-input.28
 99: 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 118956 0 0 PCI-MSI-edge virtio1-input.29
101: 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 87746 0 PCI-MSI-edge virtio1-input.30
103: 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 102608 PCI-MSI-edge virtio1-input.31



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

