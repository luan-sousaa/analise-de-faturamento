# percorrer todos os arquivos da pasta de vendas
import os
import pandas as pd
import plotly.express as px
diretorio_vendas = r"C:\Users\Luan\Downloads\Vendas"
lista_arquivo = os.listdir(diretorio_vendas)

tabela_total = pd.DataFrame()

# importas as bases de vendas

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        #  tratar/compilar
        caminho_arquivo = os.path.join(diretorio_vendas, arquivo)
        tabela = pd.read_csv(caminho_arquivo)
        tabela_total = tabela_total._append(tabela)

# calcular o produto mais vendido

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]]

# calcular o produto com mais faturamento

tabela_total['Faturamento'] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby('Produto').sum()

# calcular a loja/cidade que mais vendeu

tabela_lojas = tabela_total.groupby('Loja').sum()

#tabela/dashboard
grafico = px.bar(tabela_lojas,x=tabela_lojas.index , y= 'Faturamento')
grafico.show()



