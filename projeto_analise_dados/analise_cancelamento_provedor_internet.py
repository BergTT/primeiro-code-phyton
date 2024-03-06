# Passo 1: Importar base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")

# Passo 2: Visualizar a base de dados
# excluindo coluna da base de dados desnecessária, se tiver mais de uma coluna a ser removida colocar em lista[]
tabela = tabela.drop(columns="CustomerID")

print(tabela)
# Passo 3: Corrigir base de dados
# valores vazios - erro de preenchimento
print(tabela.info())
tabela = tabela.dropna()  # dropna é pra tirar os nulos ou vazios
print(tabela.info())

# Passo 4: Analise dos cancelamentos

print(tabela["cancelou"].value_counts())
# Colocando para porcentagem, fala-se normalizar
print(tabela["cancelou"].value_counts(normalize=True))
# display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Analise da causa dos cancelamentos

import plotly.express as px

# Criar o grafico
# Para cada coluna da minha tabel
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    # Exibir o grafico
    grafico.show()

# Analise da causa dos cancelamentos

# Se o cliente ligar mais de 4 vezes deve resolver urgente o problema
# Criar processo para resolver o problema

# Se um cliente atrasar o pagmaento mais de 20 dias ele cancela
# Criar um processo para não deixar o cliente atrasar mais de 20 dias

# Todos os clientes do contrato mensal cancelam
# Criar processo de desconto dos planos anuais e trimestral

tabela = tabela[
    tabela["duracao_contrato"] != "Monthly"
]  # sem duraçao do contrato mensal
tabela = tabela[
    tabela["ligacoes_callcenter"] <= 4
]  # sem ligaçao do call center acima de 4
tabela = tabela[
    tabela["dias_atraso"] <= 20
]  # sem atraso de pagamento maior que 20 dias

print(
    tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)
)  # usando funçao map para diminuir as casas do percentual
