
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='flannel: host-gw')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='flannel: vxlan', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='flannel: udp', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('iptables proxy performance for (rss,rps)=(0,1) \n')
plt.savefig('test.png')


# In[ ]:



