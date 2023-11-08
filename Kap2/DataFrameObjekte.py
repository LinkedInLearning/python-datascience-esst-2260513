#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# In[9]:


np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),index=['row 1','row 2','row 3','row 4','row 5','row 6'],
                  columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
DF_obj

# In[ ]:



