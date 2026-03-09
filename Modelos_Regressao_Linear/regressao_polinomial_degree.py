import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# from sklearn.pipeline import Pipeline
from joblib import dump, load

df = pd.read_csv('Arquivos/Advertising.csv')

X = df.drop(columns=['sales'])
Y = df['sales']

train_rmse_errors = []
test_rmse_errors = []


for d in range(1, 10):
    poly_converter = PolynomialFeatures(degree=d, include_bias=False)
    poly_features = poly_converter.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(
        poly_features, Y, test_size=0.3, random_state=101
    )

    model = LinearRegression()
    model.fit(X_train, Y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_rmse = np.sqrt(mean_squared_error(Y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(Y_test, test_pred))

    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)


print(f'\nTrain RMSE Errors: {train_rmse_errors}')
print(f'\nTest RMSE Errors: {test_rmse_errors}')

plt.plot(range(1,6), train_rmse_errors[:5], label='Train RMSE')
plt.plot(range(1,6), test_rmse_errors[:5], label='Test RMSE')
plt.xlabel('Degree of Polynomial')
plt.ylabel('RMSE')
plt.legend()
plt.show()

# Se observa que o erro de teste diminui até o grau 3,
# mas depois começa a aumentar, indicando overfitting. 
# O modelo com grau 3  ou 2 são os mais adequados para este conjunto de dados.

campaign = [[149, 22, 12]]

final_poly_converter = PolynomialFeatures(degree=3, include_bias=False)
full_converted_X = final_poly_converter.fit_transform(X)
final_model = LinearRegression()
final_model.fit(full_converted_X, Y)

dump(final_model, 'Modelos/final_poly_model.joblib')
dump(final_poly_converter, 'Modelos/final_poly_converter.joblib') 

loaded_model = load('Modelos/final_poly_model.joblib')
loaded_converter = load('Modelos/final_poly_converter.joblib')


transformed_data = loaded_converter.fit_transform(campaign)

prediction = loaded_model.predict(transformed_data)[0]


# Esse foi o exemplo de deploy do curso.
# Porém exite um maneira mais simples de fazer isso utilizando o pipeline.

'''
pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=3, include_bias=False)),
    ('model', LinearRegression())
])

pipeline.fit(X, Y)

os.makedirs('Modelos', exist_ok=True)

dump(pipeline,'Modelos/poly_model_pipeline.joblib')

model = load('Modelos/poly_model_pipeline.joblib')
prediction = model.predict(campaign)[0]
'''

print(f'\nPredicted Sales for Campaign: {prediction:.2f}')