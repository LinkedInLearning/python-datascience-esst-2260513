#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb


# In[ ]:


rcParams['figure.figsize'] = 15,3
sb.set_style('whitegrid')

# In[26]:


x = np.array(['2020-07-10','2020-07-11','2020-07-12','2020-07-13', '2020-07-14', '2020-07-15'], dtype='datetime64')
y = np.random.randint(100, size=x.shape)
plt.plot(x,y)

# In[ ]:



