
# coding: utf-8

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

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)
cubic10 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
cubic20 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
cubic30 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
cubic40 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

bbr10 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
bbr20 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
bbr30 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
bbr40 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*cubic10, color='r')
ax1.plot(*cubic20, color='r')
ax1.plot(*cubic30, color='r')
ax1.plot(*cubic40, color='r')

ax1.plot(*bbr10, color='b')
ax1.plot(*bbr20, color='b')
ax1.plot(*bbr30, color='b')
ax1.plot(*bbr40, color='b')

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

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)

cubic10 = np.loadtxt("Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
bbr10 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*cubic10, color='r')
ax1.plot(*bbr10, color='b')

plt.show()


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

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)

cubic10 = np.loadtxt("Try03_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
bbr10 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*cubic10, color='r')
ax1.plot(*bbr10, color='b')

plt.show()


# In[180]:

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

d0 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt1=dt; m1=m

d0 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt2=dt; m2=m

d0 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
m=np.mean(dt[1::1], axis=0)

dt3=dt; m3=m

#d0 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_0.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d1 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_1.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d2 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_2.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d3 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_3.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d4 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_4.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d5 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_5.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d6 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_6.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d7 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_7.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d8 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_8.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)
d9 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_9.csv",usecols=(0,1), delimiter=',', unpack=True, skiprows=1)

#dt=np.delete(np.concatenate((d0, d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16,18],0)
dt=np.delete(np.concatenate((d1, d2, d3, d4, d5, d6, d7, d8, d9), axis=0), [2,4,6,8,10,12,14,16],0)
m=np.mean(dt[1::1], axis=0)

dt4=dt; m4=m

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

ax1.plot(dt1[0], m1,  color='r', ls='-', marker='', label='#lb = 1')
ax1.plot(dt1[0], dt1[1::1].T,  color='r', ls='', marker='.')

ax1.plot(dt2[0], m2,  color='b', ls='-', marker='', label='#lb = 2')
ax1.plot(dt2[0], dt2[1::1].T,  color='b', ls='', marker='.')

ax1.plot(dt3[0], m3,  color='g', ls='-', marker='', label='#lb = 3')
ax1.plot(dt3[0], dt3[1::1].T,  color='g', ls='', marker='.')

ax1.plot(dt4[0], m4,  color='c', ls='-', marker='', label='#lb = 4')
ax1.plot(dt4[0], dt4[1::1].T,  color='c', ls='', marker='.')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_yticks(np.arange(0, 1000001, 200000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx worker containers(#pods)')
ax1.legend()
plt.title('Load balancer scalability')

plt.savefig('IEICE_Figs/ecmp_lb.png', bbox_inches="tight", dpi=300)
plt.show()


# In[184]:

max= [np.mean(m1[6::1]), np.mean(m2[10::1]), np.mean(m3[16::1]), np.mean(m4[21::1])]

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

ax1.bar([1,2,3,4], max, 0.6, align='center')
ax1.set_xticks([1,2,3,4])
ax1.set_yticks(np.arange(0, 800001, 200000))
ax1.set_ylabel('Max. throughput [req/sec]')
ax1.set_xlabel('Number of load balancers')
plt.title('Load balancer scalability')
ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

plt.savefig('IEICE_Figs/ecmp_lb_plateau.png', bbox_inches="tight", dpi=300)
#plt.show()


# In[191]:

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)

cubic10 = np.loadtxt("Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*cubic10, color='r', label='node with 10G nic(ixgbe)')

ax1.plot(dt1[0], m1,  color='b', ls='-', marker='', label='node with 1G nic(tg3)')
ax1.plot(dt1[0], dt1[1::1].T,  color='b', ls='', marker='.')

ax1.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax1.set_yticks(np.arange(0, 400001, 100000))
ax1.set_ylabel('Throughput [req/sec]')
ax1.set_xlabel('Number of nginx worker containers(#pods)')
ax1.legend()
plt.title('Load balancer throughput \w 10Gbps NIC')

plt.savefig('IEICE_Figs/10G_ipvs.png', bbox_inches="tight", dpi=300)


# In[ ]:



