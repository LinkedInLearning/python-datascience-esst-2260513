#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# In[2]:


missing = np.nan
series_obj = Series(['row 1', 'row 2',missing,'row 4','row 5','row 6',np.nan,'row 8'])
series_obj

# In[3]:


series_obj.isnull()
