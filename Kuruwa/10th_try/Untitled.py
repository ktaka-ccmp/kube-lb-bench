
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("lvs_cpu16_0.csv")
pf0=pd.read_csv("proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='ipvs#1')
ax=pf0.plot(x='# of pods',y='Req/sec', color='b', label='proxy#1', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
textstr='flannel: host-gw \nrss: off \nrps: off \nrfs: off'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.75, 0.25, textstr, transform=ax.transAxes, fontsize=16,verticalalignment='top', bbox=props)
plt.title('Loadbalancer Performance')
plt.savefig('rps_vs_pods.png')


# In[ ]:



