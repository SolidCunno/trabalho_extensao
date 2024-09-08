import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo Excel
df = pd.read_excel('Cadastro_de_Clientes_geral.xlsx')

# Corrigindo os erros de escrita na coluna "Serviço Desejado"
df['Serviço Desejado'] = df['Serviço Desejado'].replace(['clinico', 'clínico'], 'Clínico')

# Filtrando os clientes que optaram por "Clínico"
df_clinico = df.loc[df['Serviço Desejado'] == 'Clínico']

# Criando um gráfico de barras da contagem de clientes por região para o serviço "Clínico"
plt.figure(figsize=(14, 10))
sns.countplot(data=df_clinico, x='Endereço', order=df_clinico['Endereço'].value_counts().index)
plt.title('Moradores por Rua - Alto do Coqueirinho (Serviço Clínico)')
plt.xlabel('Região')
plt.ylabel('Número de moradores')
plt.xticks(rotation=90, ha='center')  # Rotaciona os rótulos para 90 graus e alinha ao centro
plt.tight_layout()  # Ajusta o layout para evitar cortes
plt.show()
