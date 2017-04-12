
# coding: utf-8

# In[11]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df02=pd.read_csv("proxy_cpu02.csv")
df04=pd.read_csv("proxy_cpu04.csv")
df08=pd.read_csv("proxy_cpu08.csv")
df12=pd.read_csv("proxy_cpu12.csv")
df16=pd.read_csv("proxy_cpu16.csv")

print(plt.style.available)


# In[12]:

plt.style.use('seaborn-poster')
ax=df02.plot(x='# of pods',y='Req/sec', color='m', label='2cpu')
ax=df04.plot(x='# of pods',y='Req/sec', color='r', label='4cpu', ax=ax)
ax=df08.plot(x='# of pods',y='Req/sec', color='b', label='8cpu', ax=ax)
ax=df12.plot(x='# of pods',y='Req/sec', color='g', label='12cpu', ax=ax)
ax=df16.plot(x='# of pods',y='Req/sec', color='c', label='16cpu', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,80000)
plt.savefig('proxy_rps_vs_pods.png')


# In[13]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df02=pd.read_csv("lvs_cpu02.csv")
df04=pd.read_csv("lvs_cpu04.csv")
df08=pd.read_csv("lvs_cpu08.csv")
df12=pd.read_csv("lvs_cpu12.csv")
df16=pd.read_csv("lvs_cpu16.csv")

print(plt.style.available)


# In[8]:

plt.style.use('seaborn-poster')
ax=df02.plot(x='# of pods',y='Req/sec', color='m', label='2cpu')
ax=df04.plot(x='# of pods',y='Req/sec', color='r', label='4cpu', ax=ax)
ax=df08.plot(x='# of pods',y='Req/sec', color='b', label='8cpu', ax=ax)
ax=df12.plot(x='# of pods',y='Req/sec', color='g', label='12cpu', ax=ax)
ax=df16.plot(x='# of pods',y='Req/sec', color='c', label='16cpu', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,80000)
plt.savefig('lvs_rps_vs_pods.png')


# In[11]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
lvs01 =pd.read_csv("lvs_pod1.csv")
lvs10 =pd.read_csv("lvs_pod10.csv")
lvs20 =pd.read_csv("lvs_pod20.csv")
lvs30 =pd.read_csv("lvs_pod30.csv")
lvs40 =pd.read_csv("lvs_pod40.csv")

plt.style.use('seaborn-poster')
ax=lvs01.plot(x='# of cpu on LB',y='Req/sec', color='m', label='pod # 1')
ax=lvs10.plot(x='# of cpu on LB',y='Req/sec', color='r', label='pod # 10', ax=ax)
ax=lvs20.plot(x='# of cpu on LB',y='Req/sec', color='b', label='pod # 20', ax=ax)
ax=lvs30.plot(x='# of cpu on LB',y='Req/sec', color='g', label='pod # 30', ax=ax)
ax=lvs40.plot(x='# of cpu on LB',y='Req/sec', color='c', label='pod # 40', ax=ax)
ax.set_xlim(0,18)
plt.savefig('lvs_rps_vs_cpus.png')


# In[12]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
prx01 =pd.read_csv("proxy_pod1.csv")
prx10 =pd.read_csv("proxy_pod10.csv")
prx20 =pd.read_csv("proxy_pod20.csv")
prx30 =pd.read_csv("proxy_pod30.csv")
prx40 =pd.read_csv("proxy_pod40.csv")

plt.style.use('seaborn-poster')
ax=prx01.plot(x='# of cpu on LB',y='Req/sec', color='m', label='pod # 1')
ax=prx10.plot(x='# of cpu on LB',y='Req/sec', color='r', label='pod # 10', ax=ax)
ax=prx20.plot(x='# of cpu on LB',y='Req/sec', color='b', label='pod # 20', ax=ax)
ax=prx30.plot(x='# of cpu on LB',y='Req/sec', color='g', label='pod # 30', ax=ax)
ax=prx40.plot(x='# of cpu on LB',y='Req/sec', color='c', label='pod # 40', ax=ax)
ax.set_xlim(0,18)
plt.savefig('prx_rps_vs_cpus.png')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



