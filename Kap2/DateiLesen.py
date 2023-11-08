#!/usr/bin/env python
# coding: utf-8

# In[1]:


fobj = open("mpython.txt")
for line in fobj:
    print(line.rstrip())
fobj.close()

# In[ ]:



