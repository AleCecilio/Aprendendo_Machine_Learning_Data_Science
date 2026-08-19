import pandas as pd

df = pd.read_excel('Pandas/Arquivos/my_excel_file.xlsx')
wb = pd.ExcelFile('Pandas/Arquivos/my_excel_file.xlsx')
excel_sheet_dict = pd.read_excel('Pandas/Arquivos/my_excel_file.xlsx', sheet_name=None)
print(df,'\n')
print(wb.sheet_names,'\n')
print(type(excel_sheet_dict),'\n')
print(excel_sheet_dict.keys(),'\n')
print(excel_sheet_dict['First_Sheet'],'\n')

our_df = excel_sheet_dict['First_Sheet']
our_df.to_excel('Pandas/Arquivos/example.xlsx',sheet_name='First_Sheet',index=False)
