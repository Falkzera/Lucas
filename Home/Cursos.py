import streamlit as st
import pandas as pd

def convert_to_direct_link(link):
    # Verifica se o link é do Google Drive e converte para link de visualização direta
    if 'drive.google.com' in link:
        file_id = link.split('/')[-2]
        direct_link = f"https://drive.google.com/file/d/{file_id}/preview"
        return direct_link
    return link

def display_certificates():
    st.title("Certificados de Cursos 🎓 ✓")
    st.write('Possuo certificados de cursos voltados a tecnologia, como Data Science, Data analytics, Machine Learning, Python, entre outros. Abaixo, você pode visualizar os certificados que possuo.')

    with st.expander("CLIAQUI AQUI PARA VISUALIZAR OS CERTIFICADOS", expanded=False):
    # Caminho absoluto para o arquivo CSV
        file_path = 'Home/Certificados/BDA_Certificados.csv'

        try:
            # Carregar o arquivo CSV
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            st.error('Arquivo CSV: Lista de Certificados não encontrado.')
            return

        if 'df' in locals():
            # Verificar se a coluna 'ANO' existe
            if 'ANO' in df.columns:
                # Converter a coluna 'ANO' para inteiro
                df['ANO'] = df['ANO'].astype(int)

                # Filtro temporal com slider
                st.sidebar.header("Filtro Temporal")

                # Definir intervalo de anos mínimo e máximo com base nos dados
                min_year = df['ANO'].min()
                max_year = df['ANO'].max()

                # Adicionar o slider de anos
                start_year, end_year = st.sidebar.slider(
                    "Selecione o intervalo de anos",
                    min_value=min_year,
                    max_value=max_year,
                    value=(min_year, max_year)
                )

                # Filtrar os dados com base no intervalo selecionado
                filtered_df = df[(df['ANO'] >= start_year) & (df['ANO'] <= end_year)]

                # Exibir dados filtrados (apenas Nome e Imagem)
                st.header("Certificados")
                
                # Criar três colunas
                col1, col2, col3 = st.columns(3)
                
                # Iterar sobre o DataFrame filtrado e distribuir os resultados nas colunas
                for index, row in filtered_df.iterrows():
                    direct_link = convert_to_direct_link(row['LINK'])
                    if index % 3 == 0:
                        with col1:
                            st.caption(f"### {row['NOME']}")
                            st.components.v1.iframe(direct_link, width=300, height=400)
                    elif index % 3 == 1:
                        with col2:
                            st.caption(f"### {row['NOME']}")
                            st.components.v1.iframe(direct_link, width=300, height=400)
                    else:
                        with col3:
                            st.caption(f"### {row['NOME']}")
                            st.components.v1.iframe(direct_link, width=300, height=400)
            else:
                st.error("A coluna 'ANO' não foi encontrada no DataFrame.")
        else:
            st.error("Houve algum erro ao carregar o DataFrame.")

if __name__ == "__main__":
    display_certificates()