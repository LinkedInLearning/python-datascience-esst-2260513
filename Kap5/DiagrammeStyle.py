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


x = range(1,10)
y = [1,2,3,11,4,7,1,2,5]
wide=[0.5,0.5,1,1,0.5,1,1,0.5,2]
plt.bar(x,y, color=['red'], width=wide, align='center')

# In[ ]:



