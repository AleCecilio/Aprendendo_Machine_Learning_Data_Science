import numpy as np
import pandas as pd

hotels = pd.read_csv('Pandas/Arquivos/hotel_booking_data.csv')

print(hotels.head(),'\n')

# Mostra o total de reservas no DataFrame
print(len(hotels.index),'\n')

# Mostra a quantidade de valores nulos por coluna
print(hotels.isnull().sum(),'\n')

# Remove a coluna 'company' do DataFrame (se existir)
hotels.drop('company', axis=1, inplace=True, errors='ignore')

# Mostra os 5 países com mais reservas
print(hotels['country'].value_counts().head(5),'\n')

# Mostra o hotel com a maior tarifa diária (adr) e o nome do hotel
print(hotels.loc[hotels['adr'].idxmax(), ['adr','name']], '\n')

# Calcula e mostra a média da tarifa diária (adr) arredondada para 2 casas decimais
print(round(hotels['adr'].mean(),2),'\n')

# Calcula a soma das médias de noites em fim de semana e semana
print(
    hotels[['stays_in_weekend_nights','stays_in_week_nights']]
    .mean()
    .sum()
    .round(2),
    '\n'
)

# Calcula a média do faturamento total por reserva (adr * total de noites) arredondada
print(
    (
        hotels['adr'] 
        * (
            hotels['stays_in_weekend_nights']
            + hotels['stays_in_week_nights']
        )
    )
    .mean()
    .round(2),
    '\n'
)

# Mostra os hóspedes que fizeram 5 pedidos especiais, exibindo nome e email
print(
    hotels[
        hotels['total_of_special_requests'] == 5 
    ][['name','email']], 
    '\n'
)

# Calcula a porcentagem de hóspedes que já são repetidos
print(
    (hotels['is_repeated_guest'].sum() * 100 / len(hotels))
    .round(2),
    '\n'
)

# Mostra os 5 sobrenomes mais comuns entre os hóspedes
print(
    hotels['name']
    .str.split(' ')
    .str[-1]
    .value_counts()
    .head(5),
    '\n'
)

# Mostra os 5 hóspedes que reservaram mais crianças e bebês
print(
    hotels.assign(
        total_kids = hotels['children'] + hotels['babies']
    ).loc[
        lambda df: df['total_kids'].nlargest(5).index,
        ['name', 'adults', 'total_kids', 'babies', 'children']
    ],
    '\n'
)

# Mostra os 3 códigos de telefone mais comuns entre os hóspedes
print(
    hotels['phone-number']
    .str.split('-')
    .str[0]
    .value_counts()
    .head(3)
    .reset_index()
    .rename(columns={'phone-number': 'Code', 'count': 'Total_Count'}),
    '\n'
)

# Conta quantas reservas têm chegada entre o dia 1 e o dia 15 do mês
print(
    len(
        hotels[
            (hotels['arrival_date_day_of_month'] >= 1) 
            & (hotels['arrival_date_day_of_month'] <= 15) 
        ]
        .index
    ),
    '\n'
)

# Conta quantas chegadas ocorreram em cada dia, exibindo o total por dia da semana
print(
    hotels.assign(
        arrival_date = pd.to_datetime(
            hotels['arrival_date_year'].astype(str) + '-' +
            hotels['arrival_date_month'].astype(str) + '-' +
            hotels['arrival_date_day_of_month'].astype(str)
        )
    )['arrival_date']
    .dt.day_name()
    .value_counts(),
    '\n'
)