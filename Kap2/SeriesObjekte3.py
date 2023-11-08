#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# In[12]:


series_obj = Series(np.arange(8),index=['row 1', 'row 2','row 3','row 4','row 5','row 6','row 7','row 8'])

# In[13]:


series_obj

# In[18]:


series_obj[2:5]


# In[19]:


series_obj < 5

# In[ ]:



