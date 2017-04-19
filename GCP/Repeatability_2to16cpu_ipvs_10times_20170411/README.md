# Repeatability test for LoadBalancer(ipvs)

http request counts are measured for k8s cluster via ipvs using wrk http stress tool.
Each worker pod runs nginx serving ingress demo page.

While the number of pods are increased, we measured rps for different loadbalancers kt-lvs002, kt-lvs004, kt-lvs008, kt-lvs012, kt-lvs016, where the 
st 2 letters of the instance name indicate # of cpus.
The measurements were done with the increasing cpu counts of load balancers, for each pod number condition.
The number of pods are increased from 1 to 40.

This series of experiments are repeated for 10 times in oder to see the repeatability.

## Node Specs

###  Master node
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

### Worker node x 20
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

### Loadbalancer node
#### kt-lvs002
* Instance Type: custom-2-12288
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 2
* Memory: 12GByte

#### kt-lvs004
* Instance Type: custom-4-16384
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 16GByte

#### kt-lvs008
* Instance Type: custom-8-16384
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 8
* Memory: 16GByte

#### kt-lvs012
* Instance Type: custom-12-16384
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 12
* Memory: 16GByte

#### kt-lvs016
* Instance Type: custom-16-16384
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 16
* Memory: 16GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/coffee

## Experiment date 

* Start: Sun, 02 Apr 2017 16:49:49 +0900
* End: Mon, 03 Apr 2017 07:46:54 +0900

