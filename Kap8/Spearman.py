#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr

# In[2]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

# In[3]:


X = cars[['cyl', 'vs', 'am', 'gear']]
sb.pairplot(X)

# In[4]:


print(spearmanr(cars['cyl'],cars['vs']))

# In[5]:


print(spearmanr(cars['am'],cars['gear']))

# In[ ]:



