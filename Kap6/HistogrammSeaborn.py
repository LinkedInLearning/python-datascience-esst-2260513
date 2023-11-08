#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

# In[9]:


rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

# In[10]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
cars

# In[11]:


cyl = cars['cyl']
gear = cars['gear']
sb.distplot(cyl)

# In[12]:


sb.distplot(gear)

# In[ ]:



