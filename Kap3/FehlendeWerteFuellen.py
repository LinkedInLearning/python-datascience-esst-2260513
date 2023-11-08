#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# In[13]:


missing = np.nan
np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj

# In[14]:


DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing
DF_obj

# In[17]:


filled_DF = DF_obj.fillna(0)
filled_DF

# In[18]:


filled_DF = DF_obj.fillna({0:0.1,5:1.25})
filled_DF

# In[ ]:



