#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


#getting our data set into IDe
database = 'C:/Users/User/Downloads/Advertising.csv'

#reading our data
df = pd.read_csv(database)

#getting a look at our data
df.head()


# In[19]:


#creating a data frame to store the first 15 
data_new = df.head(40)


# In[20]:


data_new


# In[22]:


#ploting the graph
plt.scatter(data_new.Newspaper, data_new.Sales)

#adding axis
plt.xlabel('Newspaper')
plt.ylabel('Sales')
plt.title('This is my first simple data plotting in python')
plt.show()


# In[ ]:





# In[ ]:




