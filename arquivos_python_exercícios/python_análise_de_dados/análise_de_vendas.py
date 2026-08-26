import pandas as pd

import plotly.express as px

import time

tabela = pd.read_csv("python_análise_de_dados/arquivos_csv/vendas_loja.csv")

tabela['faturamento_total'] = tabela['quantidade'] * tabela['preco_unitario']
#cria tabela de faturamento total

faturamento_p_produto = tabela.groupby('produto')['faturamento_total'].sum()

faturamento_p_regiao = tabela.groupby('regiao')['faturamento_total'].sum()
#groupby separa por grupos, depois os [] pegam o valor do faturamento e somam de todos os
#que estao dentro dos grupos

total_linhas = len(tabela)

produtos_cancelados = tabela[tabela['status_entrega'] == 'Cancelado']
#separa uma lista com todos elementos da tabela que constam como cancelados

qtd_cancelados = len(produtos_cancelados)

taxa_cancelamento = qtd_cancelados/total_linhas
#pega as linhas q estao canceladas e divide pelo total pra dar a taxa de cancelamento

grafico = px.bar(tabela,x='produto', y='faturamento_total', title='faturamento total dos produtos')
grafico2 = px.bar(tabela,x='regiao', y='faturamento_total', title='faturamento total das regiões')
grafico3 = px.histogram(tabela, x='produto',color = 'regiao', title = 'produtos por regiao')
#cria os graficos de barra com eixo x e y

print(tabela)
time.sleep(7)
print(faturamento_p_produto)
time.sleep(7)
print(faturamento_p_regiao)
time.sleep(7)
print(f'taxa de cancelamento é igual a {(taxa_cancelamento * 100):.2f}%')
time.sleep(7)
grafico.show()
time.sleep(7)
grafico2.show()
time.sleep(7)
grafico3.show()

