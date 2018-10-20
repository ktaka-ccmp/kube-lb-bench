
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


# In[ ]:



