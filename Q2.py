#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = input()
allValid = 1
record = []
errorCodes = []
for i in range(int(n)):
    record.append(input().split())

for i in range(int(n)):
    if len(record[i])==3:
        errorCodes.append(record[i][2])
        allValid = 0

s = " "
err = s.join(errorCodes)
     
if allValid == 1:
    print ("Yes")
else:
    print ("No")
    print (err)
        


# In[ ]:




