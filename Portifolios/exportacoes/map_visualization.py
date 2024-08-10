import pandas as pd
import plotly.express as px
import streamlit as st
import json

# Função para carregar dados e criar o mapa
def create_map():
    file_path = 'Portifolios/exportacoes/SerieExportacaoAl.csv'
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error('Arquivo não encontrado')
        return

    # Geojson com os municípios de Alagoas
    with open('Portifolios/exportacoes/Alagoas_Mapa.geojson') as f:
        geojson = json.load(f)

    # Lista de municípiosss
    municipios_geojson = [feature['properties']['NM_MUN'] for feature in geojson['features']]

    # Temas disponíveis
    temas = ['Blues', 'Magma']

    # Filtro de Tema
    tema_selecionado = st.selectbox('Selecione o tema do mapa:', temas)

    # Filtro de Data
    ano_inicial = df['CO_ANO'].min()
    anos_disponiveis = df['CO_ANO'].unique()
    ano_final = st.slider('Selecione a data final:', min_value=ano_inicial, max_value=anos_disponiveis.max(), value=ano_inicial)

    # Filtrar os dados com base no intervalo de anos selecionado
    df_filtrado = df[(df['CO_ANO'] >= ano_inicial) & (df['CO_ANO'] <= ano_final)]

    # Agrupar os dados por município e somar os valores
    df_filtrado = df_filtrado.groupby('Nome_Município').sum().reset_index()

    # Criar um DataFrame completo com todos os municípios e valores zeradosc
    df_completo = pd.DataFrame(municipios_geojson, columns=['Nome_Município'])
    df_completo = df_completo.merge(df_filtrado, on='Nome_Município', how='left').fillna(0)

    # Definir o valor mínimo fixo em 0
    valor_minimo = 0

    # Slider para o valor máximo com legenda "Valor em US$"
    valor_maximo = st.slider(
        'Valor em US$:',
        min_value=float(df_completo['VL_FOB'].min()),  
        max_value=float(df_completo['VL_FOB'].max()) + 1_000_000,  
        value=float(df_completo['VL_FOB'].mean()) + 1_000_000,  
        format="$%.0f"  # Formato dos valores do slider
    )

    # Função para criar o mapa coroplético
    def make_choropleth(input_df, geojson, input_id, input_column, input_color_theme, valor_minimo, valor_maximo):
        choropleth = px.choropleth(
            input_df,
            geojson=geojson,
            locations=input_id,
            featureidkey="properties.NM_MUN",
            color=input_column,
            color_continuous_scale=input_color_theme,
            range_color=(valor_minimo, valor_maximo),
            scope="south america",
            labels={input_column: 'Valor'}
        )
        choropleth.update_geos(fitbounds="locations", visible=False)
        choropleth.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            margin=dict(l=0, r=0, t=0, b=0),
            height=900,
            coloraxis_showscale=False,
            geo=dict(bgcolor='rgba(0,0,0,0)',
                     projection_scale=5,
                     
                     )
        )
        return choropleth

    # Parâmetros para a função
    input_id = 'Nome_Município'  
    input_column = 'VL_FOB'   

    # Mapa coroplético
    choropleth_fig = make_choropleth(df_completo, geojson, input_id, input_column, tema_selecionado, valor_minimo, valor_maximo)

    # Mostrar o mapa
    st.plotly_chart(choropleth_fig)

# Chamar a função create_map
if __name__ == "__main__":
    create_map()