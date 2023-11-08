#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

# In[24]:


df = pd.read_csv(
    filepath_or_buffer='iris.data.csv',
    header=None,
    sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
df

# In[25]:


sb.boxplot(x='Species', y='Sepal Length', data=df)

# In[26]:


sb.boxplot(x='Species', y='Sepal Width', data=df)

# In[27]:


sb.boxplot(x='Species', y='Petal Length', data=df)

# In[28]:


sb.boxplot(x='Species', y='Petal Width', data=df)

# In[29]:


sb.pairplot(df,hue='Species')

# In[ ]:



