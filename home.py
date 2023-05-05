import streamlit as st
# import pandas as pd
# import numpy as np
# from components.NavBar import NavBar
# from components.Login import Login
# from components.Dashboard import Dashboard
# from components.Regioes import Regioes

#Esta linha define o título da página e o ícone a ser exibido na guia do navegador.
st.set_page_config(
    page_title="Dados Sisu",
    page_icon="🏫",
)
#Esta linha define o título da página principal.
st.title("Painel de Dados Sisu")
#Esta linha cria uma mensagem de sucesso na barra lateral.
st.sidebar.success("Selecione uma pagina.")
  
    
    
    
    
    

# def main():
#     st.set_page_config(page_title="Sistema de Administração")

#     nav_bar = NavBar()
#     nav_bar.show()

#     page = st.sidebar.selectbox("Selecione uma opção", [
#                                 "Login", "Dashboard", "Regiões", "Universidades", "Cursos", "Distribuição por idade"])

#     if page == "Login":
#         login = Login()
#         login.show()
#     elif page == "Dashboard":
#         dashboard = Dashboard()
#         dashboard.show()
#     elif page == "Regiões":
#         regioes = Regioes()
#         regioes.show()
#     elif page == "Universidades":
#         st.write("Você selecionou a opção Universidades")
#     elif page == "Cursos":
#         st.write("Você selecionou a opção Cursos")
#     elif page == "Distribuição por idade":
#         st.write("Você selecionou a opção Distribuição por idade")


# if __name__ == '__main__':
#     main()
