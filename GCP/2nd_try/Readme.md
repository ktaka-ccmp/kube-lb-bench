flannel: flannel vxlan mode 

CPU:
Intel(R) Xeon(R) CPU @ 2.20GHz x 16
Mem:
16470340 kB

NIC Queue 16
ktaka@kt-lvs002:~$ egrep virtio1-in  /proc/interrupts  | tr -s ' '
 41: 2728228 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.0
 43: 1 4429433 0 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.1
 45: 1 0 2786264 0 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.2
 47: 1 0 0 2796859 0 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.3
 49: 1 0 0 0 3498361 0 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.4
 51: 1 0 0 0 0 2806304 0 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.5
 53: 1 0 0 0 0 0 3122193 0 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.6
 55: 1 0 0 0 0 0 0 3010527 0 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.7
 57: 1 0 0 0 0 0 0 0 2838006 0 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.8
 59: 1 0 0 0 0 0 0 0 0 2869409 0 0 0 0 0 0 PCI-MSI-edge virtio1-input.9
 61: 1 0 0 0 0 0 0 0 0 0 2849972 0 0 0 0 0 PCI-MSI-edge virtio1-input.10
 63: 1 0 0 0 0 0 0 0 0 0 0 2769334 0 0 0 0 PCI-MSI-edge virtio1-input.11
 65: 1 0 0 0 0 0 0 0 0 0 0 0 2818778 0 0 0 PCI-MSI-edge virtio1-input.12
 67: 1 0 0 0 0 0 0 0 0 0 0 0 0 2727862 0 0 PCI-MSI-edge virtio1-input.13
 69: 1 0 0 0 0 0 0 0 0 0 0 0 0 0 2833642 0 PCI-MSI-edge virtio1-input.14
 71: 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2777891 PCI-MSI-edge virtio1-input.15


