import streamlit as st


class NavBar:
    def __init__(self):
        pass

    def show(self):
        st.markdown(
            """
            <style>
                .navbar {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 20px;
                    background-color: #333;
                    color: white;
                }

                .logo {
                    height: 50px;
                }

                .navbar-title {
                    font-size: 24px;
                    font-weight: bold;
                    text-decoration: none;
                    color: white;
                    margin-left: 10px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="navbar">
                <img src="https://cdn.pixabay.com/photo/2017/09/25/13/12/dna-2781266_960_720.png" alt="Logo" class="logo">
                <a class="navbar-title" href="#">Dados SISU</a>
            </div>
            """,
            unsafe_allow_html=True
        )
