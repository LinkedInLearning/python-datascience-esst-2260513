#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# In[2]:


DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj

# In[3]:


DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
DF_obj_2

# In[4]:


series_obj = pd.Series(np.arange(6))

# In[5]:


series_obj

# In[6]:


series_obj_2 = pd.Series(np.arange(7))

# In[8]:


series_obj_2

# In[9]:


series_obj_3 = pd.Series(np.arange(3))

# In[10]:


series_obj_3

# In[16]:


pd.concat([series_obj, series_obj_2])

# In[17]:


pd.concat([DF_obj, DF_obj_2])

# In[19]:


pd.concat([DF_obj, DF_obj_2],axis=1)

# In[22]:


pd.concat([DF_obj, series_obj_3],axis=1)

# In[23]:


pd.concat([DF_obj, series_obj_3],axis=0)

# In[ ]:



