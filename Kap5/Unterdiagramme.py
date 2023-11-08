#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[25]:


a = range(1,10)
b = range(2,8)
c = [1,2,10,5,7,11]
fig=plt.figure()

# In[26]:


fig, (ax1,ax2,ax3) = plt.subplots(1,3)
ax1.plot(a)
ax2.plot(b)
ax3.set_ylim([1,12])
ax3.plot(c)


# In[ ]:



