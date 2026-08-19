import pandas as pd
import requests
from io import StringIO

url = 'https://en.wikipedia.org/wiki/World_population' 
# ou 'Pandas/Arquivos/wikipedia_World_population.html'
# nesse caso bastaria ler a url normalmente com pd.read_html(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0"
}

res = requests.get(url, headers=headers)

tables = pd.read_html(StringIO(res.text)) 
print(len(tables),'\n')

print(tables[6],'\n')  

tables[6].to_html('Pandas/Arquivos/sample_table.html', index=False)