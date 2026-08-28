import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error

df = pd.read_csv('Arquivos/Advertising.csv')

X = df.drop(columns=['sales'])
y = df['sales']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

base_elastic_net_model = ElasticNet()

param_grid = {
    'alpha': [0.1, 1, 5, 10, 50, 100],
    'l1_ratio': [.1,.5,.7,.95,.99,1]
}

grid_model = GridSearchCV(
    estimator=base_elastic_net_model,
    param_grid=param_grid,
    scoring='neg_mean_squared_error',
    cv=5,
    verbose=2
)

grid_model.fit(X_train_scaled, y_train)

print('\nMelhores parâmetros: ', grid_model.best_estimator_)
print('\nResultados da busca em grade: ', pd.DataFrame(grid_model.cv_results_))

y_predc = grid_model.predict(X_test_scaled)

print('\nMSE: ', mean_squared_error(y_test, y_predc))
