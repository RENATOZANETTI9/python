import pandas as pd
dados = pd.read_excel('arquivo1.xlsx', engine='openpyxl')
print(dados)
#dados.head(1000)