
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


# In[ ]:



