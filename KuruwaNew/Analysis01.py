
# coding: utf-8

# In[45]:

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
dt10 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt20 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt21 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs2_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt22 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs2_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt23 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs2_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt24 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs2_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs2_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt30 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt31 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt32 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt33 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt34 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt35 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt40 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt41 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs4_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt42 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs4_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt43 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs4_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt44 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs4_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt45 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs4_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10)
ax1.plot(*dt11)
ax1.plot(*dt12)
ax1.plot(*dt13)
ax1.plot(*dt14)
ax1.plot(*dt15)

ax1.plot(*dt20)
ax1.plot(*dt21)
ax1.plot(*dt22)
ax1.plot(*dt23)
ax1.plot(*dt24)
ax1.plot(*dt25)

ax1.plot(*dt30)
ax1.plot(*dt31)
ax1.plot(*dt32)
ax1.plot(*dt33)
ax1.plot(*dt34)
ax1.plot(*dt35)

ax1.plot(*dt40)
ax1.plot(*dt41)
ax1.plot(*dt42)
ax1.plot(*dt43)
ax1.plot(*dt44)
ax1.plot(*dt45)

plt.show()


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

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)
dt10 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10)
ax1.plot(*dt11)
ax1.plot(*dt12)
ax1.plot(*dt13)
ax1.plot(*dt14)
ax1.plot(*dt15)

plt.show()


# In[37]:

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
dt10 = np.loadtxt("Try03/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try03/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try03/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try03/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try03/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try03/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt20 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt21 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt22 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt23 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt24 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("Try03_2/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10)
ax1.plot(*dt11)
ax1.plot(*dt12)
ax1.plot(*dt13)
ax1.plot(*dt14)
ax1.plot(*dt15)

ax1.plot(*dt20)
ax1.plot(*dt21)
ax1.plot(*dt22)
ax1.plot(*dt23)
ax1.plot(*dt24)
ax1.plot(*dt25)

plt.show()


# In[36]:

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
dt10 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt20 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt21 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt22 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt23 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt24 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("Try03_4/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10)
ax1.plot(*dt11)
ax1.plot(*dt12)
ax1.plot(*dt13)
ax1.plot(*dt14)
ax1.plot(*dt15)

ax1.plot(*dt20)
ax1.plot(*dt21)
ax1.plot(*dt22)
ax1.plot(*dt23)
ax1.plot(*dt24)
ax1.plot(*dt25)

plt.show()


# In[41]:

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
dt10 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt20 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt21 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt22 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt23 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt24 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs2_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt30 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt31 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt32 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt33 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt34 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt35 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs3_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt40 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt41 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt42 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt43 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt44 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt45 = np.loadtxt("Try01_bbr/rss_rps_rfs_xps_0_1_1_1/ipvs4_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)


dt50 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt51 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt52 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt53 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt54 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt55 = np.loadtxt("Try01/rss_rps_rfs_xps_0_1_0_0/ipvs3_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10)
ax1.plot(*dt11)
ax1.plot(*dt12)
ax1.plot(*dt13)
ax1.plot(*dt14)
ax1.plot(*dt15)

ax1.plot(*dt20)
ax1.plot(*dt21)
ax1.plot(*dt22)
ax1.plot(*dt23)
ax1.plot(*dt24)
ax1.plot(*dt25)

ax1.plot(*dt30)
ax1.plot(*dt31)
ax1.plot(*dt32)
ax1.plot(*dt33)
ax1.plot(*dt34)
ax1.plot(*dt35)

ax1.plot(*dt40)
ax1.plot(*dt41)
ax1.plot(*dt42)
ax1.plot(*dt43)
ax1.plot(*dt44)
ax1.plot(*dt45)

ax1.plot(*dt50, color='r')
ax1.plot(*dt51, color='r')
ax1.plot(*dt52, color='r')
ax1.plot(*dt53, color='r')
ax1.plot(*dt54, color='r')
ax1.plot(*dt55, color='r')

plt.show()


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

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)
dt10 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try02/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt20 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt21 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt22 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt23 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt24 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("Try02_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10, color='b')
ax1.plot(*dt11, color='b')
ax1.plot(*dt12, color='b')
ax1.plot(*dt13, color='b')
ax1.plot(*dt14, color='b')
ax1.plot(*dt15, color='b')

ax1.plot(*dt20, color='r')
ax1.plot(*dt21, color='r')
ax1.plot(*dt22, color='r')
ax1.plot(*dt23, color='r')
ax1.plot(*dt24, color='r')
ax1.plot(*dt25, color='r')

plt.show()


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

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)
dt10 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt11 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt12 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt13 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt15 = np.loadtxt("Try03_3/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt20 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt21 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt22 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt23 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_3.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt24 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("Try03_bbr/rss_rps_rfs_xps_1_0_0_0/ipvs1_5.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10)
ax1.plot(*dt11)
ax1.plot(*dt12)
ax1.plot(*dt13)
ax1.plot(*dt14)
ax1.plot(*dt15)

ax1.plot(*dt20, color='r')
ax1.plot(*dt21, color='r')
ax1.plot(*dt22, color='r')
ax1.plot(*dt23, color='r')
ax1.plot(*dt24, color='r')
ax1.plot(*dt25, color='r')

plt.show()


# In[46]:

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
dt10 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt30 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs3_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt40 = np.loadtxt("Try01_cubic/rss_rps_rfs_xps_0_1_1_1/ipvs4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

dt50 = np.loadtxt("Try02_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt60 = np.loadtxt("Try03_cubic/rss_rps_rfs_xps_1_0_0_0/ipvs1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(*dt10, color='r')
ax1.plot(*dt20, color='r')
ax1.plot(*dt30, color='r')
ax1.plot(*dt40, color='r')

ax1.plot(*dt50, color='b')
ax1.plot(*dt60, color='g')

plt.show()


# In[ ]:



