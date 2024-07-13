#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install langchain


# In[2]:


pip install langchain_experimental


# In[4]:


pip show langchain


# In[16]:


pip install OpenAI


# In[61]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from getpass import getpass

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent


# In[13]:


OPENAI_API_KEY = getpass("Enter API:")
os.environ['OPENAI_API_KEY'] = gpt_api_key


# In[14]:


# Read data from CSV file
data = pd.read_csv('/Users/mythilimoparthi/Downloads/healthcare_dataset.csv')


# In[21]:


# Create agent
agent = create_pandas_dataframe_agent(OpenAI(temperature=0),data, verbose=True,allow_dangerous_code=True)


# In[22]:


x=data.columns
print(x)
y=data.shape
print(y)


# In[23]:


openai = OpenAI(temperature = 0.0)


# In[24]:


openai.model_name


# In[54]:


query = "total no of rows in the data"
result = agent(query)


# In[55]:


query = "toatl attributes in the data"
result = agent(query)


# In[56]:


data.shape


# In[57]:


query = "Are there any missing values in dataset"
result = agent(query)


# In[58]:


query = "What are the different attributes"
result = agent(query)


# In[65]:


query = "visualize a bar plot for Gender and Age"
result = agent(query)


# In[ ]:


query = "visualize a scatterplot for Insurance Provider and Hospital"
result = agent(query)


# In[53]:


# Store the response in a memory (list in this case)
results = []
results.append({
    "query": query,
    "response": response
})

# Print the stored results (optional)
print("Stored Results:")
for result in results:
    print(f"Query: {result['query']}")
    print(f"Response: {result['response']}")
    print("---")


# In[ ]:




