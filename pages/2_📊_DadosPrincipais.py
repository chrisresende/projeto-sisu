import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

st.title("Dados Principais")

# Gerar dados aleatórios
data = np.random.randint(1, 51, size=(100, 4))
dates = pd.date_range('1/1/2022', periods=100)

# Salvar os dados em um pandas DataFrame
df = pd.DataFrame(data, index=dates, columns=['A', 'B', 'C', 'D'])

# Criar uma figura com 2x2 subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Plotar os dados no primeiro subplot
axs[0, 0].bar(df.index, df['A'], label='Série A')
axs[0, 0].set_title('Por curso escolhido')

# Plotar os dados no segundo subplot
axs[0, 1].bar(df.index, df['B'], label='Série B')
axs[0, 1].set_title('Por cidade')

# Plotar os dados no terceiro subplot
axs[1, 0].bar(df.index, df['C'], label='Série C')
axs[1, 0].set_title('Por Sexo')

# Plotar os dados no quarto subplot
axs[1, 1].bar(df.index, df['D'], label='Série D')
axs[1, 1].set_title('Por estado')

# Configurar o eixo x do gráfico
days = mdates.DayLocator(interval=60)  # mostrar datas a cada 60 dias
date_fmt = mdates.DateFormatter('%d-%m-%y')  # formato das datas
for ax in axs.flat:
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(date_fmt)
    ax.tick_params(axis='x', rotation=45)

# Renderizar o gráfico usando o Streamlit
st.pyplot(fig)
