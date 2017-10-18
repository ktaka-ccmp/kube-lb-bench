
# coding: utf-8

# In[15]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import seaborn as sns
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

#sns.set_style("white")
#sns.set_context("paper")
plt.style.use('seaborn-poster')

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

df1 = np.loadtxt("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='b', label='ipvs')
ax1.plot(*df2, color='r', label='iptables')


ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Request/sec')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('host-gw, rps=on')

df1 = np.loadtxt("24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("27th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax2.plot(*df1, color='b', label='ipvs')
ax2.plot(*df2, color='r', label='iptables')

ax2.set_xticks(np.arange(0, 41, 10))   
ax2.set_xlim(0,41)
ax2.set_ylim(0,200000)
ax2.set_xlabel('Number of pods')
#ax2.set_ylabel('Request/sec')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('host-gw, rss=on')

ax1.legend(loc=4)
ax2.legend(loc=4)

ax1.grid(ls='--', lw='1')
ax2.grid(ls='--', lw='1')

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('33th_try/ipvs_iptabls_2figs.png', bbox_inches="tight", dpi=300)
plt.show()


# In[23]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import seaborn as sns
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

#sns.set_style("white")
#sns.set_context("paper")
plt.style.use('seaborn-poster')

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(6, 6))

ax1 = fig.add_subplot(111)

df1 = np.loadtxt("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='b', label='ipvs')
ax1.plot(*df2, color='r', label='iptables')


ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Request/sec')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('host-gw, rps=on')

ax1.legend(loc=4)

ax1.grid(ls='--', lw='1')

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('33th_try/ipvs_iptabls_rps.png', bbox_inches="tight", dpi=300)
plt.show()


# In[25]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import seaborn as sns
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

#sns.set_style("white")
#sns.set_context("paper")
plt.style.use('seaborn-poster')

get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(6, 6))

ax1 = fig.add_subplot(111)
df1 = np.loadtxt("24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("27th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='b', label='ipvs')
ax1.plot(*df2, color='r', label='iptables')

ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Request/sec')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('host-gw, rss=on')

ax1.legend(loc=4)

ax1.grid(ls='--', lw='1')

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('33th_try/ipvs_iptabls_rss.png', bbox_inches="tight", dpi=300)
plt.show()


# In[ ]:



