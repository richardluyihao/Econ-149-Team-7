#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Key Imports
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col


# In[20]:


#Access Data
url_1 = 'http://research.stlouisfed.org/fred2/series/GDPC1/downloaddata/GDPC1.csv'
data_1 = pd.read_csv(url_1, parse_dates=True)
data_1.head()


# In[21]:


data_1.columns=['DATE','GDP']
data_1.head()


# In[22]:


#Summary Statistics for GDP
data_1.describe()


# In[23]:


#Graphing the GDP
data1=data_1.set_index('DATE')
ax = data1['1947':'2020'].plot(title='US GDP', legend=False, figsize=(12,6))
ax.set_xlabel('year', fontsize=12)
ax.set_ylabel('billion dollars', fontsize=12)
plt.show()


# In[40]:


#Access Data
url_2 = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
data_2 = pd.read_csv(url_2, parse_dates=True)
data_2.head()


# In[41]:


data_2.columns=['DATE','URATE']
data_2.head()


# In[42]:


#Summary Statistics for Unemployment Rate
data_2.describe()


# In[44]:


#Graphing the Unemployment Rate
data2=data_2.set_index('DATE')
ax = data2['1948':'2020'].plot(title='US Unemployment Rate', legend=False, figsize=(12,6))
ax.set_xlabel('year', fontsize=12)
ax.set_ylabel('%', fontsize=12)
plt.show()


# In[48]:


data_merge=pd.merge(data_1, data_2, how='inner', on='DATE', left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
data_merge.head()


# In[ ]:




