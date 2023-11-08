#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

# In[15]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

cars.head()

# In[3]:


cars.sum()

# In[4]:


cars['mpg'].sum()

# In[5]:


cars.sum(axis=1)

# In[6]:


cars.mean()

# In[7]:


cars.median()

# In[8]:


cars.median(axis=1)

# In[9]:


cars.max()

# In[10]:


cars.min()

# In[13]:


cars['mpg'].idxmax()

# In[16]:


cars.std()

# In[17]:


cars.var()

# In[19]:


cars['gear'].value_counts()

# In[20]:


cars.describe()

# In[ ]:



