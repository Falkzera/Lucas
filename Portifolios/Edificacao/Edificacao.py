import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from libpysal import weights
import os
import streamlit as st
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.axes_grid1 import make_axes_locatable
import folium
from folium import GeoJsonTooltip


def plot_map(variavel, tema='Blues'):

    csv_path = 'Portifolios/Edificacao/Edificacao_2022.csv'
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        st.error('Arquivo não encontrado')
        return None

    shapefile_path = 'Portifolios/Edificacao/AL_Municipios_2022/AL_Municipios_2022.shp'
    try:
        # Ler o arquivo shapefile
        alagoas = gpd.read_file(shapefile_path)
    except FileNotFoundError:
        st.error('Arquivo shapefile não encontrado')
        return None

    alagoas['CD_MUN'] = alagoas['CD_MUN'].astype(int)
    alagoas['NM_MUN'] = alagoas['NM_MUN'].str.upper()
    geo_df = pd.merge(alagoas, df, on='NM_MUN')

    # Criar o mapa
    m = folium.Map(location=[-10.5713, -35.7820], zoom_start=8)

    # Adicionar os dados ao mapa
    folium.Choropleth(
        geo_data=geo_df,
        name='choropleth',
        data=geo_df,
        columns=['NM_MUN', variavel],
        key_on='feature.properties.NM_MUN',
        fill_color=tema,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=variavel,
    ).add_to(m)

    # Adicionar tooltip para mostrar os valores ao passar o mouse
    folium.GeoJson(
        geo_df,
        style_function=lambda x: {'fillColor': '#ffffff00', 'color': '#000000', 'weight': 0.5},
        tooltip=GeoJsonTooltip(
            fields=['NM_MUN', variavel],
            aliases=['Município', variavel],
            localize=True
        )
    ).add_to(m)

    return m
