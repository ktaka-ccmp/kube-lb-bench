
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("proxy_cpu16_0.csv")
df1=pd.read_csv("proxy_cpu16_1.csv")
df2=pd.read_csv("proxy_cpu16_2.csv")
df3=pd.read_csv("proxy_cpu16_3.csv")
df4=pd.read_csv("proxy_cpu16_4.csv")
df5=pd.read_csv("proxy_cpu16_5.csv")
df6=pd.read_csv("proxy_cpu16_6.csv")
df7=pd.read_csv("proxy_cpu16_7.csv")
df8=pd.read_csv("proxy_cpu16_8.csv")
df9=pd.read_csv("proxy_cpu16_9.csv")
print(plt.style.available)
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='0')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='1', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='2', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='c', label='3', ax=ax)
ax=df4.plot(x='# of pods',y='Req/sec', color='m', label='4', ax=ax)
ax=df5.plot(x='# of pods',y='Req/sec', color='k', label='5', ax=ax)
ax=df6.plot(x='# of pods',y='Req/sec', color='y', label='6', ax=ax)
ax=df7.plot(x='# of pods',y='Req/sec', color='pink', label='7', ax=ax)
ax=df8.plot(x='# of pods',y='Req/sec', color='tan', label='8', ax=ax)
ax=df9.plot(x='# of pods',y='Req/sec', color='teal', label='9', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,180000)
plt.savefig('proxy_rps_vs_pods.png')


# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("lvs_cpu16_0.csv")
df1=pd.read_csv("lvs_cpu16_1.csv")
df2=pd.read_csv("lvs_cpu16_2.csv")
df3=pd.read_csv("lvs_cpu16_3.csv")
df4=pd.read_csv("lvs_cpu16_4.csv")
df5=pd.read_csv("lvs_cpu16_5.csv")
df6=pd.read_csv("lvs_cpu16_6.csv")
df7=pd.read_csv("lvs_cpu16_7.csv")
df8=pd.read_csv("lvs_cpu16_8.csv")
df9=pd.read_csv("lvs_cpu16_9.csv")
print(plt.style.available)
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='0')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='1', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='2', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='c', label='3', ax=ax)
ax=df4.plot(x='# of pods',y='Req/sec', color='m', label='4', ax=ax)
ax=df5.plot(x='# of pods',y='Req/sec', color='k', label='5', ax=ax)
ax=df6.plot(x='# of pods',y='Req/sec', color='y', label='6', ax=ax)
ax=df7.plot(x='# of pods',y='Req/sec', color='pink', label='7', ax=ax)
ax=df8.plot(x='# of pods',y='Req/sec', color='tan', label='8', ax=ax)
ax=df9.plot(x='# of pods',y='Req/sec', color='teal', label='9', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,180000)
plt.savefig('lvs_rps_vs_pods.png')


# In[ ]:



