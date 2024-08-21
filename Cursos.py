import streamlit as st

def display_courses():
  # FORMAÇÃO ACADÊMICA
        with st.expander("**FORMAÇÃO E ESPECIALIZAÇÃO**", expanded=False):
            st.write("## Graduação")
            st.write("Ciências Econômicas - Universidade Federal de Alagoas - UFAL")
            st.caption("Em andamento")
            st.write("---")
 # CURSOS E CERTIFICADOS
        with st.expander("**CURSOS COM CERTIFICADOS**", expanded=False):
            st.write("## Cursos")
            st.write("#### **Escola Nacional de Administração Pública (ENAP)**")
            st.write("Introdução à Ciência de Dados - Conjuntos Frequentes - 2024")
            st.write("Introdução à Ciência de Dados - Conceitos e Ferramentas - 2024")
            st.write("Introdução à Ciência de Dados - Modelos de Regressão - 2024")
            st.write("Introdução à Ciência de Dados - Modelos de Agrupamento - 2024")
            st.write("Análise de dados como suporte à tomada de decisão. - 2024")
            st.write("Estatística para Análise de Dados na Administração Pública - 2024")
            st.write("Criação de indicadores de desempenho para transformação digital - 2024")
            st.write("Aprendendo com Python - 2024")
            st.write("Estatística - 2024")
            st.write("---")


if __name__ == "__main__":
    display_courses()