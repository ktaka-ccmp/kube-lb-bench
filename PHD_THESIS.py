#!/usr/bin/env python
# coding: utf-8

# In[76]:


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

fig = plt.figure(figsize=(6, 4))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("Kuruwa/24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("Kuruwa/24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("Kuruwa/24th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax1.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax1.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')


ax1.set_xticks(np.arange(0, 41, 10))  
ax1.set_yticks(np.arange(0, 200001, 20000))
ax1.set_xlim(0,41)
# ax1.set_ylim(0,220000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/sec]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.legend(frameon=False,loc=(0.65,0.65))
# ax1.text(0.45,0.04,'Experimental condtions:\n host-gw, (rss,rps)=(off,on)',transform=ax1.transAxes)
ax1.text(0.6,0.04,'flannel backend: host-gw',transform=ax1.transAxes)

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('PHD_THESIS_FIGS/ipvs_mcore_proccessing.png', bbox_inches="tight", dpi=600)


# In[4]:


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

fig = plt.figure(figsize=(6, 4))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("Kuruwa/27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("Kuruwa/27th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("Kuruwa/27th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax1.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax1.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')


ax1.set_xticks(np.arange(0, 41, 10))  
ax1.set_yticks(np.arange(0, 200001, 20000))
ax1.set_xlim(0,41)
# ax1.set_ylim(0,220000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/sec]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.legend(frameon=False,loc=(0.65,0.65))
# ax1.text(0.45,0.04,'Experimental condtions:\n host-gw, (rss,rps)=(off,on)',transform=ax1.transAxes)
ax1.text(0.6,0.04,'flannel backend: host-gw',transform=ax1.transAxes)

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('PHD_THESIS_FIGS/iptables_mcore_proccessing.png', bbox_inches="tight", dpi=600)


# In[80]:


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

fig = plt.figure(figsize=(6, 4))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("Kuruwa/24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("Kuruwa/25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("Kuruwa/26th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='host-gw')
ax1.plot(*df2, color='g', label='vxlan tunnel')
ax1.plot(*df3, color='b', label='udp tunnel')

ax1.set_xticks(np.arange(0, 41, 10))
ax1.set_yticks(np.arange(0, 200001, 20000))
ax1.set_xlim(0,41)
# ax1.set_ylim(0,220000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/sec]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#ax1.set_title('(a) host-gw mode\n',y=-0.3)

ax1.legend(frameon=False,loc=(0.7,0.5))
ax1.text(0.45,0.04,'Multicore settings: (rss,rps)=(off,on)',transform=ax1.transAxes)

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('PHD_THESIS_FIGS/ipvs_flannel_mode.png', bbox_inches="tight", dpi=600)


# In[1]:


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

fig = plt.figure(figsize=(6, 4))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("Kuruwa/27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("Kuruwa/25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("Kuruwa/26th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='host-gw')
ax1.plot(*df2, color='g', label='vxlan tunnel')
ax1.plot(*df3, color='b', label='udp tunnel')

ax1.set_xticks(np.arange(0, 41, 10))
ax1.set_yticks(np.arange(0, 200001, 20000))
ax1.set_xlim(0,41)
# ax1.set_ylim(0,220000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/sec]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#ax1.set_title('(a) host-gw mode\n',y=-0.3)

ax1.legend(frameon=False,loc=(0.7,0.5))
ax1.text(0.45,0.04,'Multicore settings: (rss,rps)=(off,on)',transform=ax1.transAxes)

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('PHD_THESIS_FIGS/iptables_flannel_mode.png', bbox_inches="tight", dpi=600)


# In[79]:


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

fig = plt.figure(figsize=(6, 4))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("Kuruwa/24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("Kuruwa/27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("Kuruwa/29th_try/rss_rps_rfs_0_1_0/nginx_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='ipvs')
ax1.plot(*df2, color='g', label='iptables DNAT')
ax1.plot(*df3, color='b', label='nginx')
ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_yticks(np.arange(0, 200001, 20000))
ax1.set_xlim(0,41)
# ax1.set_ylim(0,220000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/sec]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#ax1.set_title('host-gw mode\n',y=-0.2)

ax1.text(0.45,0.14,'Experimental condtions\n    flannel backend: host-gw \n    Muticore settings: (rss,rps)=(off,on)',transform=ax1.transAxes)

ax1.legend(frameon=False,loc=(0.70,0.65))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('PHD_THESIS_FIGS/ipvs-iptables-nginx.png', bbox_inches="tight", dpi=600)


# In[70]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
sns.set_style("white")
sns.set_context("paper")

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

dt = np.loadtxt("Kuruwa/33th_try/rss_rps_rfs_0_1_0/latency_ipvs_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='160k[rec/sec], ipvs')
dt = np.loadtxt("Kuruwa/33th_try/rss_rps_rfs_0_1_0/latency_ipvs_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='180k[rec/sec], ipvs')
dt = np.loadtxt("Kuruwa/33th_try/rss_rps_rfs_0_1_0/latency_proxy_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='r', ls='--',lw='1.5',marker='', label='160k[rec/sec], iptables DNAT')
dt = np.loadtxt("Kuruwa/33th_try/rss_rps_rfs_0_1_0/latency_proxy_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt[1], dt[0], color='b', ls='--',lw='1.5',marker='', label='180k[rec/sec], iptables DNAT')

# ax1.legend(frameon=False,loc=4, bbox_to_anchor=(0.99, 0.65))
ax1.legend(frameon=False,loc=(0.5,0.5))

#ax1.set_title('Latency CDF for 40 pods flannel:host-gw,  rps=on, rss=off')

ax1.set_ylabel('Percentile')
ax1.set_xlabel('Latency [sec]')
ax1.set_xlim(0,0.004001)
ax1.set_xticks(np.arange(0,0.004001,0.001)) 
ax1.set_yticks(np.arange(0,1.01,0.25)) 

ax1.grid(ls='--', lw='0.5')
ax1.grid(ls='--', lw='0.5')

ax1.text(0.45,0.04,'Experimental condtions:\n40 pods, host-gw, rps=on, rss=off',transform=ax1.transAxes)
plt.savefig('PHD_THESIS_FIGS/latency_cdf_rps_40pods.png', bbox_inches="tight", dpi=600)
plt.show()


# In[71]:


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
ax = fig.add_subplot(111)

dt1 = np.loadtxt("GCP/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt2 = np.loadtxt("GCP/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt3 = np.loadtxt("GCP/5th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt4 = np.loadtxt("GCP/6th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

#ax.plot(*dt4, color='c', label='64 cpu,rps')
ax.plot(*dt3, color='g', label='gcp, custom instance, 32 cpu')
ax.plot(*dt2, color='r', label='gcp, custom instance, 16 cpu')
ax.plot(*dt1, color='b', label='gcp, custom instance, 8 cpu')

ax.set_xlim(0,41)
ax.set_ylim(0,180000)
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax.set_xlabel('Number of nginx pods')
ax.set_ylabel('Throughput [req/sec]')
ax.legend(frameon=False,loc=(0.5,0.1))

#plt.title('Ipvs Loadbalancer Performance on GCP\n')

plt.savefig('PHD_THESIS_FIGS/gcp_all_tp.png', dpi=600)


# In[72]:


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
ax = fig.add_subplot(111)

dt1 = np.loadtxt("AWS/9th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt2 = np.loadtxt("AWS/8th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt3 = np.loadtxt("AWS/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax.plot(*dt3, color='g', label='aws, c4.8xlarge, 32cpu')
ax.plot(*dt2, color='r', label='aws, c4.4xlarge, 16cpu')
ax.plot(*dt1, color='b', label='aws, c4.2xlarge, 8cpu')

ax.set_xlim(0,41)
ax.set_ylim(0,120000)
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax.set_xlabel('Number of nginx pods')
ax.set_ylabel('Throughput [req/sec]')
ax.legend(frameon=False,loc=(0.6,0.1))

#plt.title('Ipvs Loadbalancer Performance on AWS\n')
plt.savefig('PHD_THESIS_FIGS/aws_c4_tp.png', dpi=600)


# In[63]:


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

d0 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb10g = dt ; mcb10g = m

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb1=dt; mcb1=m


d0 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb10gdnat = dt ; mcb10gdnat = m

ax1.plot(cb10gdnat[0], mcb10gdnat,  color='g', ls='-', marker='', label='iptables DNAT 10Gbps')
# ax1.plot(cb10gdnat[0], cb10gdnat[1::1].T,  color='g', ls='', marker='.')

ax1.plot(cb10g[0], mcb10g ,  color='r', ls='-', marker='', label='ipvs 10Gbps')
#ax1.plot(cb10g[0], cb10g[1::1].T,  color='r', ls='', marker='.')

ax1.plot(cb1[0], mcb1,  color='b', ls='-', marker='', label='ipvs 1Gbps')
#ax1.plot(cb1[0], cb1[1::1].T,  color='b', ls='', marker='.')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_xlim(0,60)
ax1.set_yticks(np.arange(0, 900001, 100000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
ax1.legend(frameon=False,loc=(0.6,0.65))

plt.savefig('PHD_THESIS_FIGS/ipvs_iptables_dnat_10g.png', bbox_inches="tight", dpi=600)


# In[3]:


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

fig = plt.figure(figsize=(6, 4))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("Kuruwa/24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("Kuruwa/27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("Kuruwa/29th_try/rss_rps_rfs_0_1_0/nginx_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='ipvs')
ax1.plot(*df2, color='g', label='iptables DNAT')
ax1.plot(*df3, color='b', label='nginx')

ax1.plot(cb1[0], mcb1,  color='b', ls='-', marker='', label='node with 1G nic(tg3)')

ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,220000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#ax1.set_title('host-gw mode\n',y=-0.2)

ax1.legend(loc=(0.70,0.65))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.show()


# In[64]:


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

dt0 = np.loadtxt("Kuruwa/31th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_pod40.csv",usecols=(0, 1, 2), delimiter=',', unpack=True, skiprows=1)

ax1.plot(dt0[0],dt0[1], color='b', label='Experiment', ls='',lw='1',marker='.')
ax1.plot(x, 1000000000/(x+665.36)/8, label='1Gbps limit', color='r',ls='-',lw='1')
ax1.set_ylabel('Throughput [req/sec]')
plt.legend(frameon=False,loc=1, bbox_to_anchor=(0.97, 0.95))

ax1.set_xlabel('HTTP response body data size [byte]')
ax1.set_xlim(0,1500)
ax1.set_ylim(0,200000)
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#plt.title('Experimental cond.: ipvs, flannel:host-gw mode,\n 40 pods, rps=on, rss=off', x=0.5, y=0.03)
ax1.text(0.65,0.04,'Experimental condtions:\nipvs, host-gw, 40 pods, \nrps=on, rss=off',transform=ax1.transAxes)
plt.savefig('PHD_THESIS_FIGS/tp_limit_1gbps.png', bbox_inches="tight", dpi=600)
plt.show()


# In[65]:


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

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt1=dt; m1=m

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt2=dt; m2=m

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt3=dt; m3=m

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
#dt=np.delete(np.concatenate((d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16],0)
m=np.mean(dt[1::1], axis=0)

dt4=dt; m4=m

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs5_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt5=dt; m5=m

cubic1=m1
cubic2=m2
cubic3=m3
cubic4=m4
cubic5=m5

fig = plt.figure(figsize=(6, 4))
#fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)

#ax1.plot(dt1[0], cubic5,  color='c', ls='--', marker='', label='lb x5')
ax1.plot(dt1[0], cubic4,  color='m', ls='-', marker='', label='lb x4')
ax1.plot(dt1[0], cubic3,  color='g', ls='-', marker='', label='lb x3')
ax1.plot(dt1[0], cubic2,  color='b', ls='-', marker='', label='lb x2')
ax1.plot(dt1[0], cubic1,  color='r', ls='-', marker='', label='lb x1')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_ylim(0,800000)

ax1.set_yticks(np.arange(0, 800001, 200000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
ax1.legend(frameon=False,loc=(0.6,0.80), ncol=2)
#plt.title('Load balancer scalability BBR/CUBIC')

plt.savefig('PHD_THESIS_FIGS/ecmp_lb_cubic.png', bbox_inches="tight", dpi=600)
#plt.show()


# In[66]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
sns.set_style("white")
sns.set_context("paper")

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)


from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
ax1.xaxis.set_major_locator(MultipleLocator(1))
ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.tick_params(which='major', direction='in', length=5, width='1',top='off')
#ax1.tick_params(which='minor', direction='in', length=5, width='1',top='off')

#d3 = np.loadtxt("Try01_cubic/response_0844/lbnum2.csv",usecols=(0,3), delimiter=',', unpack=True, skiprows=0)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/response_1836/lbnum2.csv",usecols=(0,3), delimiter=',', unpack=True, skiprows=0)

ax1.hist(d3[1], bins=10, range=(0, 10), label='delay count')
ax1.legend(frameon=False,loc=(0.75,0.85))
ax1.set_xlim(-0,11)
ax1.set_ylabel('Count')
ax1.set_xlabel('Routing update delay on router [sec]')

plt.savefig('PHD_THESIS_FIGS/ecmp_delay_histgram.png', bbox_inches="tight", dpi=600)


# In[67]:


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

d0 = np.loadtxt("KuruwaNew/Try01_cubic/response_0844/lbnum.csv",usecols=(0,1,2), delimiter=',', unpack=True, skiprows=0)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/response_0844/rps.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=0)


fig = plt.figure(figsize=(6, 4))
#fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)

ax1.plot(d0[0]-d0[0][0], d0[1],  color='r', ls='-', marker='', label='#ipvs pods')
ax1.set_xlim(60,1860)
#ax1.plot((d0[0]-1540511067)/60, d0[1],  color='r', ls='-', marker='', label='#ipvs pods')
#ax1.set_xlim(1,31)
ax1.set_ylim(0,20)
#ax1.set_yticks(np.arange(0, 10.1, 1))
ax1.set_ylabel('Number of ipvs pods')
ax1.set_xlabel('Time [sec]')

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
ax1.xaxis.set_minor_locator(MultipleLocator(60))
ax1.xaxis.set_major_locator(MultipleLocator(300))
#ax1.xaxis.set_minor_locator(MultipleLocator(1))
#ax1.xaxis.set_major_locator(MultipleLocator(5))
ax1.tick_params(which='minor', direction='in', length=5, width='1',top='off')
ax1.tick_params(which='major', direction='in', length=5, width='2',top='off')

ax2 = ax1.twinx()
ax2.plot(d1[0]-d0[0][0], d1[1],  color='b', ls='-', marker='', label='Throughput')
ax2.set_xlim(60,1860)
#ax2.plot((d1[0]-1540511067)/60, d1[1],  color='b', ls='-', marker='', label='Throughput')
#ax2.set_xlim(1,31)
ax2.set_ylim(0,1000000)
ax2.set_yticks(np.arange(0, 1000001, 200000))
ax2.set_ylabel('Throughput [req/sec]')

ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.legend(frameon=False,loc=(0.75,0.85))
ax2.legend(frameon=False,loc=(0.75,0.9))

#ax1.legend(loc=(0.6,0.75), ncol=2)
#plt.title('Load balancer scalability BBR/CUBIC')

plt.savefig('PHD_THESIS_FIGS/ecmp_response.png', bbox_inches="tight", dpi=600)
plt.show()


# In[1]:


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

d0 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic_iptablesdnat/rss_rps_rfs_xps_0_1_1_1/iptdnat_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb1gdnat=dt; mcb1gdnat=m

d0 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic_lvstun_1g/rss_rps_rfs_xps_0_1_1_1/ipvs1_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb1gtun=dt; mcb1gtun=m

d0 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb1=dt; mcb1=m

ax1.plot(cb1gtun[0], mcb1gtun,  color='r', ls='-', marker='', label='ipvs tun')
# ax1.plot(cb1gtun[0], cb1gtun[1::1].T,  color='b', ls='', marker='.')

ax1.plot(cb1[0], mcb1,  color='b', ls='-', marker='', label='ipvs nat')
# ax1.plot(cb1[0], cb1[1::1].T,  color='r', ls='', marker='.')

ax1.plot(cb1gdnat[0], mcb1gdnat,  color='g', ls='-', marker='', label='iptables DNAT')
# ax1.plot(cb1gdnat[0], cb1gdnat[1::1].T,  color='g', ls='', marker='.')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_xlim(0,60)
ax1.set_yticks(np.arange(0, 400001, 100000))
ax1.set_ylim(0,400000)
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
ax1.legend(frameon=False,loc=(0.7,0.15))

# plt.show()
plt.savefig('PHD_THESIS_FIGS/ipvs_l3dsr_1g.png', bbox_inches="tight", dpi=600)


# In[46]:


mcb1[20],mcb1gtun[20],mcb1gdnat[20]


# In[2]:


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
# fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(111)

d0 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb10gdnat = dt ; mcb10gdnat = m

d0 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic_lvstun/rss_rps_rfs_xps_1_0_0_0/ipvs1_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb10gtun = dt ; mcb10gtun = m

d0 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb10g = dt ; mcb10g = m

ax1.plot(cb10gdnat[0], mcb10gdnat ,  color='g', ls='-', marker='', label='iptabls DNAT')
# ax1.plot(cb10gdnat[0], cb10gdnat[1::1].T,  color='g', ls='', marker='.')

ax1.plot(cb10gtun[0], mcb10gtun ,  color='r', ls='-', marker='', label='ipvs tun')
# ax1.plot(cb10gtun[0], cb10gtun[1::1].T,  color='b', ls='', marker='.')

ax1.plot(cb10g[0], mcb10g ,  color='b', ls='-', marker='', label='ipvs nat')
# ax1.plot(cb10g[0], cb10g[1::1].T,  color='r', ls='', marker='.')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_xlim(0,60)
ax1.set_yticks(np.arange(0, 900001, 100000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
ax1.legend(frameon=False,loc=(0.7,0.55))

# plt.show()
plt.savefig('PHD_THESIS_FIGS/ipvs_l3dsr_10g.png', bbox_inches="tight", dpi=600)


# In[41]:


mcb10g[20],mcb10gtun[20],mcb10gdnat[20]


# In[31]:


mcb10gdnat


# In[32]:


mcb10gtun


# In[11]:


mcb10g


# In[3]:


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

# fig = plt.figure(figsize=(12, 8))
fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

d0 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic_iptablesdnat/rss_rps_rfs_xps_1_0_0_0/iptdnat_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

cb10gdnat = dt ; mcb10gdnat = m

d0 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_tun_1_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)


dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
# dt=np.delete(np.concatenate((d0, d1), axis=0), [2],0)
m=np.mean(dt[1::1], axis=0)

cb10gtun = dt ; mcb10gtun = m

d0 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_6.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_7.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_8.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("KuruwaNew/Try02_cubic_lvs_on_node/rss_rps_rfs_xps_1_0_0_0/ipvs_nat_1_9.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)


dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
# dt=np.delete(np.concatenate((d0, d1), axis=0), [2],0)
m=np.mean(dt[1::1], axis=0)

cb10g = dt ; mcb10g = m

ax1.plot(cb10gdnat[0], mcb10gdnat ,  color='g', ls='-', marker='', label='iptabls DNAT')
# ax1.plot(cb10gdnat[0], cb10gdnat[1::1].T,  color='g', ls='', marker='.')

ax1.plot(cb10gtun[0], mcb10gtun ,  color='r', ls='-', marker='', label='ipvs tun')
# ax1.plot(cb10gtun[0], cb10gtun[1::1].T,  color='b', ls='', marker='.')

ax1.plot(cb10g[0], mcb10g ,  color='b', ls='-', marker='', label='ipvs nat')
# ax1.plot(cb10g[0], cb10g[1::1].T,  color='r', ls='', marker='.')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_xlim(0,60)
ax1.set_yticks(np.arange(0, 900001, 100000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
ax1.legend(frameon=False,loc=(0.7,0.55))

# plt.show()
plt.savefig('PHD_THESIS_FIGS/ipvs_node_l3dsr_10g.png', bbox_inches="tight", dpi=600)


# In[44]:


mcb10g[20],mcb10gtun[20],mcb10gdnat[20]


# In[7]:


mcb10gdnat


# In[8]:


mcb10gtun


# In[3]:


mcb10g


# In[ ]:




