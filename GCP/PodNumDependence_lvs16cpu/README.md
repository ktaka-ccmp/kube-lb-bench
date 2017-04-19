# RPS vs # pods for 16CPU LoadBalancer

http request counts are measured for direct single pod, via proxy(iptables), via ingress(nginx) and via ipvs using wrk http stress tool.
Each work pod runs nginx serving ingress demo page.

## Node Specs

###  Master node
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

### Worker node
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

### Loadbalancer node
* Instance Type: n1-standard-16
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 16
* Memory: 60GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/coffee

## Experiment date 

1st
* Start: Thu, 30 Mar 2017 20:34:55 +0900
* End: Thu, 30 Mar 2017 21:46:11 +0900

2nd
* Start: Fri, 31 Mar 2017 10:51:09 +0900
* End: Fri, 31 Mar 2017 12:16:51 +0900



