
# coding: utf-8

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

fig = plt.figure(figsize=(5, 12))

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

df1 = np.loadtxt("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("24th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax1.plot(*df1, color='r', label='(RSS,RPS)=(off,on)')
ax1.plot(*df2, color='g', label='(RSS,RPS)=(on,off)')
ax1.plot(*df3, color='b', label='(RSS,RPS)=(off,off)')


ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Request/sec')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('(a) host-gw\n',y=-0.3)

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
ax2.set_ylabel('Request/sec')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('(b) vxlan\n', y=-0.3)

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
ax3.set_ylabel('Request/sec')
ax3.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax3.set_title('(c) udp\n', y=-0.3)

ax1.legend(loc=(0.55,0.65))
ax2.legend(loc=(0.55,0.5))
ax3.legend(loc=(0.55,0.5))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('HPCAsiaFigs/ipvs_3figs.png', bbox_inches="tight", dpi=300)


# In[2]:

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
ax1.set_ylabel('Request/sec')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('(a) host-gw\n',y=-0.3)

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
ax2.set_ylabel('Request/sec')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('(b) vxlan\n', y=-0.3)

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
ax3.set_ylabel('Request/sec')
ax3.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax3.set_title('(c) udp\n', y=-0.3)

ax1.legend(loc=(0.55,0.5))
ax2.legend(loc=(0.55,0.5))
ax3.legend(loc=(0.55,0.5))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('HPCAsiaFigs/iptables_3figs.png', bbox_inches="tight", dpi=300)


# In[343]:

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
ax1.plot(*df1, color='r', label='ipvs')
ax1.plot(*df2, color='g', label='iptables')
ax1.plot(*df3, color='b', label='nginx')

ax1.set_xticks(np.arange(0, 41, 10))   
ax1.set_xlim(0,41)
ax1.set_ylim(0,200000)
ax1.set_xlabel('Number of pods')
ax1.set_ylabel('Request/sec')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax1.set_title('(a) host-gw\n',y=-0.3)

df1 = np.loadtxt("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df2 = np.loadtxt("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
df3 = np.loadtxt("28th_try/rss_rps_rfs_0_1_0/nginx_cpu16_0.csv", delimiter=',', unpack=True, skiprows=1)
ax2.plot(*df1, color='r', label='ipvs')
ax2.plot(*df2, color='g', label='iptables')
ax2.plot(*df3, color='b', label='nginx')

ax2.set_xticks(np.arange(0, 41, 10))   
ax2.set_xlim(0,41)
ax2.set_ylim(0,200000)
ax2.set_xlabel('Number of pods')
ax2.set_ylabel('Request/sec')
ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))
ax2.set_title('(b) vxlan\n', y=-0.3)

ax1.legend(loc=(0.75,0.6))
ax2.legend(loc=(0.75,0.5))

fig.tight_layout()  # タイトルとラベルが被るのを解消
plt.savefig('HPCAsiaFigs/ipvs-iptables-nginx_2figs.png', bbox_inches="tight", dpi=300)


# In[ ]:



