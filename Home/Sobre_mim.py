import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie # type: ignore

def load_assets():
    assets = {}
    with open("image/animation_python.json", "r") as f:
        assets['animation_python'] = json.load(f)
    with open("image/animation_dashboard.json", "r") as f:
        assets['animation_dashboard'] = json.load(f)
    with open("image/animation_machinelearning.json", "r") as f:
        assets['animation_machinelearning'] = json.load(f)
    with open("image/animation_statistics.json", "r") as f:
        assets['animation_statistics'] = json.load(f)
    
    return assets

def display_profile():
    # Carregar os ativos
    assets = load_assets()

    # st.image(assets['falkzera'], width=200, use_column_width=False)

            
    # Container Principal
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("## **Lucas Falcão**")
            st.markdown("### Data Analytics | Data Science")
            st.markdown("### Lifelong Learner | Data-Driven Business Solutions")
            st.caption("23 anos, Maceió-AL")
            texto = """
            Olá, sou Lucas Falcão, graduando de Ciências Econômicas pela Universidade Federal de Alagoas - UFAL, possuo habilidades em Python 🐍, Data Science 📉 e Econometria 📊.
            Aqui você encontrará um pouco sobre mim, meus projetos e como entrar em contato. 🚀

            Sem dados, você é apenas mais uma pessoa com uma opinião. Com dados, você é uma pessoa com uma opinião fundamentada. 📊
            A análise de dados e a Ciência de dados é uma ferramenta poderosa para a tomada de decisões, e é por isso que estou aqui. 📈

            Siga os menus , e visualize as informações que deseja. Caso queira entrar em contato, utilize o formulário no menu "Contato" :email:.
            Ou se preferir, entre em contato pelas redes sociais.
            """
            # HTML para justificar o texto
            html_text = f"""
            <div style="text-align: justify;">
                {texto}
            </div>
            """
            # Exibir o texto justificado no Streamlit
            st.markdown(html_text, unsafe_allow_html=True)
            #     st.write("## Redes Sociais")

            col1, col22, col3 = st.columns(3)
            with col1:
                st_lottie(assets['animation_python'], height=100)
            with col22:
                st_lottie(assets['animation_dashboard'], height=100)
            with col3:
                st_lottie(assets['animation_machinelearning'], height=100)
        

        with col2:
            st.image("image/falkzera.png", width=200, use_column_width=True)

    st.write("---")
            
if __name__ == "__main__":
    display_profile()