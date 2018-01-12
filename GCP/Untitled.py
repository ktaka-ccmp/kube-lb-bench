
# coding: utf-8

# In[29]:

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
#sns.set_context("paper")
sns.set_context("talk")

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(6, 5))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/ipvs_cpu08_3.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/proxy_cpu08_3.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/kt-v101_cpu08_3.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='ipvs')
ax1.plot(*df2, color='g', label='gcplb+iptables')
ax1.plot(*df3, color='b', label='gcplb+iptables single')


ax1.set_xticks(np.arange(0, 51, 10))   
ax1.set_xlim(0,51)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('8cpu x 4node')

ax1.grid(ls='--', lw='0.5')
ax1.grid(ls='--', lw='0.5')

ax1.legend(loc=(0.5,0.2))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('8cpux4node.png', bbox_inches="tight", dpi=100)
plt.show()


# In[28]:

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
#sns.set_context("paper")
sns.set_context("talk")

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(6, 5))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_3.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/proxy_cpu16_3.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("9th_try/rss_rps_rfs_0_1_0/kt-v101_cpu16_3.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='ipvs')
ax1.plot(*df2, color='g', label='gcplb+iptables')
ax1.plot(*df3, color='b', label='gcplb+iptables single')


ax1.set_xticks(np.arange(0, 51, 10))   
ax1.set_xlim(0,51)
ax1.set_ylim(0,260000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Throughput [req/s]')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('16cpu x 4node')

ax1.grid(ls='--', lw='0.5')
ax1.grid(ls='--', lw='0.5')

ax1.legend(loc=(0.5,0.15))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('16cpux4node.png', bbox_inches="tight", dpi=100)
plt.show()


# In[ ]:



