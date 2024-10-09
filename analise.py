import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = pd.read_excel('Cadastro_de_Clientes_geral.xlsx')

# Limpeza de dados
data.dropna(inplace=True)

# Verificar valores únicos na coluna 'Serviço Desejado' antes da limpeza
print("Valores únicos antes da limpeza:", data['Serviço Desejado'].unique())

# Limpar dados: remover espaços extras e padronizar valores
data['Serviço Desejado'] = data['Serviço Desejado'].str.strip().str.lower()

# Verificar novamente os valores únicos após a limpeza
print("Valores únicos após a limpeza:", data['Serviço Desejado'].unique())

# Análise Exploratória de Dados
print(data.describe())

# Distribuição de atendimentos por tipo de serviço
data['Serviço Desejado'].value_counts().plot(kind='bar')
plt.title('Distribuição de Atendimentos por Tipo de Serviço')
plt.xlabel('Tipo de Serviço')
plt.ylabel('Serviços mais solicitados')
plt.show()
