# Repeatability test for LoadBalancer(ipvs)

http request counts are measured for k8s cluster via ipvs using wrk http stress tool.
Each worker pod runs nginx serving ingress demo page.

While the number of pods are increased, we measured rps for different loadbalancers kt-lvs002, kt-lvs004, kt-lvs008, kt-lvs012, kt-lvs016, with all having 8 cpus.
The number of pods are increased from 1 to 30.

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


