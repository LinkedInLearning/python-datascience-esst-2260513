#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame



# In[2]:


address = 'mtcars.csv'
cars = pd.read_csv(address)

cars.head()

# In[3]:


cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# In[5]:


cars.head(2)

# In[ ]:



