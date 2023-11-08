#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[39]:


x = range(1,10)
y = [1,2,3,1,4,7,1,2,5]
fig=plt.figure()
ax=fig.add_axes([0,0,2,0.5])
ax.set_ylim([1,10])
ax.set_xlim([1,9])
ax.set_xticks([1,2,5,9])
ax.set_yticks([1,3,5,7,9])
ax.grid()
ax.plot(x,y)


# In[ ]:



