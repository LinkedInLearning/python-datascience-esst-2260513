#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[10]:


rcParams['figure.figsize'] = 15,3
sb.set_style('whitegrid')

# In[19]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
DF_obj = DataFrame(cars)
DF_obj

# In[18]:


x = range(1,10)
y = [1,2,3,1,4,17,1,2,5]
plt.plot(x,y)

# In[20]:


DF_obj.plot()

# In[21]:


DF_obj['mpg'].plot()

# In[ ]:




# In[ ]:



