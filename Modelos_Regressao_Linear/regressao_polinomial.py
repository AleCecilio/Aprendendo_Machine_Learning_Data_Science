import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Arquivos/Advertising.csv')

X = df.drop(columns=['sales'])
Y = df['sales']

from sklearn.preprocessing import PolynomialFeatures

polynomial_converter = PolynomialFeatures(degree=2, include_bias=False)
polynomial_converter.fit(X)
poly_features = polynomial_converter.transform(X)

print('\n', poly_features)
print('\n', poly_features.shape)
print('\n', X.iloc[0])
print('\n', poly_features[0])

print('\n', polynomial_converter.fit_transform(X))

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(poly_features, Y, test_size=0.3, random_state=101)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)
test_predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error
MAE = mean_absolute_error(Y_test, test_predictions)
MSE = mean_squared_error(Y_test, test_predictions) 
RMSE = np.sqrt(MSE)

print(f'\nMAE: {MAE}')
print(f'RMSE: {RMSE}')

print('\nCoefficients:', model.coef_)
print('\n', poly_features[0])
print('\n', X.iloc[0])