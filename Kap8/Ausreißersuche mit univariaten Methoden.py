#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

# In[15]:


df = pd.read_csv(
    filepath_or_buffer='iris.data.csv',
    header=None,
    sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
df

# In[28]:


df.boxplot(return_type='dict')
plt.plot()

# In[39]:


df[df.iloc[:,1] > 4]

# In[40]:


df[df.iloc[:,1] < 2.05]

# In[41]:


df.describe()

# In[43]:


df[df.iloc[:,1] > 4].describe()

# In[ ]:



