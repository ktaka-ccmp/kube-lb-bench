
# coding: utf-8

# In[86]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure()
ax1 = fig.add_subplot(111)

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
ax1.errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', label='ipvs, pod=10', ls='--',lw='1', fmt='.', capthick=1)

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
ax1.errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', label='iptabls, pod=10', ls='--',lw='1', fmt='.', capthick=1)

plt.legend()

ax1.set_yscale("log", nonposy='clip')

ax1.set_ylabel('Latency [msec]')
ax1.set_xlabel('Load rate [rps]')
ax1.set_xlim(0,200000)
plt.title('LB latency \n flannel:host-gw,  rps=on, rss=off\n')
plt.savefig('latency_rps_10pods.png')
plt.show()


# In[7]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(111)

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_20.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
ax1.errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', label='ipvs, pod=20', ls='--',lw='1', fmt='.', capthick=1)

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
ax1.errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', label='iptabls, pod=20', ls='--',lw='1', fmt='.', capthick=1)

ax1.legend(loc=2)

ax1.set_yscale("log", nonposy='clip')

ax1.set_ylabel('Latency [msec]')
ax1.set_xlabel('Load rate [rps]')
ax1.set_xlim(0,200000)
ax1.grid(ls='--', lw='0.5')
plt.title('LB latency: host-gw,  rps=on, rss=off\n')
plt.savefig('latency_rps_20pods.png')
plt.show()


# In[88]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')

f, axarr = plt.subplots(2, 3, figsize=(20, 15))

axarr[0, 0].set_title('podnum=5')
axarr[0, 1].set_title('podnum=10')
axarr[0, 2].set_title('podnum=20')
axarr[1, 0].set_title('podnum=30')
axarr[1, 1].set_title('podnum=40')

#####ipvs
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_5.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_20.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_30.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs')

#####proxy i.e. iptables DNAT
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_5.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_30.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

axarr[1, 2].remove()

axarr[0, 0].legend(loc="upper left")
axarr[0, 1].legend(loc="upper left")
axarr[0, 2].legend(loc="upper left")
axarr[1, 0].legend(loc="upper left")
axarr[1, 1].legend(loc="upper left")

plt.setp(axarr[0,0].get_xticklabels(), visible=False)
plt.setp(axarr[0,1].get_xticklabels(), visible=False)

plt.setp(axarr[0,1].get_yticklabels(), visible=False)
plt.setp(axarr[0,2].get_yticklabels(), visible=False)
plt.setp(axarr[1,1].get_yticklabels(), visible=False)

for ax in axarr.flat:
    ax.grid(ls='--', lw='0.5')
    ax.set_xlim(0,200000)
    ax.set_ylim(0.1,100000)
    ax.set_yscale("log", nonposy='clip')

axarr[0, 0].set_ylabel('Latency [msec]')
axarr[1, 0].set_ylabel('Latency [msec]')
axarr[0, 2].set_xlabel('Load rate [rps]')
axarr[1, 0].set_xlabel('Load rate [rps]')
axarr[1, 1].set_xlabel('Load rate [rps]')

f.suptitle('Latency median with max-min for ipvs(blue) & iptable DNAT(red),  flannel:host-gw, rss off, rps on', fontsize=24)
plt.savefig('latency_rps_all.png')
plt.show()


# In[91]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')

f, axarr = plt.subplots(2, 3, figsize=(20, 15))

axarr[0, 0].set_title('podnum=5')
axarr[0, 1].set_title('podnum=10')
axarr[0, 2].set_title('podnum=20')
axarr[1, 0].set_title('podnum=30')
axarr[1, 1].set_title('podnum=40')

#####ipvs
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_5.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_20.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_30.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='b', ls='--',lw='1', fmt='.', capthick=1, label='ipvs')

#####proxy i.e. iptables DNAT
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_5.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_20.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[0, 2].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_30.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 0].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40.csv",usecols=(0, 1, 2, 3), delimiter=',', unpack=True, skiprows=1)
axarr[1, 1].errorbar(dt[0],dt[2], yerr=[dt[2]-dt[1],dt[3]-dt[2]], color='r', ls='--',lw='1', fmt='.', capthick=1, label='iptables' )

axarr[1, 2].remove()

axarr[0, 0].legend(loc="upper left")
axarr[0, 1].legend(loc="upper left")
axarr[0, 2].legend(loc="upper left")
axarr[1, 0].legend(loc="upper left")
axarr[1, 1].legend(loc="upper left")

plt.setp(axarr[0,0].get_xticklabels(), visible=False)
plt.setp(axarr[0,1].get_xticklabels(), visible=False)

plt.setp(axarr[0,1].get_yticklabels(), visible=False)
plt.setp(axarr[0,2].get_yticklabels(), visible=False)
plt.setp(axarr[1,1].get_yticklabels(), visible=False)

for ax in axarr.flat:
    ax.grid(ls='--', lw='0.5')
    ax.set_xlim(0,200000)
    ax.set_ylim(0.1,100000)
    ax.set_yscale("log", nonposy='clip')

axarr[0, 0].set_ylabel('Latency [msec]')
axarr[1, 0].set_ylabel('Latency [msec]')
axarr[0, 2].set_xlabel('Load rate [rps]')
axarr[1, 0].set_xlabel('Load rate [rps]')
axarr[1, 1].set_xlabel('Load rate [rps]')

f.suptitle('Latency median with max-min for ipvs(blue) & iptable DNAT(red),  flannel:host-gw, rss on, rps off', fontsize=24)
plt.savefig('latency_rss_all.png')
plt.show()


# In[131]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='160krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_170000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='170krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='180krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_190000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='190krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_40_200000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='200krps')

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='160krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_170000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='170krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='180k rps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_190000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='190k rps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_200000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='200Krps')

ax1.legend(loc=2, prop={'size': 14})
ax2.legend(loc=2, prop={'size': 14})

ax1.set_title('ipvs')
ax2.set_title('iptables')

ax1.set_ylabel('Percentile')
ax1.set_xlabel('Latency [sec]')
ax2.set_xlabel('Latency [sec]')
ax1.set_xlim(0.0001,10)
ax2.set_xlim(0.0001,10)

ax1.grid(ls='--', lw='0.5')
ax2.grid(ls='--', lw='0.5')

fig.suptitle('Latency CDF for 40 pods flannel:host-gw,  rps=on, rss=off\n', fontsize=24)
plt.savefig('latency_cdf_rps_40pods.png')
plt.show()


# In[132]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_70000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='70krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_80000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='80krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_90000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='90krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_100000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='100krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_110000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='110krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_ipvs_10_120000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='y', ls='-',lw='1.5',marker='', label='120krps')

dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_70000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='70krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_80000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='80krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_90000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='90krps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_100000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='100k rps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_110000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='110k rps')
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_120000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='y', ls='-',lw='1.5',marker='', label='120Krps')

ax1.legend(loc=2, prop={'size': 14})
ax2.legend(loc=2, prop={'size': 14})

ax1.set_title('ipvs')
ax2.set_title('iptables')

ax1.set_ylabel('Percentile')
ax1.set_xlabel('Latency [sec]')
ax2.set_xlabel('Latency [sec]')
ax1.set_xlim(0.0001,10)
ax2.set_xlim(0.0001,10)

ax1.grid(ls='--', lw='0.5')
ax2.grid(ls='--', lw='0.5')

fig.suptitle('Latency CDF for 10 pods flannel:host-gw,  rps=on, rss=off\n', fontsize=24)
plt.savefig('latency_cdf_rps_10pods.png')
plt.show()


# In[133]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40_60000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='60krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40_70000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='70krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40_80000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='80krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40_90000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='90krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40_100000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='100krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_40_110000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='y', ls='-',lw='1.5',marker='', label='110krps')

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_140000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='140krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_150000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='150krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_160000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='160k rps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_170000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='170k rps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_180000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='180Krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_190000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='y', ls='-',lw='1.5',marker='', label='190Krps')

ax1.legend(loc=2, prop={'size': 14})
ax2.legend(loc=2, prop={'size': 14})

ax1.set_title('ipvs')
ax2.set_title('iptables')

ax1.set_ylabel('Percentile')
ax1.set_xlabel('Latency [sec]')
ax2.set_xlabel('Latency [sec]')
ax1.set_xlim(0.0001,10)
ax2.set_xlim(0.0001,10)

ax1.grid(ls='--', lw='0.5')
ax2.grid(ls='--', lw='0.5')

fig.suptitle('Latency CDF for 40 pods flannel:host-gw,  rps=off, rss=on\n', fontsize=24)
plt.savefig('latency_cdf_rss_40pods.png')
plt.show()


# In[134]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_60000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='60krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_70000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='70krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_80000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='80krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_90000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='90krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_100000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='100krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_110000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='y', ls='-',lw='1.5',marker='', label='110krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_ipvs_10_120000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.semilogx(dt[1], dt[0], color='k', ls='-',lw='1.5',marker='', label='120krps')

dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_60000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='r', ls='-',lw='1.5',marker='', label='60krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_70000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='g', ls='-',lw='1.5',marker='', label='70krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_80000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='b', ls='-',lw='1.5',marker='', label='80krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_90000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='c', ls='-',lw='1.5',marker='', label='90krps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_100000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='m', ls='-',lw='1.5',marker='', label='100k rps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_110000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='y', ls='-',lw='1.5',marker='', label='110k rps')
dt = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_120000.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax2.semilogx(dt[1], dt[0], color='k', ls='-',lw='1.5',marker='', label='120Krps')

ax1.legend(loc=2, prop={'size': 14})
ax2.legend(loc=2, prop={'size': 14})

ax1.set_title('ipvs')
ax2.set_title('iptables')

ax1.set_ylabel('Percentile')
ax1.set_xlabel('Latency [sec]')
ax2.set_xlabel('Latency [sec]')
ax1.set_xlim(0.0001,10)
ax2.set_xlim(0.0001,10)

ax1.grid(ls='--', lw='0.5')
ax2.grid(ls='--', lw='0.5')

fig.suptitle('Latency CDF for 10 pods flannel:host-gw,  rps=off, rss=on\n', fontsize=24)
plt.savefig('latency_cdf_rss_10pods.png')
plt.show()


# In[ ]:



