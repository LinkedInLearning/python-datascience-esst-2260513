#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[4]:


rcParams['figure.figsize'] = 15,3
sb.set_style('whitegrid')

# In[5]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
DF_obj = DataFrame(cars)
DF_obj

# In[15]:


x = range(1,10)
y = [1,2,3,11,4,7,1,2,5]
plt.bar(x,y)

# In[16]:


DF_obj.plot(kind='bar')

# In[18]:


DF_obj.plot(kind='barh')

# In[19]:


df = DF_obj[['mpg','wt','cyl']]

# In[20]:


df.plot(kind='bar')

# In[21]:


df.plot(kind='barh')

# In[ ]:



