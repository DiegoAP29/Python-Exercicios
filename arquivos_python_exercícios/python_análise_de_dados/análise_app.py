import pandas as pd

import plotly.express as px

import time

tabela = pd.read_csv("python_análise_de_dados/arquivos_csv/avaliacoes_app.csv")

print(tabela['plano'].value_counts())
#mostra a quantidade de cada plano, o value_counts() mostra a quantidade de cada item na coluna
time.sleep(5)

print(tabela.query('nota <= 2'))
#mostra as pessoas que deram nota menor ou igual a 2, o query() é usado para fazer uma consulta na tabela
time.sleep(5)

tabela_cruzada = pd.crosstab(tabela['plano'], tabela['nota'])
print(tabela_cruzada)
time.sleep(5)
#mostra a tabela cruzada com a contagem de cada combinação de plano e nota

grafico1 = px.bar(tabela, x = 'horas_uso_semana', y = 'plataforma', color= 'plano', title = 'Horas de uso por semana por plataforma e plano')
grafico2 = px.box(tabela, x = 'plano', y = 'horas_uso_semana', color = 'plano', title = 'Distribuição de horas de uso por semana por plano')   
#grafico1 - gráfico de barra que relaciona as horas de uso por semana com a plataforma e o plano do usuário
#grafico2 - gráfico de caixa que mostra a distribuição de horas de uso por semana para cada plano


grafico1.show()
time.sleep(5)
grafico2.show()