# RPS vs # pods for 4CPU LoadBalancer

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
* Instance Type: n1-standard-4
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 4
* Memory: 14GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/coffee

## Experiment date 

1st
* Start: Thu, 30 Mar 2017 18:23:23 +0900
* End: Thu, 30 Mar 2017 19:34:44 +0900

2nd
* Start: Fri, 31 Mar 2017 15:08:09 +0900
* End: Fri, 31 Mar 2017 16:19:27 +0900

3rd
* Start: Fri, 31 Mar 2017 16:40:08 +0900
* End: Fri, 31 Mar 2017 17:51:24 +0900




