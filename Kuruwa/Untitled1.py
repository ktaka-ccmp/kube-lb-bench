
# coding: utf-8

# In[12]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='flannel: host-gw')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='flannel: vxlan', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='flannel: udp', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('iptables proxy performance for (rss,rps)=(0,1) \n')
plt.savefig('SwoppFigs/iptables-proxy-rss-off-rps-on.png')


# In[13]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='flannel: host-gw')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='flannel: vxlan', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='flannel: udp', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('ipvs ingress performance for (rss,rps)=(0,1) \n')
plt.savefig('SwoppFigs/ipvs-ingress-rss-off-rps-on.png')


# In[10]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("24th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv")
df2=pd.read_csv("24th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(0,1)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(1,0)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,0)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('iptables proxy performance for  flannel: host-gw\n')
plt.savefig('SwoppFigs/iptables-proxy-host-gw.png')


# In[11]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv")
df2=pd.read_csv("25th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(0,1)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(1,0)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,0)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('iptables proxy performance for  flannel: vxlan\n')
plt.savefig('SwoppFigs/iptables-proxy-vxlan.png')


# In[8]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("24th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(0,1)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(1,0)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,0)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('ipvs-ingress performance for  flannel: host-gw\n')
plt.savefig('SwoppFigs/ipvs-ingress-host-gw.png')


# In[9]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("25th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(0,1)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(1,0)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(0,0)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('ipvs-ingress performance for  flannel: vxlan\n')
plt.savefig('SwoppFigs/ipvs-ingress-vxlan.png')


# In[16]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/lvs_cpu16_0.csv")
df2=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='ipvs-pod(ingress)')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='ipvs-node', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='iptables-node(proxy)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_ylabel('Request/sec')
plt.title('LB comparison for  flannel: vxlan, (rss,rps)=(0,1)\n')
plt.savefig('SwoppFigs/Ibs-vxlan-rss-off-rps-on.png')


# In[ ]:



