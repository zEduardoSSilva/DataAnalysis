#pip install pandas
#pip install openpyxl
#pip install plotly

# Passo 1 - Importar Base de Dados

import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.csv")

# Passo 2 - Visualizar a Base de Dados
#Entender quais as informações estão disponiveis
#Descobrir as Cagadas da Base de Dados

tabela = tabela.drop("Unnamed: 0", axis=1)
#-Excluir colunas Desnecessária

# Passo 3 - Tratamento de Dados
#Valores que estão sendo Reconhecidos de forma errada

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#Valores Vazios

#all = somente todos
#any = pelo menos 1 valor vazio

#Deletar Colunas Vazia
tabela = tabela.dropna(how="all", axis=1)
#Deletar Linhas Vazia
tabela = tabela.dropna(how="any", axis=0)

#object -"TEXTO"
#float64 - "NUMEROS COM CASAS DECIMAIS"
#int64 - "NUMEROS INTEIRO"

#print(tabela.info())

# Passo 4 - Analise Inicial
# Analise de Como estão os nossos Cancelamento

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))

# Passo 5 - Analise mais Completa
#Comparar Cada Coluna da Minha Tabela com a Coluna de Cancelamento

#Etapa 1 - Criar o Grafico
#Para Edições de Grafico
#Para Mudar a Cor do Grafico, color_discrete

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequence=["blue", "green"])

#Etaoa 2 - Exibir o Grafico

    grafico.show()

#Clientes com Contratos mensal tem muito mais chance de cancelar os contratos:
#As Chances de Cancelamentos mensais é muito maior que os demais.
# - Podemos fazer promoções para o Cliente optar por Contratos Anuais

#Familias Maiores tendem a Cancelar menos do que Familias menores.
# - Podemos fazer promoções para o Cliente optar por linhas Extra de Telefon

#MesesComoCLiente baixo tem Muito Cancelamento. Cliente com pouco tempo tendem a Cancelar Muito.
# - A Primeira Experiencia do Cliente na Operadora pode ser ruim
# - Talvez a captação de Cliente esta trazendo clientes desqualificados
# - Ideia a gente pode criar incentivos para o cliente ficar com mais tempo com a linha.

#Quanto mais serviços o clinete possui, menor a taxa de cancelamento
# - podemos fazer promoções com mais serviços para o cliente

#Tem Alguma coisa no nosso serviço de fibra que esta fazendo os clientes cancelarem.
#- Agir sobre a Fibra

#Clientes no boleto tem mais chance de Cancelar, então temos que fazer alguma ação para eles irem para eles irem para outra forma de pagamento.
