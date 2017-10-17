
# coding: utf-8

# In[30]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure()
ax1 = fig.add_subplot(111)

dt1 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt6 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt10 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt16 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt18 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt40 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_0.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt1[1],dt1[0], color='r', label='podnum=1', ls='-',lw='1',marker='')
ax1.plot(dt6[1],dt6[0], color='c', label='podnum=6', ls='-',lw='1',marker='')
ax1.plot(dt10[1],dt10[0], color='g', label='podnum=10', ls='-',lw='1',marker='')
ax1.plot(dt14[1],dt14[0], color='g', label='podnum=14', ls='--',lw='1',marker='')
ax1.plot(dt16[1],dt16[0], color='m', label='podnum=16', ls='-',lw='1',marker='')
ax1.plot(dt18[1],dt18[0], color='m', label='podnum=18', ls='--',lw='1',marker='')
ax1.plot(dt20[1],dt20[0], color='b', label='podnum=20', ls='-',lw='1',marker='')
ax1.plot(dt25[1],dt25[0], color='b', label='podnum=25', ls='--',lw='1',marker='')
ax1.plot(dt40[1],dt40[0], color='y', label='podnum=40', ls='-',lw='1',marker='')
ax1.set_xlabel('Latency [msec]', color='r')
#plt.legend(loc=1, bbox_to_anchor=(0.97, 0.25))
plt.legend()

ax1.set_ylabel('Percentile')

plt.yscale('linear')
plt.xscale('log')

#ax1.set_xlim(0,100)
#ax2.set_ylim(0,110)
plt.title('LB performance \n flannel:host-gw, podnum=40, rps=on, rss=off\n')


# In[31]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure()
ax1 = fig.add_subplot(111)

dt1 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt6 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt10 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt16 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt18 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt40 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt1[1],dt1[0], color='r', label='podnum=1', ls='-',lw='1',marker='')
ax1.plot(dt6[1],dt6[0], color='c', label='podnum=6', ls='-',lw='1',marker='')
ax1.plot(dt10[1],dt10[0], color='g', label='podnum=10', ls='-',lw='1',marker='')
ax1.plot(dt14[1],dt14[0], color='g', label='podnum=14', ls='--',lw='1',marker='')
ax1.plot(dt16[1],dt16[0], color='m', label='podnum=16', ls='-',lw='1',marker='')
ax1.plot(dt18[1],dt18[0], color='m', label='podnum=18', ls='--',lw='1',marker='')
ax1.plot(dt20[1],dt20[0], color='b', label='podnum=20', ls='-',lw='1',marker='')
ax1.plot(dt25[1],dt25[0], color='b', label='podnum=25', ls='--',lw='1',marker='')
ax1.plot(dt40[1],dt40[0], color='y', label='podnum=40', ls='-',lw='1',marker='')
ax1.set_xlabel('Latency [msec]', color='r')
#plt.legend(loc=1, bbox_to_anchor=(0.97, 0.25))
plt.legend()

ax1.set_ylabel('Percentile')

plt.yscale('linear')
plt.xscale('log')

#ax1.set_xlim(0,100)
#ax2.set_ylim(0,110)
plt.title('LB performance \n flannel:host-gw, podnum=40, rps=on, rss=off\n')


# In[32]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure()
ax1 = fig.add_subplot(111)

dt1 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt6 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_6_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt10 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_10_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_14_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt16 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_16_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt18 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_18_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_20_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_25_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt40 = np.loadtxt("rss_rps_rfs_1_0_0/latency_proxy_40_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
ax1.plot(dt1[1],dt1[0], color='r', label='podnum=1', ls='-',lw='1',marker='')
ax1.plot(dt6[1],dt6[0], color='c', label='podnum=6', ls='-',lw='1',marker='')
ax1.plot(dt10[1],dt10[0], color='g', label='podnum=10', ls='-',lw='1',marker='')
ax1.plot(dt14[1],dt14[0], color='g', label='podnum=14', ls='--',lw='1',marker='')
ax1.plot(dt16[1],dt16[0], color='m', label='podnum=16', ls='-',lw='1',marker='')
ax1.plot(dt18[1],dt18[0], color='m', label='podnum=18', ls='--',lw='1',marker='')
ax1.plot(dt20[1],dt20[0], color='b', label='podnum=20', ls='-',lw='1',marker='')
ax1.plot(dt25[1],dt25[0], color='b', label='podnum=25', ls='--',lw='1',marker='')
ax1.plot(dt40[1],dt40[0], color='y', label='podnum=40', ls='-',lw='1',marker='')
ax1.set_xlabel('Latency [msec]', color='r')
#plt.legend(loc=1, bbox_to_anchor=(0.97, 0.25))
plt.legend()

ax1.set_ylabel('Percentile')

plt.yscale('linear')
plt.xscale('log')

#ax1.set_xlim(0,100)
#ax2.set_ylim(0,110)
plt.title('LB performance \n flannel:host-gw, podnum=40, rps=on, rss=off\n')


# In[41]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')
fig = plt.figure()
ax1 = fig.add_subplot(331)
ax2 = fig.add_subplot(332)
ax3 = fig.add_subplot(333)
ax4 = fig.add_subplot(334)
ax5 = fig.add_subplot(335)
ax6 = fig.add_subplot(336)
ax7 = fig.add_subplot(337)
ax8 = fig.add_subplot(338)
ax9 = fig.add_subplot(339)

dt1 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt6 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt10 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt14 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt16 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt18 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt20 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt25 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt40 = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax1.plot(dt1[1],dt1[0], color='r', label='podnum=1', ls='-',lw='1',marker='')
ax2.plot(dt6[1],dt6[0], color='c', label='podnum=6', ls='-',lw='1',marker='')
ax3.plot(dt10[1],dt10[0], color='g', label='podnum=10', ls='-',lw='1',marker='')
ax4.plot(dt14[1],dt14[0], color='g', label='podnum=14', ls='--',lw='1',marker='')
ax5.plot(dt16[1],dt16[0], color='m', label='podnum=16', ls='-',lw='1',marker='')
ax6.plot(dt18[1],dt18[0], color='m', label='podnum=18', ls='--',lw='1',marker='')
ax7.plot(dt20[1],dt20[0], color='b', label='podnum=20', ls='-',lw='1',marker='')
ax8.plot(dt25[1],dt25[0], color='b', label='podnum=25', ls='--',lw='1',marker='')
ax9.plot(dt40[1],dt40[0], color='y', label='podnum=40', ls='-',lw='1',marker='')
ax1.set_xlabel('Latency [msec]', color='r')
#plt.legend(loc=1, bbox_to_anchor=(0.97, 0.25))
#plt.legend()


ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax4.set_xscale('log')
ax5.set_xscale('log')
ax6.set_xscale('log')
ax7.set_xscale('log')
ax8.set_xscale('log')
ax9.set_xscale('log')


#ax1.set_xlim(0,100)
#ax2.set_ylim(0,110)
#plt.title('LB performance \n flannel:host-gw, podnum=40, rps=on, rss=off\n')


# In[49]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.style.use('seaborn-poster')

plt.subplot(531)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_1_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(532)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_2_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=6')
plt.grid(True)

plt.subplot(533)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_4_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(534)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_6_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(535)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_8_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(536)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_10_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(537)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_12_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(538)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_14_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(539)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_16_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(5,3,10)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_18_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(5,3,11)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_20_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(5,3,12)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_25_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(5,3,13)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_30_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(5,3,14)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_35_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)

plt.subplot(5,3,15)
dt = np.loadtxt("rss_rps_rfs_0_1_0/latency_proxy_40_1.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
plt.semilogx(dt[1],dt[0], color='r', ls='-',lw='1',marker='')
plt.title('podnum=1')
plt.grid(True)


#ax1.set_xlim(0,100)
#ax2.set_ylim(0,110)
#plt.title('LB performance \n flannel:host-gw, podnum=40, rps=on, rss=off\n')


# In[84]:

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


# In[ ]:



