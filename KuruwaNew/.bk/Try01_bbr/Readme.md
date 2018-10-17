flannel: flannel host-gw mode 
rps=1 means fffe
rfs=0

lvs: k07, k08, k09, k10 (all w tg3 @1Gbps)
node: k03, k04, k05, k06, k13, k14
client: k11

/proc/sys/net/ipv4/tcp_congestion_control
	(client, ipvs, node) = (bbr, bbr, bbr)

