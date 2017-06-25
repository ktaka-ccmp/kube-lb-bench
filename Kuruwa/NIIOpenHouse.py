
# coding: utf-8

# In[6]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("9th_try/lvs_cpu16_0.csv")
df1=pd.read_csv("12th_try/lvs_cpu16_0.csv")
df2=pd.read_csv("13th_try/lvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='host-gw')
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='vxlan', ax=ax)
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='udp', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('# of nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs\n')
plt.savefig('openhouse.png')


# In[ ]:



