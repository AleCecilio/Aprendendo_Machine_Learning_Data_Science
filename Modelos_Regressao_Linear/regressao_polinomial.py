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