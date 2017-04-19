# Repeatability test for LoadBalancer(ipvs)

http request counts are measured for k8s cluster via ipvs using wrk http stress tool.
Each worker pod runs nginx serving ingress demo page.

While the number of pods are increased, we measured rps for different loadbalancers kt-lvs002, kt-lvs008, kt-lvs016, with all of them having 8 cpus.
The number of pods are increased from 1 to 35.

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

#### kt-lvs002, kt-lvs008, kt-lvs016
* Instance Type: custom-8-16384
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 8
* Memory: 16GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/

## Experiment date 

kt-lvs002
* Start: Wed, 12 Apr 2017 17:10:56 +0900
* End: Wed, 12 Apr 2017 19:36:19 +0900

kt-lvs008
* Start: Wed, 12 Apr 2017 12:22:56 +0900
* End: Wed, 12 Apr 2017 14:40:10 +0900

kt-lvs016
* Start: Wed, 12 Apr 2017 14:48:44 +0900
* End: Wed, 12 Apr 2017 16:53:31 +0900

