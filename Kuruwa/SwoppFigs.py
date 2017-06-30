
# coding: utf-8

# In[160]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='flannel: host-gw', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='flannel: vxlan', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='flannel: udp', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('iptables, (rss,rps)=(off,on) \n')
plt.savefig('SwoppFigs/iptables-proxy-rss-off-rps-on.png')


# In[136]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='flannel: host-gw', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='flannel: vxlan', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='flannel: udp', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('ipvs ingress performance for (rss,rps)=(off,on) \n')
plt.savefig('SwoppFigs/ipvs-ingress-rss-off-rps-on.png')


# In[137]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("talk")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("27th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("27th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv")
df2=pd.read_csv("27th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(off,on)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(on,off)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(off,off)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('iptables proxy performance for  flannel: host-gw\n')
plt.savefig('SwoppFigs/iptables-proxy-host-gw.png')


# In[139]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv")
df2=pd.read_csv("25th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(off,on)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(on,off)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(off,off)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('iptables proxy performance for  flannel: vxlan\n')
plt.savefig('SwoppFigs/iptables-proxy-vxlan.png')


# In[140]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
df1=pd.read_csv("26th_try/rss_rps_rfs_1_0_0/proxy_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_0_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(off,on)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(on,off)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(off,off)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,100000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('iptables proxy performance for  flannel: udp\n')
plt.savefig('SwoppFigs/iptables-proxy-udp.png')


# In[158]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("24th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("24th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("24th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(off,on)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(on,off)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(off,off)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.legend(loc=(0.55,0.65))
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('ipvs-ingress performance for  flannel: host-gw\n')
plt.savefig('SwoppFigs/ipvs-ingress-host-gw.png')


# In[159]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("25th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(off,on)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(on,off)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(off,off)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.legend(loc=(0.55,0.55))
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('ipvs-ingress performance for  flannel: vxlan\n')
plt.savefig('SwoppFigs/ipvs-ingress-vxlan.png')


# In[143]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("26th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("26th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_0.csv")
df2=pd.read_csv("26th_try/rss_rps_rfs_0_0_0/ipvs_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='(rss,rps)=(off,on)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='(rss,rps)=(on,off)', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='(rss,rps)=(off,off)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,100000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('ipvs-ingress performance for  flannel: udp\n')
plt.savefig('SwoppFigs/ipvs-ingress-udp.png')


# In[144]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib.ticker import FuncFormatter

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
#                    print (val, signf)
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

sns.set_style("white")
sns.set_context("poster")

get_ipython().magic('matplotlib inline')
df0=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_0.csv")
df1=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/lvs_cpu16_0.csv")
df2=pd.read_csv("25th_try/rss_rps_rfs_0_1_0/proxy_cpu16_0.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='ipvs-pod(ingress)', figsize=(8, 6))
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='ipvs-node', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='iptables-node(proxy)', ax=ax)
ax.set_xlim(0,50)
ax.set_ylim(0,200000)
ax.set_xlabel('Number of pods')
ax.set_ylabel('Request/sec')
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))
plt.title('LB comparison for  flannel: vxlan, (rss,rps)=(off,on)\n')
plt.savefig('SwoppFigs/Ibs-vxlan-rss-off-rps-on.png')


# In[ ]:



