
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df01=pd.read_csv("cpu08_lv02_1.csv")
df02=pd.read_csv("cpu08_lv02_2.csv")
df03=pd.read_csv("cpu08_lv02_3.csv")
df04=pd.read_csv("cpu08_lv02_4.csv")
df05=pd.read_csv("cpu08_lv02_5.csv")
df06=pd.read_csv("cpu08_lv02_6.csv")
df07=pd.read_csv("cpu08_lv02_7.csv")
df08=pd.read_csv("cpu08_lv02_8.csv")
print(plt.style.available)


# In[5]:

plt.style.use('seaborn-poster')
ax=df01.plot(x='# of pods',y='Req/sec', color='m', label='1st try')
ax=df02.plot(x='# of pods',y='Req/sec', color='r', label='2nd try', ax=ax)
ax=df03.plot(x='# of pods',y='Req/sec', color='g', label='3rd try', ax=ax)
ax=df04.plot(x='# of pods',y='Req/sec', color='b', label='4th try', ax=ax)
ax=df05.plot(x='# of pods',y='Req/sec', color='c', label='5th try', ax=ax)
ax=df06.plot(x='# of pods',y='Req/sec', color='y', label='6th try', ax=ax)
ax=df07.plot(x='# of pods',y='Req/sec', color='k', label='7th try', ax=ax)
ax=df08.plot(x='# of pods',y='Req/sec', color='pink', label='8th try', ax=ax)
ax.set_xlim(0,40)
ax.set_ylim(0,180000)
plt.savefig('lv_rps_vs_pods.png')


# In[ ]:



