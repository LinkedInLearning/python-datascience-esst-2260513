#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

# In[2]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# In[3]:


cars[['mpg']].plot()

# In[4]:


cars[['mpg']].describe()

# In[5]:


cars[['mpg']]

# In[6]:


scaled = preprocessing.MinMaxScaler()

# In[7]:


scaled_mpg=scaled.fit_transform(cars[['mpg']])

# In[8]:


plt.plot(scaled_mpg)

# In[10]:


st_mpg=scale(cars[['mpg']], axis=0, with_mean=False, with_std=False)

# In[11]:


plt.plot(st_mpg)

# In[12]:


st_mpg=scale(cars[['mpg']], axis=0, with_mean=False, with_std=True)

# In[13]:


plt.plot(st_mpg)

# In[14]:


st_mpg=scale(cars[['mpg']], axis=0, with_mean=True, with_std=True)

# In[15]:


plt.plot(st_mpg)

# In[ ]:



