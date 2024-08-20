import streamlit as st
import pandas as pd

def display_courses():
    col1, col2 = st.columns(2)
    with col1:  # FORMAÇÃO ACADÊMICA
        with st.expander("**FORMAÇÃO E ESPECIALIZAÇÃO**", expanded=False):
            st.write("## Graduação")
            st.write("Ciências Econômicas - Universidade Federal de Alagoas - UFAL")
            st.caption("Em andamento")
            st.write("---")

    with col2:  # CURSOS E CERTIFICADOS
        with st.expander("**CURSOS COM CERTIFICADOS**", expanded=False):
            st.write("## Cursos")
            st.write("#### **Escola Nacional de Administração Pública (ENAP)**")
            st.write("Introdução à Ciência de Dados - Conjuntos Frequentes - 2024")
            st.write("Aprendendo com Python - 2024")
            st.write("Estatística - 2024")
            st.write("---")

if __name__ == "__main__":
    display_courses()