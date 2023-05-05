import streamlit as st
import pandas as pd
import numpy as np


class Regioes:
    def __init__(self):
        pass

    def show(self):
        st.title("Regioes")

        chart_data = pd.DataFrame(
            np.random.randn(40, 7),
            columns=["a", "b", "c", "d", "e", "f", "g"]
        )

        # Alterando o estilo do gráfico
        st.bar_chart(chart_data)

