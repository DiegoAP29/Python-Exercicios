import pandas as pd

import plotly.express as px

import time

tabela = pd.read_csv("arquivos_python_exercícios/python_análise_de_dados/arquivos_csv/rh_funcionarios.csv")

tabela = tabela.sort_values(by = "salario", ascending = False)
#organiza pelo salário, no topo os maiores e vai descendo

print(tabela)
time.sleep(5)

media_salarial_p_departamento = tabela.groupby('departamento')['salario'].mean().round(2)
print('\033[34mMedia salarial por departamento\033[m')
print(media_salarial_p_departamento)
time.sleep(5)

#essas duas médias pegam o groupby separando o criterio que vai separar em grupos pelos ()
#definem um segundo critério e decide oque fazer com esse 2 critério relacionado ao grupo

media_aval = tabela.groupby('departamento')['avaliacao'].mean().round(2)
print('\033[34mMédia de avaliação por departamento: \033[m')
print(media_aval)
time.sleep(5)

max_salario = tabela['salario'].max()
min_salario = tabela['salario'].min()
#separa salarios minimo e maximo entre os dados
print(f'\033[34mMenor salário é R${min_salario}:.2f\033[m')
print(f'\033[34mMaior salário é R${max_salario}:.2f\033[m')
time.sleep(5)

grafico1 = px.scatter(tabela , x = 'anos_empresa' , y = 'salario' , color = 'departamento', title = 'salário por anos de trabalho')

grafico2 = px.bar(tabela , x = 'departamento', y = 'avaliacao', color = 'avaliacao', title= 'média de desempenho por setor')

grafico3 = px.box(tabela, x = 'departamento', y = 'salario', color = 'departamento', title = 'Distribuição e Variação Salarial por Departamento')

#grafico1 - gráfico de dispersão entre o salário e os anos de empresa da pessoa
#grafico2 - gráfico de barra que relaciona o departamento com as avaliações dos funcionários
#grafico3 - gráfico de dispersão salarial por setor

grafico1.show()
time.sleep(5)
grafico2.show()
time.sleep(5)
grafico3.show()
