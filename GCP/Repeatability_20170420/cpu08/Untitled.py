
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df02=pd.read_csv("ipt_lv02.csv")
df04=pd.read_csv("ipt_lv04.csv")
df06=pd.read_csv("ipt_lv06.csv")
df08=pd.read_csv("ipt_lv08.csv")
plt.style.use('seaborn-poster')
ax=df02.plot(x='# of pods',y='Req/sec', color='m', label='lv02')
ax=df04.plot(x='# of pods',y='Req/sec', color='r', label='lv04', ax=ax)
ax=df06.plot(x='# of pods',y='Req/sec', color='b', label='lv06', ax=ax)
ax=df08.plot(x='# of pods',y='Req/sec', color='g', label='lv08', ax=ax)
ax.set_xlim(0,40)
plt.savefig('ipt_rps_vs_pods.png')


# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df02=pd.read_csv("ipvs_lv02.csv")
df04=pd.read_csv("ipvs_lv04.csv")
df06=pd.read_csv("ipvs_lv06.csv")
df08=pd.read_csv("ipvs_lv08.csv")
plt.style.use('seaborn-poster')
ax=df02.plot(x='# of pods',y='Req/sec', color='m', label='lv02')
ax=df04.plot(x='# of pods',y='Req/sec', color='r', label='lv04', ax=ax)
ax=df06.plot(x='# of pods',y='Req/sec', color='b', label='lv06', ax=ax)
ax=df08.plot(x='# of pods',y='Req/sec', color='g', label='lv08', ax=ax)
ax.set_xlim(0,40)
plt.savefig('ipvs_rps_vs_pods.png')


# In[ ]:



