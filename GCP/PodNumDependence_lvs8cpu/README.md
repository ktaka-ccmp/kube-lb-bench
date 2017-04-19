# RPS vs # pods for 8CPU LoadBalancer

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
* Instance Type: n1-standard-8
* CPU: Intel(R) Xeon(R) CPU @ 2.20GHz x 8
* Memory: 30GByte

## Benchmark Command example

wrk -c800 -t40 -d60s http://172.16.121.2/coffee

## Experiment date 

1st
* Start: Fri, 31 Mar 2017 02:12:23 +0900
* End: Fri, 31 Mar 2017 03:23:41 +0900




