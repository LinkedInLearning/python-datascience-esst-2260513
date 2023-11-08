#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# In[75]:


data = {'Fahrzeug': ['Auto', 'Motorrad', 'Motorrad', 'Auto', 'Auto'],  'PS': [380, 70, 124, 165,156]}
DF_obj = pd.DataFrame(data)
DF_obj

# In[78]:


gr=DF_obj.groupby(['Fahrzeug'])
gr.mean()

# In[79]:


gr.sum()

# In[80]:


gr.min()

# In[ ]:



