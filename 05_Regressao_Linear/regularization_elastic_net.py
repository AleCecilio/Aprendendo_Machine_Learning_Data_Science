import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNetCV
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

elastic_model = ElasticNetCV(
    l1_ratio=[.1, .5, .7, .9, .95, .99, 1],
    eps=0.001,
    alphas=100,
    cv=5,
    max_iter=1000000
)

elastic_model.fit(X_train, y_train)

print(f'\nOptimal alpha (ElasticNetCV): {elastic_model.alpha_}')
print(f'\nOptimal l1_ratio (ElasticNetCV): {elastic_model.l1_ratio_}')

test_predictions = elastic_model.predict(X_test)
MAE = mean_absolute_error(y_test, test_predictions)
print(f'\nMAE: {MAE}')

RMSE = np.sqrt(mean_squared_error(y_test, test_predictions))
print(f'\nRMSE: {RMSE}')