#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
from mlxtend.plotting import plot_decision_regions
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


df = pd.read_csv('/Users/lichiaoyu/Downloads/heart copy.csv')


# In[15]:


df.head()


# In[16]:


df.info()


# In[17]:


df.describe()


# In[18]:


df.isnull().sum()


# In[19]:


df.hist(figsize = (20,20),color='#008631')
plt.tight_layout()
plt.show()


# In[25]:


Hdislabel = ['Have heart disease','Do not have heart disease']
val_counts = [508,409] 
fig = px.pie(values=val_counts,names=Hdislabel,
             color=Hdislabel,
             color_discrete_map={'Have heart disease':'red',
                                 'Do not have heart disease':'#008631'},
             title='Heart disease count')

fig.show()


# In[27]:


plt.figure(figsize=(10,10))
from pandas.plotting import scatter_matrix
p=scatter_matrix(df,figsize=(25, 25))


# In[28]:


plt.figure(figsize = (10, 10))
sns.heatmap(df.corr(),annot=True)
plt.title('Fig: Annoted values of correlation coefficient of each pair of features', y=-0.23)


# In[31]:


X = df.drop('output',axis=1)
Y = df['output']


# In[38]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)


# In[39]:


from sklearn.naive_bayes import GaussianNB


# In[40]:


gaussNB = GaussianNB()


# In[44]:


# Train the model
gaussNB.fit(X_train,Y_train)


# In[45]:


Y_pred_nb = gaussNB.predict(X_test)


# In[46]:


print('The value of accuracy score is ',accuracy_score(Y_test,Y_pred_nb))


# In[ ]:




