import pandas as pd

import plotly.express as px

import seaborn as sns

import numpy as np

import matplotlib.pyplot as plt

tabela = pd.read_csv('python_análise_de_dados/arquivos_csv/vendas_sazonais.csv')

classificacao_faturamento = np.where(tabela['faturamento'] > 6000 , 'Alto', 'Padrão')
#cria usando numpy uma condição, assim como o query porem usando arrays, funcionando de forma mais rápida


tabela['classificacao_faturamento'] = classificacao_faturamento
#cria uma nova coluna

matriz_correlacao = tabela[['faturamento', 'desconto_aplicado']].corr()
#cria uma matriz correlacionando o faturamento com o desconto aplicado

sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm')
# o seaborn cria um mapa de calor e por ser relacionado ao matlib, o heatmap que será ativo
#será o exibido no plt.show()



plt.show()

resumo_vendas = tabela.groupby('classificacao_faturamento')['faturamento'].agg(['count','mean','sum'])
#tira o número de cada grupo, a média e a soma total

print(resumo_vendas)
