#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# In[3]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
cars

# In[5]:


carb = cars.carb
carb.value_counts()

# In[6]:


cars_cat = cars[['cyl','vs','am','gear','carb']]
cars_cat.head()


# In[7]:


gears_group = cars_cat.groupby('gear')
gears_group.describe()

# In[ ]:




# In[ ]:



