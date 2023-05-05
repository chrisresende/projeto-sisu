import streamlit as st

class Login:
    def __init__(self):
        pass

    def show(self):
        st.title("Login")

        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if username == "admin" and password == "123":
                st.success("Login realizado com sucesso!")
            else:
                st.error("Usuário ou senha incorretos.")
