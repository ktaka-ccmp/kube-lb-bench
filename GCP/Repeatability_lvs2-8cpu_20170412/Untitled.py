
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df02=pd.read_csv("cpu08_lv02.csv")
df04=pd.read_csv("cpu08_lv04.csv")
df06=pd.read_csv("cpu08_lv06.csv")
df08=pd.read_csv("cpu08_lv08.csv")
df10=pd.read_csv("cpu08_lv10.csv")
df12=pd.read_csv("cpu08_lv12.csv")
df14=pd.read_csv("cpu08_lv14.csv")
df16=pd.read_csv("cpu08_lv16.csv")
print(plt.style.available)


# In[6]:

plt.style.use('seaborn-poster')
ax=df02.plot(x='# of pods',y='Req/sec', color='m', label='lv02')
ax=df04.plot(x='# of pods',y='Req/sec', color='r', label='lv04', ax=ax)
ax=df06.plot(x='# of pods',y='Req/sec', color='b', label='lv06', ax=ax)
ax=df08.plot(x='# of pods',y='Req/sec', color='g', label='lv08', ax=ax)
ax=df10.plot(x='# of pods',y='Req/sec', color='c', label='lv10', ax=ax)
ax=df12.plot(x='# of pods',y='Req/sec', color='y', label='lv12', ax=ax)
ax=df14.plot(x='# of pods',y='Req/sec', color='k', label='lv14', ax=ax)
ax=df16.plot(x='# of pods',y='Req/sec', color='pink', label='lv16', ax=ax)
ax.set_xlim(0,40)
plt.savefig('lv_rps_vs_pods.png')


# In[ ]:



