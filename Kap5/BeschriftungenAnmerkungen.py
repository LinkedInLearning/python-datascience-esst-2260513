#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# In[2]:


rcParams['figure.figsize'] = 8,4
sb.set_style('whitegrid')

# In[5]:


x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]

plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.bar(x,y)

# In[32]:


verteilung = ['a', 'b','c', 'de', 'e', 'f','g','h','i']
plt.pie(y, labels=verteilung)
plt.legend(verteilung, loc='right')
plt.show()

# In[18]:


address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.cyl

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])

mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Anzahl Zylinder in mtcars')

ax.set_xlabel('Name des Autos')
ax.set_ylabel('Zylinder')
ax.legend(loc='best')


# In[ ]:




# In[38]:


fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_title('Anzahl Zylinder in mtcars')
ax.set_ylabel('Zylinder')

ax.set_ylim([0,15])

ax.annotate('Toyota Corolla', xy=(19,8), xytext = (23,10),
           arrowprops=dict(facecolor='black', shrink=0.05))

# In[ ]:



