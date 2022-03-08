#importar o pandas
import pandas as pd

# importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar base de dados
pd.set_option('display.max.column', None)
print(tabela_vendas)

# faturamento por loja
# total vendido por loja
# ticket médio por produto
# enviar e-mail


