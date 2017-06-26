
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df2=pd.read_csv("rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,1)')
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('iptables proxy performance flannel: host-gw\n')
plt.savefig('iptables_proxy_flannel_hostgw.png')


# In[ ]:




# In[ ]:



