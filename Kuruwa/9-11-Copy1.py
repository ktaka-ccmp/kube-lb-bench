
# coding: utf-8

# In[13]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("9th_try/lvs_cpu16_0.csv")
pf0=pd.read_csv("9th_try/proxy_cpu16_0.csv")
df1=pd.read_csv("11th_try/lvs_cpu16_0.csv")
pf1=pd.read_csv("11th_try/proxy_cpu16_0.csv")
df2=pd.read_csv("10th_try/lvs_cpu16_0.csv")
pf2=pd.read_csv("10th_try/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='ipvs#1')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='ipvs#2', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='ipvs#3', ax=ax)
ax=pf0.plot(x='# of pods',y='Req/sec', color='r', label='proxy#1', linestyle='dashed', ax=ax)
ax=pf1.plot(x='# of pods',y='Req/sec', color='g', label='proxy#2', linestyle='dashed', ax=ax)
ax=pf2.plot(x='# of pods',y='Req/sec', color='b', label='proxy#3', linestyle='dashed',  ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
textstr='flannel: host-gw \n#1: rss=on, rps=on, rfs=on \n#2: rss=on, rps=off, rfs=off \n#3: rss=off, rps=off, rfs=off'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.55, 0.20, textstr, transform=ax.transAxes, fontsize=16,verticalalignment='top', bbox=props)
plt.title('Loadbalancer Performance\n')
plt.savefig('rps_vs_pods.png')


# In[ ]:



