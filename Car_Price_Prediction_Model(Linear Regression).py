#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('car data.csv')
df.head()


# In[2]:


print(df.shape) #print shape of the dataset


# In[3]:


#Count Null values
total_na = df.isna().sum().sum()
print(total_na)


# In[4]:


sns.boxplot(df['Selling_Price'])


# In[6]:


car_groups = df.groupby('Fuel_Type')['Selling_Price']
price_stats = car_groups.agg(['mean', 'median', 'count','std'])
print(price_stats)


# In[7]:


# Bar chart of mean prices
plt.figure(figsize=(6, 4))
plt.bar(price_stats.index, price_stats['mean'])
plt.xlabel('Fuel')
plt.ylabel('Mean Price')
plt.title('Mean Price by Number of Bedrooms')
plt.show()


# In[9]:


#barplot using saeborn
sns.barplot(data=df, x="Year", y="Selling_Price", hue="Fuel_Type")
plt.xlabel("Year")
plt.ylabel("Selling Price")
plt.xticks(rotation=90)
plt.show()


# In[32]:


# Create a DataFrame subset with the selected columns
subset = df[['Selling_Price', 'Present_Price', 'Year']]

# Calculate the correlation matrix for the selected columns
correlation_matrix = subset.corr()

# Create a heatmap to visualize the correlations
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[15]:


# Scatter plot
fig, ax = plt.subplots(figsize = (6,4))
ax.scatter(df['Selling_Price'],df['Present_Price'])

# x-axis label
ax.set_xlabel('(Selling Price)')

# y-axis label
ax.set_ylabel('(Present_Price)')
plt.show()


# In[17]:


df['Car_Name'].unique()


# In[18]:


df['Year'].unique()


# In[19]:


df['Selling_Price'].unique()


# In[20]:


df['Present_Price'].unique()


# In[21]:


df['Kms_Driven'].unique()


# In[22]:


df['Fuel_Type'].unique()


# In[23]:


df['Seller_Type'].unique()


# In[24]:


df['Transmission'].unique()


# In[25]:


df['Owner'].unique()


# In[33]:


petrol_data = df.groupby('Fuel_Type').get_group('Petrol')
petrol_data.describe()


# In[37]:


seller_data = df.groupby('Seller_Type').get_group('Dealer')
seller_data.describe()


# In[40]:


#manual encoding
df.replace({'Fuel_Type':{'Petrol':0, 'Diesel':1, 'CNG':2}}, inplace=True)
#one hot encoding
df = pd.get_dummies(df, columns=['Seller_Type', 'Transmission'], drop_first=True)


# In[41]:


X = df.drop(['Car_Name','Selling_Price'], axis=1)
y = df['Selling_Price']


# In[42]:


print("Shape of X is: ",X.shape)
print("Shape of y is: ", y.shape)


# In[43]:


#Split Train Set and Test Set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)


# In[44]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[45]:


#training the model using linear regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)


# In[46]:


#Making prediction
y_pred = model.predict(X_test)


# In[47]:


from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2) Score:", r2)


# In[49]:


sns.regplot(x=y_pred, y=y_test)
plt.xlabel("Predicted Price")
plt.ylabel('Actual Price')
plt.title("ACtual vs predicted price")
plt.show()


# In[ ]:




