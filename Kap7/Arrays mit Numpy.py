#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn

# In[2]:


np.set_printoptions(precision=2)

# In[3]:


a = np.array([1,2,3,4,5,6])

# In[4]:


a

# In[5]:


b = np.array([[10,20,30],[40,50,60]])

# In[6]:


b

# In[7]:


np.random.seed(25)
c = 36 * np.random.randn(6)

# In[8]:


c

# In[9]:


d = np.arange(1,35)

# In[10]:


d

# In[11]:


a * 10

# In[12]:


c + a

# In[13]:


c - a

# In[14]:


c * a

# In[15]:


c / a

# In[16]:


aa = np.array([[2.,4.,6.], [1.,3.,5.], [10.,20.,30.]])

# In[17]:


aa

# In[18]:


bb = np.array([[0.,1.,2.], [3.,4.,5.], [6.,7.,8.]])

# In[19]:


bb

# In[20]:


aa*bb

# In[21]:


np.dot(aa,bb)

# In[ ]:



