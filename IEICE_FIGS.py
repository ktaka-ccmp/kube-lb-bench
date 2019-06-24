#!/usr/bin/env python
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

# ax1.plot(dt1[0], cubic5,  color='c', ls='--', marker='', label='lb x5')
ax1.plot(dt1[0], cubic4,  color='m', ls='-', marker='', label='lb x4')
ax1.plot(dt1[0], cubic3,  color='g', ls='-', marker='', label='lb x3')
ax1.plot(dt1[0], cubic2,  color='b', ls='-', marker='', label='lb x2')
ax1.plot(dt1[0], cubic1,  color='r', ls='-', marker='', label='lb x1')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_ylim(0,800000)

ax1.set_yticks(np.arange(0, 800001, 200000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
ax1.legend(loc=(0.6,0.75), ncol=2)
#plt.title('Load balancer scalability BBR/CUBIC')

plt.savefig('IEICE_FIGS/ecmp_lb_cubic_ieice.png', bbox_inches="tight", dpi=300)
plt.show()


# In[2]:


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
ax1.legend(loc=(0.75,0.85))
ax1.set_xlim(-0,11)
ax1.set_ylabel('Count')
ax1.set_xlabel('Routing update delay on router [sec]')

plt.savefig('IEICE_FIGS/ecmp_delay_histgram_ieice.png', bbox_inches="tight", dpi=300)

plt.show()


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

ax1.legend(loc=(0.75,0.85))
ax2.legend(loc=(0.75,0.9))

#ax1.legend(loc=(0.6,0.75), ncol=2)
#plt.title('Load balancer scalability BBR/CUBIC')

plt.savefig('IEICE_FIGS/ecmp_response_ieice.png', bbox_inches="tight", dpi=300)
plt.show()


# In[7]:


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

ipvs0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
ipvs1 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
iptd0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/iptd1_0.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
iptd1 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/iptd1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

ax1.plot(ipvs0[0], ipvs0[1],  color='r', ls='-', marker='', label='ipvs')
ax1.plot(iptd0[0], iptd0[1],  color='b', ls='-', marker='', label='iptables DNAT')

ax2 = ax1.twinx()
ax2.plot(ipvs0[0], ipvs0[2],  color='m', ls='-', marker='', label='ipvs')
ax2.plot(iptd0[0], iptd0[2],  color='c', ls='-', marker='', label='iptables DNAT')
ax2.plot(ipvs1[0], ipvs1[2],  color='r', ls='-', marker='', label='ipvs')
ax2.plot(iptd1[0], iptd1[2],  color='b', ls='-', marker='', label='iptables DNAT')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_ylim(0,250000)

# ax1.set_yticks(np.arange(0, 200001, 200000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
# ax1.legend(loc=(0.6,0.75), ncol=2)
#plt.title('Load balancer scalability BBR/CUBIC')

# plt.savefig('IEICE_FIGS/ecmp_lb_cubic_ieice.png', bbox_inches="tight", dpi=300)
plt.show()
# ipvs0[2]


# In[4]:


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

ipvs0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
ipvs1 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
iptd0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/iptd1_0.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
iptd1 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/iptd1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

ax1.plot(ipvs1[0], ipvs1[1],  color='r', ls='-', marker='', label='ipvs')
ax1.plot(iptd1[0], iptd1[1],  color='b', ls='-', marker='', label='iptables DNAT')

ax2 = ax1.twinx()
ax2.plot(ipvs1[0], ipvs1[3],  color='r', ls='-', marker='', label='ipvs')
ax2.plot(iptd1[0], iptd1[3],  color='b', ls='-', marker='', label='iptables DNAT')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_ylim(0,250000)

# ax1.set_yticks(np.arange(0, 200001, 200000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx pods')
# ax1.legend(loc=(0.6,0.75), ncol=2)
#plt.title('Load balancer scalability BBR/CUBIC')

# plt.savefig('IEICE_FIGS/ecmp_lb_cubic_ieice.png', bbox_inches="tight", dpi=300)
plt.show()
# ipvs0[2]


# In[43]:


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

ipvs0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
iptd0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/iptd1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

ax1.plot(iptd0[1], iptd0[3],  color='g', ls='-', marker='', label='iptables DNAT')
ax1.plot(ipvs0[1], ipvs0[3],  color='r', ls='-', marker='', label='ipvs')

ax2 = ax1.twinx()
ax2.plot(ipvs0[1], ipvs0[3]/ iptd0[3],  color='c', ls='-', marker='', label='Ratio')
ax2.set_ylim(0,5)

ax1.xaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_xticks(np.arange(0, 200001, 50000))

ax1.set_ylim(0,100)
ax1.set_xlabel('Throughput [req/sec]')
ax1.set_ylabel('CPU usage [%]')
ax1.legend(loc=(0.7,0.7))

#plt.savefig('IEICE_FIGS/cpu_usage.png', bbox_inches="tight", dpi=300)


# In[44]:


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

ipvs0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)
iptd0 = np.loadtxt("KuruwaNew/Try01_cubic/cpuidle_rss_rps_rfs_xps_0_1_1_1/iptd1_1.csv",usecols=(0,1,2,3,4,5,6,7), delimiter=',', unpack=True, skiprows=1)

cond =  iptd0[1]> 1.9e+5
x=np.concatenate((np.extract(~cond, iptd0[1]), np.average(np.extract(cond, iptd0[1]))), axis=None)
y=np.concatenate((np.extract(~cond, iptd0[3]), np.average(np.extract(cond, iptd0[3]))), axis=None)
ipdt0n=np.vstack((x,y))

cond =  ipvs0[1]> 1.9e+5
x=np.concatenate((np.extract(~cond, ipvs0[1]), np.average(np.extract(cond, ipvs0[1]))), axis=None)
y=np.concatenate((np.extract(~cond, ipvs0[3]), np.average(np.extract(cond, ipvs0[3]))), axis=None)
ipvs0n=np.vstack((x,y))

ax1.plot(ipdt0n[0], ipdt0n[1],  color='g', ls='-', marker='', label='iptables DNAT')
ax1.plot(ipvs0n[0], ipvs0n[1],  color='r', ls='-', marker='', label='ipvs')

ax1.xaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_xticks(np.arange(0, 200001, 50000))

ax1.set_ylim(0,100)
ax1.set_xlabel('Throughput [req/sec]')
ax1.set_ylabel('CPU usage [%]')
ax1.legend(loc=(0.7,0.7))

plt.savefig('IEICE_FIGS/cpu_usage.png', bbox_inches="tight", dpi=300)


# In[ ]:




