#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[29]:


rcParams['figure.figsize'] = 15,3
sb.set_style('whitegrid')

# In[30]:


x = [66,42,13]
plt.pie(x)
plt.savefig('diagramm.png',format='png')
plt.savefig('diagramm.svg',format='svg')


# In[ ]:



