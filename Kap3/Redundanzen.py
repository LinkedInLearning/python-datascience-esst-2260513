#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# In[2]:


DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})
DF_obj

# In[3]:


series_obj = Series([1,2,2,3,1,4,2,3,1])
series_obj

# In[4]:


series_obj.duplicated()

# In[5]:


DF_obj.duplicated()

# In[10]:


series_obj.drop_duplicates()


# In[14]:


DF_obj.drop_duplicates()

# In[ ]:




# In[ ]:



