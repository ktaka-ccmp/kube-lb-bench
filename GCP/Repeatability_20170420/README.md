# Repeatability test for LoadBalancer(ipvs)

http request counts are measured for k8s cluster via ipvs using wrk http stress tool.
Each worker pod runs nginx serving ingress demo page.

# 1st_try
While the number of pods are increased, we measured rps for 8 different loadbalancers with all having 8 cpus.
The number of pods are increased from 1 to 30.

Order
kt-lvs002, kt-lvs004, t-lvs006, kt-lvs008, kt-lvs010, kt-lvs012, kt-lvs014, kt-lvs016

I found the connection tracking table on the benchmark client was full during this test.

# 2nd_try

Same with the 1st_try, with reduced number of pod number condition.
Conntrack table is increased by the following line in the ansible playbook.

  - sysctl: name=net.netfilter.nf_conntrack_max value=20000000 sysctl_set=yes
  - sysctl: name=net.nf_conntrack_max value=20000000 sysctl_set=yes


Order
kt-lvs002, kt-lvs004, t-lvs006, kt-lvs008, kt-lvs010, kt-lvs012, kt-lvs014, kt-lvs016

I found the results were almost repeatable.
However kt-lvs008 and kt-lvs010 seemed to have higher score.

# 3rd_try
Same with the 2nd_try, with different order so as to distinguish the general tendency where kt-lvs008 and kt-lvs010 had higher scores was actually due to the measurement order.

Order
kt-lvs008, kt-lvs010, kt-lvs012, kt-lvs014, kt-lvs016, kt-lvs002, kt-lvs004, kt-lvs006 

The kt-lvs008 and kt-lvs010 still had higher scores compared to the other ones.



## Node Specs

###  Master node
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

### Worker node x 10
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

### Loadbalancer node

#### kt-lvs002, kt-lvs004, kt-lvs006, kt-lvs008, kt-lvs010, kt-lvs012, kt-lvs014, kt-lvs016
* Instance Type: custom-8-16384
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 8
* Memory: 16GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/

## Experiment date 

Ascending order
* Start: Wed, 12 Apr 2017 03:12:11 +0900
* End: Wed, 12 Apr 2017 05:12:53 +0900

Descending order
* Start: Wed, 12 Apr 2017 10:06:05 +0900
* End: Wed, 12 Apr 2017 12:06:02 +0900


