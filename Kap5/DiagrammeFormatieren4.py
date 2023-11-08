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

# In[24]:


x1 = range(1,10)
y1 = [1,2,3,1,4,17,1,2,5]
x2 = range(1,10)
y2 = [4,2,4,3,6,3,11,2,1]

plt.plot(x1,y1, drawstyle='steps', lw=5)
plt.plot(x2,y2, marker='o', mew=10)

# In[ ]:




# In[ ]:



