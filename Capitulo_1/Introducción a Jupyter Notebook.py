#!/usr/bin/env python
# coding: utf-8

# In[1]:


3 + 234


# In[1]:


def fibo():
    prev, act = 0, 1
    yield prev
    yield act
    while True:
        prev, act = act, act + prev
        yield act


# In[12]:


fibo_sec = fibo()


# In[13]:


[next(fibo_sec) for x in range(10)]


# In[19]:


fibo_sec = fibo()


# In[ ]:





# In[20]:


fibo_valores = [next(fibo_sec) for x in range(30)]


# In[ ]:





# In[21]:


import matplotlib.pyplot as plt
plt.plot(fibo_valores)
plt.ylabel('Valores fibonacci')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[11]:


[next(fibo_sec) for x in range(10)]


# In[ ]:





# In[ ]:





# In[7]:


[next(fibo_sec) for x in range(10)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
hist, bins = np.histogram(x, bins=50)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)

py.iplot_mpl(fig17, strip_style = True)


# In[ ]:




