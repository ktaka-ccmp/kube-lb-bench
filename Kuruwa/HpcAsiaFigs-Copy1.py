
# coding: utf-8

# In[66]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("paper")

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(5, 12))

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

df1 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/ipvs_cpu08_3.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("24th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax1.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax1.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')


ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('(a) host-gw mode\n',y=-0.3)

df1 = np.loadtxt("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("25th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("25th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax2.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax2.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax2.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')

ax2.set_xticks(np.arange(0, 41, 10))   
ax2.set_xlim(0,41)
ax2.set_ylim(0,200000)
ax2.set_xlabel('Number of pods')
ax2.set_ylabel('Throughput [req/s]')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('(b) vxlan mode\n', y=-0.3)

df1 = np.loadtxt("26th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("26th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("26th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax3.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax3.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax3.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')

ax3.set_xticks(np.arange(0, 41, 10))   
ax3.set_xlim(0,41)
ax3.set_ylim(0,200000)
ax3.set_xlabel('Number of pods')
ax3.set_ylabel('Throughput [req/s]')
ax3.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax3.set_title('(c) udp mode\n', y=-0.3)

ax1.legend(loc=(0.65,0.65))
ax2.legend(loc=(0.65,0.5))
ax3.legend(loc=(0.65,0.6))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('HPCAsiaFigs/ipvs_3figs.png', bbox_inches="tight", dpi=300)


# In[64]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("paper")

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(5, 12))

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

df1 = np.loadtxt("27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("27th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("27th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax1.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax1.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')

ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('(a) host-gw mode\n',y=-0.3)

df1 = np.loadtxt("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("25th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("25th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax2.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax2.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax2.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')


ax2.set_xticks(np.arange(0, 41, 10))   
ax2.set_xlim(0,41)
ax2.set_ylim(0,200000)
ax2.set_xlabel('Number of pods')
ax2.set_ylabel('Throughput [req/s]')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('(b) vxlan mode\n', y=-0.3)

df1 = np.loadtxt("26th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("26th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("26th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax3.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax3.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax3.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')

ax3.set_xticks(np.arange(0, 41, 10))   
ax3.set_xlim(0,41)
ax3.set_ylim(0,200000)
ax3.set_xlabel('Number of pods')
ax3.set_ylabel('Throughput [req/s]')
ax3.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax3.set_title('(c) udp mode\n', y=-0.3)

ax1.legend(loc=(0.65,0.6))
ax2.legend(loc=(0.65,0.5))
ax3.legend(loc=(0.65,0.6))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('HPCAsiaFigs/iptables_3figs.png', bbox_inches="tight", dpi=300)


# In[60]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("paper")

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(5, 7))

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

df1 = np.loadtxt("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("29th_try/rss_rps_rfs_0_1_0/nginx_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='IPVS')
ax1.plot(*df2, color='g', label='iptables DNAT')
ax1.plot(*df3, color='b', label='Nginx')

ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('(a) host-gw mode\n',y=-0.3)

df1 = np.loadtxt("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("28th_try/rss_rps_rfs_0_1_0/nginx_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax2.plot(*df1, color='r', label='IPVS')
ax2.plot(*df2, color='g', label='iptables DNAT')
ax2.plot(*df3, color='b', label='Nginx')

ax2.set_xticks(np.arange(0, 41, 10))   
ax2.set_xlim(0,41)
ax2.set_ylim(0,200000)
ax2.set_xlabel('Number of pods')
ax2.set_ylabel('Throughput [req/s]')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('(b) vxlan mode\n', y=-0.3)

ax1.legend(loc=(0.72,0.7))
ax2.legend(loc=(0.72,0.55))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('HPCAsiaFigs/ipvs-iptables-nginx_2figs.png', bbox_inches="tight", dpi=300)


# In[73]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
sns.set_style("white")
sns.set_context("paper")

from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

x=np.arange(0, 1600, 100)

dt0 = np.loadtxt("31th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_pod40.csv",usecols=(0, 1, 2), delimiter=',', unpack=True, skiprows=1)

ax1.plot(dt0[0],dt0[1], color='b', label='Experiment', ls='',lw='1',marker='.')
ax1.plot(x, 1000000000/(x+622.72)/8, label='1Gbps limit', color='r',ls='-',lw='1')
ax1.set_ylabel('Throughput [req/s]')
plt.legend(loc=1, bbox_to_anchor=(0.97, 0.95))

ax1.set_xlabel('HTTP response body data size [byte]')
ax1.set_xlim(0,1500)
ax1.set_ylim(0,200000)
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#plt.title('Experimental cond.: ipvs, flannel:host-gw mode,\n 40 pods, rps=on, rss=off', x=0.5, y=0.03)
ax1.text(0.65,0.04,'Experimental condtions:\nIPVS, host-gw, 40 pods, \nrps=on, rss=off',transform=ax1.transAxes)
plt.savefig('HPCAsiaFigs/performance_limitation.png', bbox_inches="tight", dpi=300)
plt.show()


# In[ ]:




# In[81]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
sns.set_style("white")
sns.set_context("paper")

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

dt = np.loadtxt("33th_try/rss_rps_rfs_0_1_0/latency_ipvs_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='160k[rec/s] load, IPVS')
dt = np.loadtxt("33th_try/rss_rps_rfs_0_1_0/latency_ipvs_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='180k[rec/s] load, IPVS')
dt = np.loadtxt("33th_try/rss_rps_rfs_0_1_0/latency_proxy_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='r', ls='--',lw='1.5',marker='', label='160k[rec/s] load, iptables DNAT')
dt = np.loadtxt("33th_try/rss_rps_rfs_0_1_0/latency_proxy_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='b', ls='--',lw='1.5',marker='', label='180k[rec/s] load, iptables DNAT')

ax1.legend(loc=4, bbox_to_anchor=(0.99, 0.65))

#ax1.set_title('Latency CDF for 40 pods flannel:host-gw,  rps=on, rss=off')

ax1.set_ylabel('Percentile')
ax1.set_xlabel('Latency [sec]')
ax1.set_xlim(0,0.004001)
ax1.set_xticks(np.arange(0,0.004001,0.001)) 
ax1.set_yticks(np.arange(0,1.01,0.25)) 

ax1.grid(ls='--', lw='0.5')
ax1.grid(ls='--', lw='0.5')

ax1.text(0.55,0.04,'Experimental condtions:\n40 pods, host-gw, rps=on, rss=off',transform=ax1.transAxes)
plt.savefig('HPCAsiaFigs/latency_cdf_rps_40pods.png', bbox_inches="tight", dpi=300)
plt.show()


# In[ ]:



