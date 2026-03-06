import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Arquivos/Advertising.csv')

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(df['TV'], df['sales'], 'o')
axes[0].set_title('TV Spend')
axes[0].set_ylabel('Sales')


axes[1].plot(df['radio'], df['sales'], 'o')
axes[1].set_title('Radio Spend')
axes[1].set_ylabel('Sales')

axes[2].plot(df['newspaper'], df['sales'], 'o')         
axes[2].set_title('Newspaper Spend')
axes[2].set_ylabel('Sales')

plt.tight_layout()
plt.show()


sns.pairplot(df)
plt.show()

X = df.drop(columns=['sales'])
Y = df['sales']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)


from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train, Y_train)
test_predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

print('\nMean Sales:', df['sales'].mean())

sns.histplot(data=df, x='sales', bins=20)
plt.show()

# MAE
print('\nMean Absolute Error:', mean_absolute_error(Y_test, test_predictions))

# RMSE
print('\nRoot Mean Squared Error:', np.sqrt(mean_squared_error(Y_test, test_predictions)))  


final_model = LinearRegression()
final_model.fit(X, Y)
print('\nCoefficients:', final_model.coef_)


y_hat = final_model.predict(X)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(df['TV'], df['sales'], 'o')
axes[0].plot(df['TV'], y_hat, 'o', color='red')
axes[0].set_title('TV Spend')
axes[0].set_ylabel('Sales')


axes[1].plot(df['radio'], df['sales'], 'o')
axes[1].plot(df['radio'], y_hat, 'o', color='red')
axes[1].set_title('Radio Spend')
axes[1].set_ylabel('Sales')

axes[2].plot(df['newspaper'], df['sales'], 'o')    
axes[2].plot(df['newspaper'], y_hat, 'o', color='red')     
axes[2].set_title('Newspaper Spend')
axes[2].set_ylabel('Sales')

plt.tight_layout()
plt.show()

from joblib import dump, load

dump(final_model, 'Modelos/final_sales_model.joblib')

loaded_model = load('Modelos/final_sales_model.joblib')

print(X.shape)

# 149 TV, 22 radio, 12.5 newspaper
# Sales? 
campaign = [[149, 22., 12.5]]

print(loaded_model.predict(campaign))