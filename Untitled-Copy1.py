
# coding: utf-8

# In[14]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("AWS/2nd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df1=pd.read_csv("GCP/2nd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df2=pd.read_csv("AWS/2nd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df3=pd.read_csv("GCP/2nd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='aws,rss', linestyle='dashed')
ax=df1.plot(x='# of pods',y='Req/sec', color='b', label='gcp,rss', linestyle='dashed', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='r', label='aws,rps', linestyle='solid', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='b', label='gcp,rps', linestyle='solid', ax=ax)
ax.set_xlim(0,50)
#ax.set_ylim(0,200000)
ax.set_xlabel('# of nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs\n')
#plt.savefig('openhouse.png')


# In[24]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("AWS/3rd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df1=pd.read_csv("AWS/4th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df2=pd.read_csv("AWS/6th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df3=pd.read_csv("AWS/5th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")

df4=pd.read_csv("AWS/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df5=pd.read_csv("AWS/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df6=pd.read_csv("AWS/6th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df7=pd.read_csv("AWS/5th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='m4.4xlarge,rss', linestyle='dashed')
ax=df1.plot(x='# of pods',y='Req/sec', color='g', label='c4.8xlarge,rss', linestyle='dashed', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='cyan', label='m4.10xlarge,rss', linestyle='dashed', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='b', label='m4.16xlarge,rss', linestyle='dashed', ax=ax)

ax=df4.plot(x='# of pods',y='Req/sec', color='r', label='m4.4xlarge,rps', linestyle='solid', ax=ax)
ax=df5.plot(x='# of pods',y='Req/sec', color='g', label='c4.8xlarge,rps', linestyle='solid', ax=ax)
ax=df6.plot(x='# of pods',y='Req/sec', color='cyan', label='m4.10xlarge,rps', linestyle='solid', ax=ax)
ax=df7.plot(x='# of pods',y='Req/sec', color='b', label='m4.16xlarge,rps', linestyle='solid', ax=ax)
ax.set_xlim(0,40)
#ax.set_ylim(0,200000)
ax.set_xlabel('# of pods i.e. nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on AWS\n')
plt.savefig('aws_all.png')


# In[27]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df8=pd.read_csv("AWS/7th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_1.csv")
df0=pd.read_csv("AWS/3rd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df2=pd.read_csv("AWS/6th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df3=pd.read_csv("AWS/5th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")

df9=pd.read_csv("AWS/7th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_1.csv")
df4=pd.read_csv("AWS/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df6=pd.read_csv("AWS/6th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df7=pd.read_csv("AWS/5th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
plt.style.use('seaborn-poster')
ax=df8.plot(x='# of pods',y='Req/sec', color='g', label='m4.2xlarge,rss', linestyle='dashed')
ax=df0.plot(x='# of pods',y='Req/sec', color='r', label='m4.4xlarge,rss', linestyle='dashed', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='cyan', label='m4.10xlarge,rss', linestyle='dashed', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='b', label='m4.16xlarge,rss', linestyle='dashed', ax=ax)

ax=df9.plot(x='# of pods',y='Req/sec', color='g', label='m4.2xlarge,rps', linestyle='solid', ax=ax)
ax=df4.plot(x='# of pods',y='Req/sec', color='r', label='m4.4xlarge,rps', linestyle='solid', ax=ax)
ax=df6.plot(x='# of pods',y='Req/sec', color='cyan', label='m4.10xlarge,rps', linestyle='solid', ax=ax)
ax=df7.plot(x='# of pods',y='Req/sec', color='b', label='m4.16xlarge,rps', linestyle='solid', ax=ax)
ax.set_xlim(0,40)
#ax.set_ylim(0,200000)
ax.set_xlabel('# of pods i.e. nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on AWS\n')
plt.savefig('aws_m4.png', dpi=300)


# In[35]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("GCP/4th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df1=pd.read_csv("GCP/3rd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df2=pd.read_csv("GCP/5th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df3=pd.read_csv("GCP/6th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")

df4=pd.read_csv("GCP/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df5=pd.read_csv("GCP/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df6=pd.read_csv("GCP/5th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df7=pd.read_csv("GCP/6th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='b', label='8 cpu,rss', linestyle='dashed')
ax=df1.plot(x='# of pods',y='Req/sec', color='r', label='16 cpu,rss', linestyle='dashed', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='g', label='32 cpu,rss', linestyle='dashed', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='m', label='64 cpu,rss', linestyle='dashed', ax=ax)

ax=df4.plot(x='# of pods',y='Req/sec', color='b', label='8 cpu, rps', linestyle='solid', ax=ax)
ax=df5.plot(x='# of pods',y='Req/sec', color='r', label='16 cpu,rps', linestyle='solid', ax=ax)
ax=df6.plot(x='# of pods',y='Req/sec', color='g', label='32 cpu,rps', linestyle='solid', ax=ax)
ax=df7.plot(x='# of pods',y='Req/sec', color='m', label='64 cpu,rps', linestyle='solid', ax=ax)
ax.set_xlim(0,40)
#ax.set_ylim(0,200000)
ax.set_xlabel('# of pods i.e. nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on GCP\n')
plt.savefig('gcp_all.png', dpi=300)


# In[34]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df0=pd.read_csv("AWS/9th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df1=pd.read_csv("AWS/8th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")
df2=pd.read_csv("AWS/4th_try/rss_rps_rfs_1_0_0/ipvs_cpu16_4.csv")

df3=pd.read_csv("AWS/9th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df4=pd.read_csv("AWS/8th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
df5=pd.read_csv("AWS/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv")
plt.style.use('seaborn-poster')
ax=df0.plot(x='# of pods',y='Req/sec', color='g', label='c4.2xlarge,rss', linestyle='dashed')
ax=df1.plot(x='# of pods',y='Req/sec', color='r', label='c4.4xlarge,rss', linestyle='dashed', ax=ax)
ax=df2.plot(x='# of pods',y='Req/sec', color='b', label='c4.8xlarge,rss', linestyle='dashed', ax=ax)
ax=df3.plot(x='# of pods',y='Req/sec', color='g', label='c4.2xlarge,rps', linestyle='solid', ax=ax)
ax=df4.plot(x='# of pods',y='Req/sec', color='r', label='c4.4xlarge,rps', linestyle='solid', ax=ax)
ax=df5.plot(x='# of pods',y='Req/sec', color='b', label='c4.8xlarge,rps', linestyle='solid', ax=ax)
ax.set_xlim(0,40)
#ax.set_ylim(0,200000)
ax.set_xlabel('# of pods i.e. nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on AWS\n')
plt.savefig('aws_c4.png')


# In[9]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df100=pd.read_csv("GCP/3rd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_all.csv")
df010=pd.read_csv("GCP/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_all.csv")
plt.style.use('seaborn-poster')
ax=df100.plot(x='# of pods',y='Req/sec', color='b', label='16 cpu,rss', linestyle='none',marker='.')
ax=df010.plot(x='# of pods',y='Req/sec', color='r', label='16 cpu,rps', linestyle='none',marker='.', ax=ax)

ax.set_xlim(0,40)
#ax.set_ylim(0,200000)
ax.set_xlabel('# of pods i.e. nginx containers')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on GCP\n')


# In[40]:

df100grouped = df100.groupby('# of pods')
df100grouped.describe()
df100grouped.ngroups
df100grouped.groups.keys()
df100grouped.describe()


# In[139]:

df010grouped = df010.groupby('# of pods')
df010grouped.describe()
#plt.figure()
x=df100grouped.groups.keys()
means=df100grouped.mean()
error=df100grouped.std()
#plt.plot(df100grouped.mean())
#df010grouped.mean().plot()
#plt.plot(y)
#plt.errorbar(y,yerr=e)
#plt.errorbar(trip.index, 'gas', yerr='std', data=trip)
#df100grouped.mean().plot(yerr=df100grouped.std())
#ax.errorbar(df100grouped.groups.keys(), df100grouped.mean() , yerr= df100grouped.std(),fmt='.')
type(df100grouped.groups.keys())
data=df100.groupby('# of pods').agg(['mean', 'std'])

gp=df010.groupby('# of pods')
means=gp.mean()
errors=gp.std()
#data.plot()
fig, ax = plt.subplots()
#means.plot.bar(yerr=errors, ax=ax)
#means.plot(yerr=errors, ax=ax)
#pd.__version__
#data.plot(yerr=errors, ax=ax)
data.reset_index().as_matrix()
d2=data.reset_index().values.T
plt.errorbar(d2[0],d2[1],yerr=d2[2],fmt='.', ls='dashed',lw='1')
d2


# In[154]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df100=pd.read_csv("GCP/3rd_try/rss_rps_rfs_1_0_0/ipvs_cpu16_all.csv")
df010=pd.read_csv("GCP/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_all.csv")
plt.style.use('seaborn-poster')

fig, ax = plt.subplots()
d100=df100.groupby('# of pods').agg(['mean', 'std']).reset_index().as_matrix().T
d010=df010.groupby('# of pods').agg(['mean', 'std']).reset_index().as_matrix().T
ax.errorbar(d100[0],d100[1],yerr=d100[2]*2,fmt='.', ls='solid',lw='1', label='rss')
ax.errorbar(d010[0],d010[1],yerr=d010[2]*2,fmt='.', ls='solid',lw='1', label='rps')

ax.set_ylabel('Request/sec')
ax.set_xlabel('# of pods')
plt.title('GCP 16CPU 20 times stats \n')
#plt.savefig('n5.png',dpi=500)

plt.show()
d100
d010


# In[187]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df002=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs002.csv")
df004=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs004.csv")
df006=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs006.csv")
df008=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs008.csv")
df010=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs010.csv")
df012=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs012.csv")
df014=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs014.csv")
df016=pd.read_csv("GCP/7th_try/rss_rps_rfs_0_1_0/ipvs_on_kt-lvs016.csv")
df002['Epoch'] = pd.to_datetime(df002['Epoch'],unit='s')
df004['Epoch'] = pd.to_datetime(df004['Epoch'],unit='s')
df006['Epoch'] = pd.to_datetime(df006['Epoch'],unit='s')
df008['Epoch'] = pd.to_datetime(df008['Epoch'],unit='s')
df010['Epoch'] = pd.to_datetime(df010['Epoch'],unit='s')
df012['Epoch'] = pd.to_datetime(df012['Epoch'],unit='s')
df014['Epoch'] = pd.to_datetime(df014['Epoch'],unit='s')
df016['Epoch'] = pd.to_datetime(df016['Epoch'],unit='s')
plt.style.use('seaborn-poster')
ax=df002.plot(x='Epoch',y='Req/sec', color='r', label='Skylake,16 cpu, rps', ls='--',lw='1',marker='.')
ax=df004.plot(x='Epoch',y='Req/sec', color='b', label='Skylake,16 cpu, rps', ls='--',lw='1',marker='.', ax=ax)
ax=df006.plot(x='Epoch',y='Req/sec', color='g', label='Skylake,16 cpu, rps', ls='--',lw='1',marker='.', ax=ax)
ax=df008.plot(x='Epoch',y='Req/sec', color='y', label='Skylake,16 cpu, rps', ls='--',lw='1',marker='.', ax=ax)
ax=df010.plot(x='Epoch',y='Req/sec', color='r', label='Broadwell,16 cpu, rps', ls='--',lw='1',marker='*', ax=ax)
ax=df012.plot(x='Epoch',y='Req/sec', color='b', label='Broadwell,16 cpu, rps', ls='--',lw='1',marker='*', ax=ax)
ax=df014.plot(x='Epoch',y='Req/sec', color='g', label='Broadwell,16 cpu, rps', ls='--',lw='1',marker='*', ax=ax)
ax=df016.plot(x='Epoch',y='Req/sec', color='y', label='Broadwell,16 cpu, rps', ls='--',lw='1',marker='*', ax=ax)

#ax.set_xlim(0,40)
ax.set_ylim(0,200000)
ax.set_xlabel('Time')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on GCP\n')
plt.savefig('gcp_16core_stability.png')


# In[192]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df101=pd.read_csv("AWS/10th_try/rss_rps_rfs_0_1_0/ipvs_on_ip-10-0-0-101.csv")
df102=pd.read_csv("AWS/10th_try/rss_rps_rfs_0_1_0/ipvs_on_ip-10-0-0-102.csv")
df101['Epoch'] = pd.to_datetime(df101['Epoch'],unit='s')
df102['Epoch'] = pd.to_datetime(df102['Epoch'],unit='s')
plt.style.use('seaborn-poster')
ax=df101.plot(x='Epoch',y='Req/sec', color='r', label='m4.4xlarge,16 cpu, rps', ls='--',lw='1',marker='.')
ax=df102.plot(x='Epoch',y='Req/sec', color='b', label='m4.4xlarge,16 cpu, rps', ls='--',lw='1',marker='.', ax=ax)

#ax.set_xlim(0,40)
ax.set_ylim(0,140000)
ax.set_xlabel('Time')
ax.set_ylabel('Request/sec')
plt.title('Loadbalancer Performance for ipvs on AWS\n')
plt.savefig('aws_16core_stability.png')


# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
sns.set_style("white")
sns.set_context("paper")

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

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

dt1 = np.loadtxt("GCP/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt2 = np.loadtxt("GCP/3rd_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt3 = np.loadtxt("GCP/5th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt4 = np.loadtxt("GCP/6th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

#ax.plot(*dt4, color='c', label='64 cpu,rps')
ax.plot(*dt3, color='g', label='gcp, custom instance, 32 cpu')
ax.plot(*dt2, color='r', label='gcp, custom instance, 16 cpu')
ax.plot(*dt1, color='b', label='gcp, custom instance, 8 cpu')

ax.set_xlim(0,41)
ax.set_ylim(0,180000)
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax.set_xlabel('Number of nginx pods')
ax.set_ylabel('Throughput [req/sec]')
ax.legend(loc=(0.55,0.1))

#plt.title('Ipvs Loadbalancer Performance on GCP\n')

plt.savefig('gcp_all_ieice.png', dpi=300)


# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import seaborn as sns
sns.set_style("white")
sns.set_context("paper")

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

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

dt1 = np.loadtxt("AWS/9th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt2 = np.loadtxt("AWS/8th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)
dt3 = np.loadtxt("AWS/4th_try/rss_rps_rfs_0_1_0/ipvs_cpu16_4.csv",usecols=(0, 1), delimiter=',', unpack=True, skiprows=1)

ax.plot(*dt3, color='g', label='aws, c4.8xlarge, 32cpu')
ax.plot(*dt2, color='r', label='aws, c4.4xlarge, 16cpu')
ax.plot(*dt1, color='b', label='aws, c4.2xlarge, 8cpu')

ax.set_xlim(0,41)
ax.set_ylim(0,120000)
ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

ax.set_xlabel('Number of nginx pods')
ax.set_ylabel('Throughput [req/sec]')
ax.legend(loc=(0.6,0.1))

#plt.title('Ipvs Loadbalancer Performance on AWS\n')
plt.savefig('aws_c4_ieice.png', dpi=300)


# In[ ]:



