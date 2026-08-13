import pandas as pd
from sqlalchemy import create_engine, text

usuario = "root"
senha = "CaliceSagrado1979!"
host = "localhost"      
banco = "PythonDB"

engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}")

with engine.begin() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {banco}"))
    conn.execute(text(f"USE {banco}"))

engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS Clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            idade INT
        )
    """))
    conn.execute(text("INSERT INTO Clientes (nome, idade) VALUES ('Fulano', 21)"))

df = pd.read_sql("SELECT * FROM Clientes", con=engine)
print(df,'\n')
