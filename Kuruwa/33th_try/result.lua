done = function(summary, latency, requests)
   io.write("------------------------------\n")
   for p=1,99 do
      n = latency:percentile(p/100)
      io.write(string.format("percentile,%g,%g\n", p/10000, n/1000000))
   end
   for p=1,99 do
      n = latency:percentile(p)
      io.write(string.format("percentile,%g,%g\n", p/100, n/1000000))
   end
   for p=1,99 do
      n = latency:percentile(p/100+99)
      io.write(string.format("percentile,%g,%g\n", p/10000+0.99, n/1000000))
   end
   io.write("------------------------------\n")
io.write(string.format("Percentile: 5%%, 10%%, 25%%, 50%%, 75%%, 90%%, 95%%\n"))
io.write(string.format("Latency[msec]: %g, %g, %g, %g, %g, %g, %g\n",
latency:percentile(5)/1000,latency:percentile(10)/1000,latency:percentile(25)/1000,
latency:percentile(50)/1000,
latency:percentile(75)/1000,latency:percentile(90)/1000,latency:percentile(95)/1000))
io.write(string.format("min=%g[msec],median=%g[msec],max=%g[msec]\n", 
latency.min/1000, latency:percentile(50)/1000, latency.max/1000))
end
