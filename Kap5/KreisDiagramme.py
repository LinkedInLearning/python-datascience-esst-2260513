#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[3]:


rcParams['figure.figsize'] = 15,3
sb.set_style('whitegrid')

# In[11]:


x = [2,3,1,5,6, 0.9]
plt.pie(x)
plt.show()

# In[ ]:



