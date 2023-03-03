#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[49]:


n = input()
j = input().split()
r = input()
k = input().split()
stock=[]
request=[]

for i in range (int(n)):
    if j[i][-1] == 'S':
        stock.append(-len(j[i]))
    elif j[i][-1] == 'M':
        stock.append(0)
    elif j[i][-1] == 'L':
        stock.append(len(j[i]))

stock.sort()

for i in range (int(r)):
    if k[i][-1] == 'S':
        request.append(-len(k[i]))
    elif k[i][-1] == 'M':
        request.append(0)
    elif k[i][-1] == 'L':
        request.append(len(k[i]))

request.sort()

p = 1
for l in range(int(r)):
    if stock[l] < request[l]:
        p = 0

if (p==1):
    print("Yes")
else:
    print("No")


# In[ ]:




