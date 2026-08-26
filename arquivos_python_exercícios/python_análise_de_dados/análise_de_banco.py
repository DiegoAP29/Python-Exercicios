import pandas as pd

import plotly.express as px

tabela = pd.read_csv("python_análise_de_dados/arquivos_csv/clientes_banco.csv")

#atribui a tabela, o banco de dados

print(tabela)
#mostra a tabela

print(tabela.info())
#mostra os dados que compoem a tabela

print(tabela.describe().round(1))
#mostra dados como media e desvio padrao, o arrendodar 1 é pra n dar muitas casas decimais



grafico = px.histogram(tabela,x="contatos_12_meses", color ="categoria")
#px.histogram cira uma tabela no modelo(tabela, x, y)
#colour = muda cor


grafico.show()
#mostra o gráfico


