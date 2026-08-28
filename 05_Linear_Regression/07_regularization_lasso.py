import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv('Arquivos/Advertising.csv')

X = df.drop(columns=['sales'])
y = df['sales']

poly_converter = PolynomialFeatures(degree=3, include_bias=False)
poly_features = poly_converter.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    poly_features, y, test_size=0.3, random_state=101
)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

lasso_cv_model = LassoCV(eps=0.1, alphas=100, cv=5, max_iter=1000000 ) 
lasso_cv_model.fit(X_train, y_train)
print(f'\nOptimal alpha (LassoCV): {lasso_cv_model.alpha_}')

test_predictions = lasso_cv_model.predict(X_test)

MAE = mean_absolute_error(y_test, test_predictions)
print(f'\nMAE: {MAE}')

RMSE = np.sqrt(mean_squared_error(y_test, test_predictions))
print(f'\nRMSE: {RMSE}')

print(f'\nCoefficients (LassoCV): {lasso_cv_model.coef_}')
