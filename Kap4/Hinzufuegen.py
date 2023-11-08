#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# In[3]:


DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj

# In[14]:


series_obj = pd.Series(np.arange(6))
series_obj.name = "Spalte"

# In[5]:


series_obj

# In[16]:


pd.concat([DF_obj,series_obj],axis=1)

# In[15]:


DataFrame.join(DF_obj,series_obj)

# In[18]:


DF_obj.append(series_obj)

# In[21]:


DF_obj.append(DF_obj, ignore_index=True)

# In[ ]:



