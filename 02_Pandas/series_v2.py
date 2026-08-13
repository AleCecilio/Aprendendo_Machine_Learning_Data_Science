import numpy as np
import pandas as pd

q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

print(sales_q1)
print(sales_q2)
print(sales_q1.keys())
print(sales_q1 / 100)
print(sales_q1 + sales_q2)
print(sales_q1.add(sales_q2, fill_value=0))
