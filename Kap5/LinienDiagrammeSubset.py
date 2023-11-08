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

# In[6]:


DF_obj.plot()

# In[8]:


df = DF_obj[['mpg','wt','cyl']]

# In[9]:


df.plot()

# In[ ]:



