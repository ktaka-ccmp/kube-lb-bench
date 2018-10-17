flannel: flannel host-gw mode 
rps=1 means fffe
rfs=0

lvs: k12  (w ixgbe @10Gbps)
node: k04
client: k11

/proc/sys/net/ipv4/tcp_congestion_control
	(client, ipvs, node) = (bbr, bbr, bbr)

