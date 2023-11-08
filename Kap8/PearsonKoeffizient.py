#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr

# In[40]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars

# In[41]:


cars.corr()

# In[42]:


sb.pairplot(cars)

# In[43]:


X = cars[['mpg','cyl']]

# In[44]:


X

# In[45]:


sb.pairplot(X)

# In[46]:


X.corr()

# In[47]:


R, p_value = pearsonr(cars['mpg'],cars['cyl'])

# In[48]:


print(R)

# In[49]:


print(p_value)

# In[ ]:



