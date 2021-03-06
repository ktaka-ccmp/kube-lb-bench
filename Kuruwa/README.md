# Repeatability test for LoadBalancer(ipvs)

http request counts are measured for k8s cluster via ipvs using wrk http stress tool.
Each worker pod runs nginx serving IP address of its own(12-14bytes).

```
root@k12:~/kube-lb-bench/Kuruwa# curl -I http://192.168.0.111:8888/
HTTP/1.1 200 OK
Server: nginx/1.13.0
Date: Thu, 11 May 2017 06:56:29 GMT
Content-Type: text/html
Content-Length: 12
Last-Modified: Thu, 11 May 2017 06:39:34 GMT
Connection: keep-alive
ETag: "59140726-c"
Accept-Ranges: bytes

root@k12:~/kube-lb-bench/Kuruwa# curl http://192.168.0.111:8888/
172.16.61.6
```

# 6th_try
While the number of pods are increased, we measured rps for a loadbalancer with having 8 physical cpus(16 with SMT).
The number of pods are increased from 1 to 40.

Target for ipvs:
http://192.168.0.111:8888/

Target for proxy:(ClusterIP)
http://10.254.0.10/

flannel mode: vxlan

## RSS(Hardware Interrupt)

```
root@k11:~# cat /proc/interrupts |egrep eth0|  tr -s ' '
 81: 828643789 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 IR-PCI-MSI-edge eth0-tx-0
 82: 2675800870 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 IR-PCI-MSI-edge eth0-rx-1
 83: 1371008650 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 IR-PCI-MSI-edge eth0-rx-2
 84: 2319515074 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 IR-PCI-MSI-edge eth0-rx-3
 85: 2359559389 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 IR-PCI-MSI-edge eth0-rx-4

root@k11:~# head /proc/irq/{82..85}/smp_affinity
==> /proc/irq/82/smp_affinity <==
0000,00000001

==> /proc/irq/83/smp_affinity <==
0000,00000001

==> /proc/irq/84/smp_affinity <==
0000,00000001

==> /proc/irq/85/smp_affinity <==
0000,00000001
```

## RPS

```
root@k11:~# head /sys/class/net/eth0/queues/rx-*/rps_cpus
==> /sys/class/net/eth0/queues/rx-0/rps_cpus <==
00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe

==> /sys/class/net/eth0/queues/rx-1/rps_cpus <==
00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe

==> /sys/class/net/eth0/queues/rx-2/rps_cpus <==
00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe

==> /sys/class/net/eth0/queues/rx-3/rps_cpus <==
00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
```

## RFS

```
root@k11:~# cat /proc/sys/net/core/rps_sock_flow_entries
32768
root@k11:~# head /sys/class/net/eth0/queues/rx-*/rps_flow_cnt
==> /sys/class/net/eth0/queues/rx-0/rps_flow_cnt <==
8192

==> /sys/class/net/eth0/queues/rx-1/rps_flow_cnt <==
8192

==> /sys/class/net/eth0/queues/rx-2/rps_flow_cnt <==
8192

==> /sys/class/net/eth0/queues/rx-3/rps_flow_cnt <==
8192

```

## CPU interrupt statitstics
```
root@k11:~# mpstat -P ALL
Linux 3.16.0-4-amd64 (k11)      05/11/17        _x86_64_        (16 CPU)

16:32:29     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
16:32:29     all    0.37    0.00    0.45    0.03    0.00    0.56    0.00    0.00    0.00   98.60
16:32:29       0    0.30    0.00    0.24    0.39    0.00    0.52    0.00    0.00    0.00   98.56
16:32:29       1    0.31    0.00    0.22    0.07    0.00    1.16    0.00    0.00    0.00   98.24
16:32:29       2    0.32    0.00    0.20    0.01    0.00    1.18    0.00    0.00    0.00   98.28
16:32:29       3    0.31    0.00    0.19    0.00    0.00    1.20    0.00    0.00    0.00   98.29
16:32:29       4    0.34    0.00    0.34    0.00    0.00    1.25    0.00    0.00    0.00   98.07
16:32:29       5    0.32    0.00    0.21    0.00    0.00    1.21    0.00    0.00    0.00   98.26
16:32:29       6    0.42    0.00    0.63    0.00    0.00    1.24    0.00    0.00    0.00   97.71
16:32:29       7    0.35    0.00    0.28    0.00    0.00    1.20    0.00    0.00    0.00   98.17
16:32:29       8    0.66    0.00    1.31    0.00    0.00    0.00    0.00    0.00    0.00   98.03
16:32:29       9    0.40    0.00    0.62    0.00    0.00    0.00    0.00    0.00    0.00   98.98
16:32:29      10    0.37    0.00    0.49    0.00    0.00    0.00    0.00    0.00    0.00   99.14
16:32:29      11    0.34    0.00    0.44    0.00    0.00    0.00    0.00    0.00    0.00   99.22
16:32:29      12    0.32    0.00    0.41    0.00    0.00    0.00    0.00    0.00    0.00   99.26
16:32:29      13    0.35    0.00    0.41    0.00    0.00    0.00    0.00    0.00    0.00   99.25
16:32:29      14    0.44    0.00    0.70    0.00    0.00    0.00    0.00    0.00    0.00   98.86
16:32:29      15    0.35    0.00    0.47    0.00    0.00    0.00    0.00    0.00    0.00   99.17

root@k11:~# mpstat -I CPU |awk '{printf "%s %-3s %-10s %-10s %-10s %-10s %-10s\n",$1,$2,$19,$20,$21,$22,$23}'
Linux 3.16.0-4-amd64

16:49:40 CPU 81/s       82/s       83/s       84/s       85/s
16:49:40 0   929.42     2983.44    1546.38    2587.51    2631.42
16:49:40 1   0.00       0.00       0.00       0.00       0.00
16:49:40 2   0.00       0.00       0.00       0.00       0.00
16:49:40 3   0.00       0.00       0.00       0.00       0.00
16:49:40 4   0.00       0.00       0.00       0.00       0.00
16:49:40 5   0.00       0.00       0.00       0.00       0.00
16:49:40 6   0.00       0.00       0.00       0.00       0.00
16:49:40 7   0.00       0.00       0.00       0.00       0.00
16:49:40 8   0.00       0.00       0.00       0.00       0.00
16:49:40 9   0.00       0.00       0.00       0.00       0.00
16:49:40 10  0.00       0.00       0.00       0.00       0.00
16:49:40 11  0.00       0.00       0.00       0.00       0.00
16:49:40 12  0.00       0.00       0.00       0.00       0.00
16:49:40 13  0.00       0.00       0.00       0.00       0.00
16:49:40 14  0.00       0.00       0.00       0.00       0.00
16:49:40 15  0.00       0.00       0.00       0.00       0.00

root@k11:~# mpstat -I SCPU
Linux 3.16.0-4-amd64 (k11)      05/11/17        _x86_64_        (16 CPU)

16:50:23     CPU       HI/s    TIMER/s   NET_TX/s   NET_RX/s    BLOCK/s BLOCK_IOPOLL/s  TASKLET/s    SCHED/s  HRTIMER/s      RCU/s
16:50:23       0       0.00      12.09     800.40     565.12       2.12       0.00       1.30      14.10       0.03      12.87
16:50:23       1       0.00      16.13       7.02    1681.44       0.03       0.00       0.00      15.95       0.03      19.40
16:50:23       2       0.00      15.46       7.22    1674.51       0.00       0.00       0.00      15.05       0.03      21.58
16:50:23       3       0.00      15.16       7.22    1675.75       0.00       0.00       0.00      14.74       0.03      21.07
16:50:23       4       0.00      20.71       7.07    1671.56       0.00       0.00       0.00      20.17       0.03      26.90
16:50:23       5       0.00      15.23       6.97    1677.83       0.00       0.00       0.00      14.78       0.03      21.21
16:50:23       6       0.00      17.77       7.25    1667.98       0.00       0.00       0.00      17.28       0.03      25.68
16:50:23       7       0.00      16.48       6.54    1682.95       0.00       0.00       0.00      16.05       0.03      23.18
16:50:23       8       0.00      13.17       0.00       0.08       0.00       0.00       0.00      12.36       0.01      34.84
16:50:23       9       0.00       9.77       0.00       0.04       0.00       0.00       0.00       9.31       0.01      17.44
16:50:23      10       0.00       8.40       0.00       0.04       0.00       0.00       0.00       8.00       0.01      14.29
16:50:23      11       0.00       7.89       0.00       0.05       0.00       0.00       0.00       7.54       0.01      12.03
16:50:23      12       0.00      10.20       0.00       0.06       0.00       0.00       0.00       9.86       0.01      13.15
16:50:23      13       0.00       7.62       0.00       0.05       0.00       0.00       0.00       7.27       0.01      10.86
16:50:23      14       0.00      10.38       0.00       0.05       0.00       0.00       0.00       9.92       0.01      20.05
16:50:23      15       0.00       8.24       0.00       0.05       0.00       0.00       0.00       7.87       0.01      12.35

root@k11:~# mpstat -I SCPU |awk '{printf "%s %-3s %-10s %-10s\n",$1,$2,$4,$5}'
Linux 3.16.0-4-amd64 05/11/17   _x86_64_

16:52:05 CPU TIMER/s    NET_TX/s
16:52:05 0   12.09      802.30
16:52:05 1   16.13      7.04
16:52:05 2   15.47      7.24
16:52:05 3   15.16      7.24
16:52:05 4   20.71      7.09
16:52:05 5   15.23      6.99
16:52:05 6   17.78      7.27
16:52:05 7   16.49      6.56
16:52:05 8   13.17      0.00
16:52:05 9   9.77       0.00
16:52:05 10  8.40       0.00
16:52:05 11  7.89       0.00
16:52:05 12  10.20      0.00
16:52:05 13  7.62       0.00
16:52:05 14  10.38      0.00
16:52:05 15  8.24       0.00

```

# 7th_try

Same with the 6th_try, only with proxy.

# 8th_try

Same with the 6th_try, only with ipvs.


# 9th_try

flanneld: host-gw

k12: rss=off, rps=on, rfs=off
k11: rss=on, rps=on, rfs=on

```
root@k11:~# ./irq_chk.sh
/proc/irq/82/smp_affinity : 0000,00000001
/proc/irq/83/smp_affinity : 0000,00000004
/proc/irq/84/smp_affinity : 0000,00000010
/proc/irq/85/smp_affinity : 0000,00000040
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/proc/sys/net/core/rps_sock_flow_entries : 32768
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 8192
```

```
root@k12:~/kube-lb-bench/Kuruwa/9th_try# ./irq_chk.sh
/proc/irq/82/smp_affinity : 0000,00000001
/proc/irq/83/smp_affinity : 0000,00000001
/proc/irq/84/smp_affinity : 0000,00000001
/proc/irq/85/smp_affinity : 0000,00000001
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/proc/sys/net/core/rps_sock_flow_entries : 0
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 0
```

```
mpstat -P ALL 1 10

Average:     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
Average:     all    0.42    0.00    0.48    0.01    0.00    3.90    0.00    0.00    0.00   95.19
Average:       0    0.39    0.00    0.39    0.78    0.00   24.22    0.00    0.00    0.00   74.22
Average:       1    0.00    0.00    0.13    0.00    0.00    3.76    0.00    0.00    0.00   96.11
Average:       2    0.19    0.00    0.19    0.00    0.00    6.63    0.00    0.00    0.00   92.98
Average:       3    0.26    0.00    0.13    0.00    0.00    5.41    0.00    0.00    0.00   94.20
Average:       4    0.39    0.00    0.58    0.00    0.00    8.16    0.00    0.00    0.00   90.87
Average:       5    0.13    0.00    0.00    0.00    0.00    3.96    0.00    0.00    0.00   95.90
Average:       6    2.53    0.00    0.00    0.00    0.00    7.78    0.00    0.00    0.00   89.69
Average:       7    0.00    0.00    0.00    0.00    0.00    3.58    0.00    0.00    0.00   96.42
Average:       8    1.49    0.00    0.75    0.00    0.00    3.13    0.00    0.00    0.00   94.63
Average:       9    0.27    0.00    0.41    0.00    0.00    1.22    0.00    0.00    0.00   98.10
Average:      10    0.15    0.00    1.02    0.00    0.00    2.19    0.00    0.00    0.00   96.64
Average:      11    0.14    0.00    0.14    0.00    0.00    0.97    0.00    0.00    0.00   98.75
Average:      12    0.58    0.00    0.29    0.00    0.00    1.32    0.00    0.00    0.00   97.81
Average:      13    0.14    0.00    0.41    0.00    0.00    1.89    0.00    0.00    0.00   97.56
Average:      14    0.42    0.00    2.54    0.00    0.00    3.25    0.00    0.00    0.00   93.79
Average:      15    0.27    0.00    0.55    0.00    0.00    1.10    0.00    0.00    0.00   98.08
```

# 10th_try

flanneld: host-gw

k12: rss=off, rps=on, rfs=off
k11: rss=off, rps=off, rfs=off

```
t@k11:~# ./irq_chk.sh
/proc/irq/82/smp_affinity : 0000,0000ffff
/proc/irq/83/smp_affinity : 0000,0000ffff
/proc/irq/84/smp_affinity : 0000,0000ffff
/proc/irq/85/smp_affinity : 0000,0000ffff
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/proc/sys/net/core/rps_sock_flow_entries : 0
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 0
```

```
root@k12:~/kube-lb-bench/Kuruwa/10th_try# ~/irq_chk.sh
/proc/irq/82/smp_affinity : 0000,00000001
/proc/irq/83/smp_affinity : 0000,00000001
/proc/irq/84/smp_affinity : 0000,00000001
/proc/irq/85/smp_affinity : 0000,00000001
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,000000fe
/proc/sys/net/core/rps_sock_flow_entries : 0
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 0
```

```
root@k11:~# mpstat -P ALL 1 1
Average:     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
Average:     all    0.25    0.00    0.21    0.05    0.00    3.36    0.00    0.00    0.00   96.13
Average:       0    0.00    0.00    0.00    0.00    0.00   99.62    0.00    0.00    0.00    0.38
Average:       1    0.30    0.00    0.30    0.40    0.00    0.00    0.00    0.00    0.00   99.00
Average:       2    0.20    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.60
Average:       3    0.00    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.90
Average:       4    0.10    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.80
Average:       5    0.60    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.30
Average:       6    0.20    0.00    0.10    0.40    0.00    0.00    0.00    0.00    0.00   99.30
Average:       7    0.20    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.70
Average:       8    0.90    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.00
Average:       9    0.10    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.70
Average:      10    0.30    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.60
Average:      11    0.30    0.00    0.70    0.00    0.00    0.00    0.00    0.00    0.00   99.00
Average:      12    0.40    0.00    0.60    0.00    0.00    0.00    0.00    0.00    0.00   99.00
Average:      13    0.00    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.90
Average:      14    0.20    0.00    0.10    0.00    0.00    0.00    0.00    0.00    0.00   99.70
Average:      15    0.20    0.00    0.40    0.00    0.00    0.00    0.00    0.00    0.00   99.40
```

# 11th_try

flanneld: host-gw

k12: rss=off, rps=on, rfs=off
k11: rss=on, rps=off, rfs=off

```
root@k11:~# ./irq_chk.sh
/proc/irq/82/smp_affinity : 0000,00000001
/proc/irq/83/smp_affinity : 0000,00000004
/proc/irq/84/smp_affinity : 0000,00000010
/proc/irq/85/smp_affinity : 0000,00000040
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
/proc/sys/net/core/rps_sock_flow_entries : 0
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 0
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 0
```

```
root@k11:~# mpstat -P ALL 1 1
Average:     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
Average:     all    0.31    0.00    0.34    0.00    0.00    3.03    0.00    0.00    0.00   96.32
Average:       0    0.64    0.00    0.64    0.00    0.00   36.31    0.00    0.00    0.00   62.42
Average:       1    0.40    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00   99.60
Average:       2    0.79    0.00    0.00    0.00    0.00   30.26    0.00    0.00    0.00   68.95
Average:       3    0.10    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00   99.90
Average:       4    0.50    0.00    1.00    0.00    0.00   33.33    0.00    0.00    0.00   65.16
Average:       5    0.30    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.50
Average:       6    0.28    0.00    0.28    0.00    0.00   27.42    0.00    0.00    0.00   72.02
Average:       7    0.00    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.80
Average:       8    0.20    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.60
Average:       9    0.10    0.00    0.30    0.00    0.00    0.00    0.00    0.00    0.00   99.60
Average:      10    0.20    0.00    0.40    0.00    0.00    0.00    0.00    0.00    0.00   99.40
Average:      11    0.30    0.00    0.70    0.00    0.00    0.00    0.00    0.00    0.00   99.00
Average:      12    1.20    0.00    0.50    0.00    0.00    0.00    0.00    0.00    0.00   98.30
Average:      13    0.00    0.00    0.30    0.00    0.00    0.00    0.00    0.00    0.00   99.70
Average:      14    0.50    0.00    0.90    0.00    0.00    0.00    0.00    0.00    0.00   98.60
Average:      15    0.30    0.00    0.20    0.00    0.00    0.00    0.00    0.00    0.00   99.50
```

# 12th_try

flanneld: udp

k12: rss=off, rps=on, rfs=off
k11: rss=on, rps=on, rfs=on

```
root@k11:~# ./irq_chk.sh
/proc/irq/82/smp_affinity : 0000,00000001
/proc/irq/83/smp_affinity : 0000,00000004
/proc/irq/84/smp_affinity : 0000,00000010
/proc/irq/85/smp_affinity : 0000,00000040
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/proc/sys/net/core/rps_sock_flow_entries : 32768
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 8192
```

```
Average:     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
Average:     all    0.49    0.00    4.17    0.00    0.00    3.42    0.00    0.00    0.00   91.92
Average:       0    0.35    0.00    0.94    0.00    0.00    1.42    0.00    0.00    0.00   97.29
Average:       1    0.21    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00   99.79
Average:       2    2.40    0.00   51.30    0.00    0.00   46.30    0.00    0.00    0.00    0.00
Average:       3    0.65    0.00    1.53    0.00    0.00    0.33    0.00    0.00    0.00   97.49
Average:       4    0.78    0.00    0.00    0.00    0.00    0.11    0.00    0.00    0.00   99.11
Average:       5    0.31    0.00    0.20    0.00    0.00    0.61    0.00    0.00    0.00   98.88
Average:       6    0.00    0.00    0.00    0.00    0.00    0.55    0.00    0.00    0.00   99.45
Average:       7    0.22    0.00    2.20    0.00    0.00    0.44    0.00    0.00    0.00   97.14
Average:       8    0.21    0.00    0.41    0.00    0.00    0.31    0.00    0.00    0.00   99.07
Average:       9    0.21    0.00    0.31    0.00    0.00    0.10    0.00    0.00    0.00   99.38
Average:      10    0.11    0.00    0.11    0.00    0.00    0.11    0.00    0.00    0.00   99.68
Average:      11    0.22    0.00    1.31    0.00    0.00    0.44    0.00    0.00    0.00   98.03
Average:      12    0.21    0.00    0.41    0.00    0.00    0.00    0.00    0.00    0.00   99.38
Average:      13    0.20    0.00    1.02    0.00    0.00    0.20    0.00    0.00    0.00   98.57
Average:      14    1.03    0.00    0.41    0.00    0.00    0.10    0.00    0.00    0.00   98.45
Average:      15    0.59    0.00    3.88    0.00    0.00    1.06    0.00    0.00    0.00   94.47
```

# 13th_try

flanneld: vxlan

k12: rss=off, rps=on, rfs=off
k11: rss=on, rps=on, rfs=on

```
root@k11:~# ./irq_chk.sh
/proc/irq/82/smp_affinity : 0000,00000001
/proc/irq/83/smp_affinity : 0000,00000004
/proc/irq/84/smp_affinity : 0000,00000010
/proc/irq/85/smp_affinity : 0000,00000040
/sys/class/net/eth0/queues/rx-0/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-1/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-2/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/sys/class/net/eth0/queues/rx-3/rps_cpus : 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,0000ffff
/proc/sys/net/core/rps_sock_flow_entries : 32768
/sys/class/net/eth0/queues/rx-0/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-1/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-2/rps_flow_cnt : 8192
/sys/class/net/eth0/queues/rx-3/rps_flow_cnt : 8192
```

```
mpstat -P ALL 1 10
Average:     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
Average:     all    0.42    0.00    0.42    0.04    0.00    5.23    0.00    0.00    0.00   93.89
Average:       0    0.33    0.00    0.00    0.33    0.00   29.43    0.00    0.00    0.00   69.90
Average:       1    0.00    0.00    0.14    0.00    0.00    5.40    0.00    0.00    0.00   94.46
Average:       2    0.67    0.00    0.50    0.00    0.00    7.51    0.00    0.00    0.00   91.32
Average:       3    0.13    0.00    0.27    0.00    0.00    6.21    0.00    0.00    0.00   93.39
Average:       4    0.41    0.00    0.41    0.00    0.00    9.80    0.00    0.00    0.00   89.39
Average:       5    1.24    0.00    0.14    0.00    0.00    5.65    0.00    0.00    0.00   92.98
Average:       6    0.20    0.00    0.61    0.00    0.00   10.82    0.00    0.00    0.00   88.37
Average:       7    1.24    0.00    0.14    0.00    0.00    5.92    0.00    0.00    0.00   92.70
Average:       8    0.48    0.00    0.97    0.00    0.00    3.54    0.00    0.00    0.00   95.01
Average:       9    0.00    0.00    0.15    0.29    0.00    1.47    0.00    0.00    0.00   98.09
Average:      10    0.45    0.00    0.30    0.00    0.00    2.09    0.00    0.00    0.00   97.17
Average:      11    0.15    0.00    0.29    0.00    0.00    1.60    0.00    0.00    0.00   97.97
Average:      12    0.77    0.00    1.70    0.00    0.00    4.33    0.00    0.00    0.00   93.19
Average:      13    0.57    0.00    0.43    0.00    0.00    2.00    0.00    0.00    0.00   97.00
Average:      14    0.16    0.00    0.47    0.00    0.00    3.13    0.00    0.00    0.00   96.24
Average:      15    0.14    0.00    0.14    0.00    0.00    1.30    0.00    0.00    0.00   98.41
```

```
root@k11:~# ifconfig eth0
eth0      Link encap:Ethernet  HWaddr b0:83:fe:e7:d8:b8
          inet addr:192.168.0.111  Bcast:192.168.0.255  Mask:255.255.255.0
          inet6 addr: fe80::b283:feff:fee7:d8b8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1014683909 errors:0 dropped:1108 overruns:0 frame:0
          TX packets:1014308027 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:168056213062 (156.5 GiB)  TX bytes:167913604597 (156.3 GiB)
          Interrupt:16

root@k11:~# ifconfig flannel.1
flannel.1 Link encap:Ethernet  HWaddr 96:57:22:a1:2a:1e
          inet addr:172.16.72.0  Bcast:0.0.0.0  Mask:255.255.255.255
          inet6 addr: fe80::9457:22ff:fea1:2a1e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1450  Metric:1
          RX packets:506647891 errors:0 dropped:0 overruns:0 frame:0
          TX packets:507606022 errors:0 dropped:116446 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:87701587263 (81.6 GiB)  TX bytes:51763871887 (48.2 GiB)
```


## Node Specs

###  Master node k04
* CPU: Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz x 16(HT)
* Memory: 32GByte

### Worker node k05-k10 
* CPU: Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz x 16(HT)
* Memory: 32GByte

### Loadbalancer node k11
* CPU: Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz x 16(HT)
* Memory: 32GByte

### Benchmarker node k12
* CPU: Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz x 16(HT)
* Memory: 32GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/

