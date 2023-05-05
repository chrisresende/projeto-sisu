import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

st.title("Regiões")

# # Carrega os dados de regiões
# df_cidades = pd.read_csv(
#     'https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv', sep=';')

# Gerar dados aleatórios
data = np.random.randint(1, 51, size=(100, 4))
dates = pd.date_range('1/1/2022', periods=100)

# Salvar os dados em um pandas DataFrame
df = pd.DataFrame(data, index=dates, columns=['A', 'B', 'C', 'D'])


# Criar um gráfico de linha simples
fig, ax = plt.subplots()
ax.bar(df.index, df['A'], label='Série A')
ax.bar(df.index, df['B'], label='Série B')
ax.bar(df.index, df['C'], label='Série C')
ax.bar(df.index, df['D'], label='Série D')
ax.legend()

# Configurar o eixo x do gráfico
days = mdates.DayLocator(interval=10)  # mostrar datas a cada 10 dias
date_fmt = mdates.DateFormatter('%Y-%m-%d')  # formato das datas
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(date_fmt)
plt.xticks(rotation=45)

# Renderizar o gráfico usando o Streamlit
st.pyplot(fig)

# Adicionar uma barra de busca por data
start_date = st.sidebar.date_input("Data de Início", min_value=df.index.min(
), max_value=df.index.max(), value=df.index.min())
end_date = st.sidebar.date_input("Data Final", min_value=df.index.min(
), max_value=df.index.max(), value=df.index.max())

# Selecionar os dados baseado nas datas selecionadas
mask = (df.index >= datetime.combine(start_date, datetime.min.time())) & (
    df.index <= datetime.combine(end_date, datetime.max.time()))
filtered_data = df.loc[mask]

# Transformar todos os valores da coluna 'B' em positivos
filtered_data['B'] = filtered_data['B'].abs()

# Criar um gráfico de barras
fig, ax = plt.subplots()
filtered_data.plot(kind='bar', ax=ax)
ax.legend()

# Configurar o eixo x do gráfico
days = mdates.DayLocator(interval=10)  # mostrar datas a cada 10 dias
date_fmt = mdates.DateFormatter('%Y-%m-%d')  # formato das datas
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(date_fmt)
plt.xticks(rotation=45)

# Renderizar o gráfico com os dados filtrados
st.pyplot(fig)
