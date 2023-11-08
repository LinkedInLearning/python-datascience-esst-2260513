#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# In[2]:


missing = np.nan
series_obj = Series(['row 1', 'row 2',missing,'row 4',np.nan,np.nan,np.nan,'row 8'])
np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj

# In[3]:


DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing
DF_obj


# In[4]:


series_obj

# In[6]:


series_obj.isnull().sum()

# In[7]:


DF_obj.isnull().sum()

# In[ ]:



