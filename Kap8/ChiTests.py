#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency

# In[7]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

# In[8]:


table = pd.crosstab(cars['cyl'], cars['am'])
table

# In[9]:


chi2_contingency(table.values)

# In[10]:


table2 = pd.crosstab(cars['cyl'], cars['gear'])
table2

# In[11]:


chi2_contingency(table2.values)

# In[12]:


table3 = pd.crosstab(cars['cyl'], cars['vs'])
table3

# In[13]:


chi2_contingency(table3.values)

# In[ ]:



