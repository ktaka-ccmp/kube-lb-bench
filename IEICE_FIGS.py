
# coding: utf-8

# In[9]:

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
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of nginx pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
#ax1.set_title('host-gw mode\n',y=-0.2)

ax1.legend(loc=(0.70,0.7))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('IEICE_FIGS/ipvs-iptables-nginx.png', bbox_inches="tight", dpi=300)


# In[11]:

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
ax.legend(loc=(0.55,0.1))

#plt.title('Ipvs Loadbalancer Performance on GCP\n')

plt.savefig('IEICE_FIGS/gcp_all_ieice.png', dpi=300)


# In[12]:

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
ax.legend(loc=(0.6,0.1))

#plt.title('Ipvs Loadbalancer Performance on AWS\n')
plt.savefig('IEICE_FIGS/aws_c4_ieice.png', dpi=300)


# In[ ]:



