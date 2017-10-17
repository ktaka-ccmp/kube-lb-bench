
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')

f, axarr = plt.subplots(5, 3, figsize=(15, 20))

axarr[0, 0].set_title('podnum=1')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[0, 1].set_title('podnum=2')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_2_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_2_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[0, 2].set_title('podnum=4')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_4_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_4_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[1, 0].set_title('podnum=6')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[1, 1].set_title('podnum=8')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_8_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_8_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_8_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[1, 2].set_title('podnum=10')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[2, 0].set_title('podnum=12')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_12_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_12_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_12_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[2, 1].set_title('podnum=14')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[2, 2].set_title('podnum=16')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[3, 0].set_title('podnum=18')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[3, 1].set_title('podnum=20')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[3, 2].set_title('podnum=25')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[4, 0].set_title('podnum=30')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_30_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_30_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_30_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[4, 1].set_title('podnum=35')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_35_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_35_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_35_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[4, 2].set_title('podnum=40')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[2, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[3, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 2]], visible=False)

for ax in axarr.flat:
    ax.set_xlim(0.1, 10000)
    ax.set_yticks([0,0.25, 0.5, 0.75,1])
    ax.grid(ls='--', lw='0.5')
    
axarr[4, 1].set_xlabel('Latency [ms]')
axarr[2, 0].set_ylabel('Percentile')
    
plt.show()


# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')

f, axarr = plt.subplots(5, 3, figsize=(15, 20))

axarr[0, 0].set_title('podnum=1')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_1_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[0, 1].set_title('podnum=2')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_2_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_2_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_2_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[0, 2].set_title('podnum=4')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_4_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_4_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_4_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[1, 0].set_title('podnum=6')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_6_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_6_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_6_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[1, 1].set_title('podnum=8')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_8_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_8_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_8_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[1, 2].set_title('podnum=10')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[1, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[2, 0].set_title('podnum=12')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_12_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_12_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_12_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[2, 1].set_title('podnum=14')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_14_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_14_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_14_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[2, 2].set_title('podnum=16')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_16_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_16_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_16_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[2, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[3, 0].set_title('podnum=18')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_18_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_18_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_18_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[3, 1].set_title('podnum=20')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_20_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_20_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_20_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[3, 2].set_title('podnum=25')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_25_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_25_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_25_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[3, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[4, 0].set_title('podnum=30')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_30_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 0].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_30_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 0].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_30_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 0].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[4, 1].set_title('podnum=35')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_35_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 1].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_35_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 1].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_35_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 1].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

axarr[4, 2].set_title('podnum=40')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 2].semilogx(dt[1], dt[0], color='r', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 2].semilogx(dt[1], dt[0], color='g', ls='-',lw='1',marker='')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_2.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
axarr[4, 2].semilogx(dt[1], dt[0], color='b', ls='-',lw='1',marker='')

plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[2, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[3, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 2]], visible=False)

for ax in axarr.flat:
    ax.set_xlim(0.1, 10000)
    ax.set_yticks([0,0.25, 0.5, 0.75,1])
    ax.grid(ls='--', lw='0.5')
    
axarr[4, 1].set_xlabel('Latency [ms]')
axarr[2, 0].set_ylabel('Percentile')
    
plt.show()


# In[ ]:



