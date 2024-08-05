#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas  
import matplotlib.pyplot as plt 
import seaborn as sns 
get_ipython().run_line_magic('', 'matplotlib inline')


# In[4]:


data=pandas.read_csv('HR_comma_sep.csv')


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.info()


# In[8]:


left = data.groupby('left')
left.mean()


# In[9]:


data.describe()


# In[31]:


left_count = data.groupby('left').count()
bars = plt.bar(left_count.index.values, left_count['satisfaction_level'], color=['blue', 'red'])
plt.xlabel('Employees')
plt.ylabel('Number of Employees')

for i, value in enumerate(left_count['satisfaction_level']):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.legend(bars, ['Stayed', 'Left'])
plt.show()


# In[11]:


data.left.value_counts()


# In[34]:


num_projects = data.groupby('number_project').count()

bars = plt.bar(num_projects.index.values, num_projects['satisfaction_level'], color='skyblue')

plt.xlabel('Number of Projects')
plt.ylabel('Number of Employees')
plt.title('Distribution of Employees by Number of Projects')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), 
             ha='center', va='bottom', color='black')
plt.show()


# In[35]:


time_spent = data.groupby('time_spend_company').count()

bars = plt.bar(time_spent.index.values, time_spent['satisfaction_level'], color='lightgreen')

plt.xlabel('Number of Years Spent in Company')
plt.ylabel('Number of Employees')
plt.title('Distribution of Employees by Years Spent in Company')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), 
             ha='center', va='bottom', color='black')
plt.show()


# In[41]:


features = ['number_project', 'time_spend_company', 'Work_accident', 'left', 'promotion_last_5years', 'Department', 'salary']

fig, axes = plt.subplots(4, 2, figsize=(15, 20))

axes = axes.flatten()

for i, feature in enumerate(features):
    sns.countplot(x=feature, data=data, ax=axes[i])
    axes[i].set_xlabel(feature.capitalize())  
    axes[i].set_ylabel('Number of Employees')  
    axes[i].set_title(f'Distribution of Employees by {feature.capitalize()}')  
    axes[i].tick_params(axis='x', rotation=45)  
plt.tight_layout()
plt.show()


# In[37]:


features = ['number_project', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'Department', 'salary']

fig, axes = plt.subplots(3, 2, figsize=(15, 20))

axes = axes.flatten()

for i, feature in enumerate(features):
    sns.countplot(x=feature, data=data, hue='left', ax=axes[i])
    axes[i].set_xlabel(feature.capitalize()) 
    axes[i].set_ylabel('Number of Employees') 
    axes[i].set_title(f'Distribution of Employees by {feature.capitalize()}')  
    axes[i].tick_params(axis='x', rotation=45)  

plt.tight_layout()

plt.show()


# In[19]:


correlation_matrix = data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


# In[39]:


sns.set(style="whitegrid")

plt.figure(figsize=(10, 8))

sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette="viridis")

plt.xlabel('Importance', fontsize=14)
plt.ylabel('Feature', fontsize=14)
plt.title('Feature Importance', fontsize=16)

for index, value in enumerate(feature_importance_df['Importance']):
    plt.text(value, index, f'{value:.2f}', fontsize=12, va='center')

plt.show()


# In[40]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("F1 Score:", f1)


# In[ ]:




