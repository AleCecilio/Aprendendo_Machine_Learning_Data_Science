import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Arquivos/Advertising.csv')

X = df.drop(columns=['sales'])
Y = df['sales']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)


from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train, Y_train)
test_predictions =model.predict(X_test)

test_residual = Y_test - test_predictions

print('\nTest Residuals:', test_residual)

sns.scatterplot(x=Y_test,y=test_residual)
plt.axhline(y=0, color='r', linestyle='--')
plt.show()

sns.displot(test_residual, bins=25, kde=True)
plt.show()

import scipy as sp

fig, axes = plt.subplots(figsize=(6,8), dpi=100)
_ = sp.stats.probplot(test_residual,plot=axes)
plt.show()