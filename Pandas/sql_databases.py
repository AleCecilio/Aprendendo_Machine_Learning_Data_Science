import pandas as pd
import numpy as np

from sqlalchemy import create_engine

temp_db = create_engine('sqlite:///:memory:')

df = pd.DataFrame(data=np.random.randint(low=0, high=100, size=(4,4)), columns=['a','b','c','d'])
print(df,'\n')

df.to_sql(name='new_table',con=temp_db,if_exists='replace', index=False)

result = pd.read_sql_query(sql='SELECT a,c FROM new_table', con=temp_db)
print(result,'\n')
