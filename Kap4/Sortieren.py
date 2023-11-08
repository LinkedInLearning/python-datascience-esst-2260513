#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# In[25]:


arr = np.arange(36).reshape(6,6)
np.random.shuffle(arr)
DF_obj = pd.DataFrame(arr)
DF_obj

# In[4]:


series_obj_1 = pd.Series([42,3,4,18,11,65])


# In[28]:


series_obj_1.sort_values(ascending=False)

# In[5]:


series_obj_2 = pd.Series(['z','A','a','Z','Text','T','text'])

# In[33]:


series_obj_2.sort_values(ascending=True)

# In[36]:


DF_obj.sort_values(by=[1], ascending=False)

# In[ ]:



