import streamlit as st
import pandas as pd
import plotly.express as px

def comparacao_gestao():
    with st.container():
        # Carregar o novo DataFrame
        st.title('Transporte Público de Maceió :bus:')
        st.write('O objetivo central é visualizar o quanto que os cidadões Maceioenses precisam desembolsar anualmente, com base no salário minimo de cada época, para se locomover através do Transporte Público de Maceió. Foi considerado duas passagens por dia (Ida e Volta, de domingo a domingo) e adicionado o cenário de dependentes: (01 filho, 02 filhos e 03 filhos).')
        st.write('Considerando o salário minimo de cada época, foi calculado o percentual do salário minimo que o cidadão precisaria desembolsar para se locomover através do transporte público de Maceió.')
        st.write('É notável que ao longo do tempo, o cidadão maceioense tem desembolsado uma menor proporção do salário minimo para se locomover através do transporte público.')
        st.caption('Fonte: Dados Públicos da Prefeitura de Maceió')


        df_novo = pd.read_excel("Portifolios/CompracaoGestao/GASTOS_GROUPED.xlsx")
        # Remover de PREFEITO as '[]' e as aspas
        df_novo['PREFEITO'] = df_novo['PREFEITO'].str.replace('[', '').str.replace(']', '').str.replace("'", '')

        mapeamento_prefeitos = {'KATIA BORN': 'Gestão 1','CÍCERO ALMEIDA': 'Gestão 2','RUI PALMEIRA': 'Gestão 3','JHC': 'Gestão 4'}

        df_novo['PREFEITO'] = df_novo['PREFEITO'].replace(mapeamento_prefeitos)

        # Colunas de gasto para comparação
        colunas_gasto1 = ['GASTO_1_PESSOA_FILHO_3_PERCENT', 'GASTO_1_PESSOA_FILHO_2_PERCENT', 'GASTO_1_PESSOA_FILHO_1_PERCENT', 'GASTO_ANUAL_SEM_FILHO_PERCENT']
        colunas_gasto = ['3 filhos', '2 filhos', '1 filho', 'sem filhos']

        mapeamento_colunas = dict(zip(colunas_gasto1, colunas_gasto))

        # Renomear as colunas no DataFrame
        df_novo.rename(columns=mapeamento_colunas, inplace=True)

        # Adicionar um selectbox para selecionar a coluna a ser visualizada
        coluna_selecionada = st.selectbox('Selecione os cenários', colunas_gasto)

        # Adicionar um slider para filtrar o DataFrame por ano
        ano_inicial = st.slider('Selecione o périodo de análise', min_value=2000, max_value=2024, value=2000)
        df_novo = df_novo[df_novo['ANO'] >= ano_inicial]

        # Fazer a comparação de gestão para a coluna selecionada
        df_gestao = df_novo.groupby(['PREFEITO', 'ANO'])[coluna_selecionada].mean().reset_index()

        # Ordenar os prefeitos pelos seus anos de gestão
        df_gestao = df_gestao.sort_values(by='ANO')

        # Adicionar uma checkbox para permitir a seleção de exibir pontos ou não
        exibir_pontos = st.checkbox('Exibir pontos no gráfico', value=True)

        # Criar o gráfico de linha com ou sem pontos
        fig_gestao = px.line(df_gestao, x='ANO', y=coluna_selecionada, color='PREFEITO',
                             labels={coluna_selecionada: f'Proporção do Gasto ({coluna_selecionada})', 'ANO': 'Ano de Gestão'},
                             title=f'Proporção do gasto anual com transporte público possuíndo {coluna_selecionada} por gestão ao Longo dos Anos',
                             markers=exibir_pontos)

        # Adicionar anotações de texto para cada ponto, se a opção de exibir pontos estiver selecionada
        if exibir_pontos:
            for i in range(len(df_gestao)):
                fig_gestao.add_annotation(x=df_gestao['ANO'][i], y=df_gestao[coluna_selecionada][i],
                                          text=f"{df_gestao[coluna_selecionada][i]:.2f}%",
                                          showarrow=True, arrowhead=2, ax=0, ay=-20)

        fig_gestao.update_layout(xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig_gestao)

        # Adicionar um checkbox para exibir o DataFrame
        df_novo = df_novo.sort_values(by=['ANO', 'PREFEITO'])
        df_penultimo_ano = df_novo.groupby('PREFEITO').nth(-2).reset_index()

        st.dataframe(df_penultimo_ano[['PREFEITO', '3 filhos', '2 filhos', '1 filho', 'sem filhos']], column_config={
            "3 filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (3 filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_penultimo_ano['3 filhos'].max())
            ),
            "2 filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (2 filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_penultimo_ano['2 filhos'].max())
            ),
            "1 filho": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (1 filho)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_penultimo_ano['1 filho'].max())
            ),
            "sem filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (sem filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_penultimo_ano['sem filhos'].max())
            )
        }, height=175, width=1200)

if __name__ == "__main__":
    comparacao_gestao()