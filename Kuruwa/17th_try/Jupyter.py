
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("rss_rps_rfs_0_0_0/lvs_cpu16_0.csv")
df1=pd.read_csv("rss_rps_rfs_1_0_0/lvs_cpu16_0.csv")
df2=pd.read_csv("rss_rps_rfs_0_1_0/lvs_cpu16_0.csv")
df3=pd.read_csv("rss_rps_rfs_1_1_0/lvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(0,0)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(1,0)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,1)', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='c', label='(rss,rps)=(1,1)', ax=ax)
ax.set_xlim(0,40)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('ipvs pod performance flannel: vxlan\n')
plt.savefig('ipvs_ingress_flannel_vxlan.png')


# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("rss_rps_rfs_0_0_0/proxy_cpu16_0.csv")
df1=pd.read_csv("rss_rps_rfs_1_0_0/proxy_cpu16_0.csv")
df2=pd.read_csv("rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df3=pd.read_csv("rss_rps_rfs_1_1_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(0,0)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(1,0)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,1)', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='c', label='(rss,rps)=(1,1)', ax=ax)
ax.set_xlim(0,40)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('iptables proxy performance flannel: vxlan\n')
plt.savefig('iptables_proxy_flannel_vxlan.png')


# In[ ]:



