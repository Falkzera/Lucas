import streamlit as st
import pandas as pd
import plotly.express as px

def comparacao_gestao():


    # Configuração da página

    # Título
    st.title('Transporte Público - Prefeitura de Maceió :bus:')
    st.subheader("Comparativo do percentual de gastos anuais com transporte público em Maceió por gestão")
    with st.expander('Sobre o Projeto', expanded=True):
        st.subheader('Objetivo:')
        st.write('O objetivo central é visualizar o quanto que os cidadões Maceioenses precisam desembolsar anualmente, com base no salário minimo de cada época, para se locomover através do Transporte Público de Maceió. Foi considerado duas passagens por dia (Ida e Volta, de domingo a domingo) e adicionado o cenário de dependentes: (01 filho, 02 filhos e 03 filhos).')
        st.write('Considerando o salário minimo de cada época, foi calculado o percentual do salário minimo que o cidadão precisaria desembolsar para se locomover através do transporte público de Maceió.')


    with st.container():
        # Carregar o novo DataFrame
        df_novo = pd.read_excel("Portifolios/CompracaoGestao/GASTOS_GROUPED.xlsx")
        # Remover de PREFEITO as '[]' e as aspas
        df_novo['PREFEITO'] = df_novo['PREFEITO'].str.replace('[', '').str.replace(']', '').str.replace("'", '')

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

        # Atualizar a cor da linha para cada prefeito
        fig_gestao.for_each_trace(
            lambda trace: trace.update(line=dict(color='green')) if trace.name == 'JHC' else (
                trace.update(line=dict(color='darkred')) if trace.name == 'KATIA BORN' else (
                    trace.update(line=dict(color='red')) if trace.name == 'CÍCERO ALMEIDA' else (
                        trace.update(line=dict(color='darkorange')) if trace.name == 'RUI PALMEIRA' else ()
                    )
                )
            )
        )

        fig_gestao.update_layout(xaxis_title=None, yaxis_title=None)
        st.plotly_chart(fig_gestao)

    # Adicionar um selectbox para escolher entre visualizar por prefeito ou por ano
    opcao_visualizacao = st.selectbox('Escolha a visualização', ['Por Prefeito', 'Por Ano'])

    df_novo = df_novo.sort_values(by=['ANO', 'PREFEITO'])

    if opcao_visualizacao == 'Por Prefeito':
        # Calcular a média dos indicadores por prefeito
        df_media_prefeito = df_novo.groupby('PREFEITO').mean().reset_index()
        
        # Definir a ordem específica dos prefeitos
        ordem_prefeitos = ['KATIA BORN', 'CÍCERO ALMEIDA', 'RUI PALMEIRA', 'JHC']
        df_media_prefeito['PREFEITO'] = pd.Categorical(df_media_prefeito['PREFEITO'], categories=ordem_prefeitos, ordered=True)
        df_media_prefeito = df_media_prefeito.sort_values('PREFEITO')
        
        # Exibir os dados tabulados por prefeito com colunas de progresso
        st.dataframe(df_media_prefeito[['PREFEITO', '3 filhos', '2 filhos', '1 filho', 'sem filhos']], column_config={
            "3 filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (3 filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_media_prefeito['3 filhos'].max())
            ),
            "2 filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (2 filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_media_prefeito['2 filhos'].max())
            ),
            "1 filho": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (1 filho)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_media_prefeito['1 filho'].max())
            ),
            "sem filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (sem filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_media_prefeito['sem filhos'].max())
            )
        }, height=178, width=1500)
    else:
        # Exibir os dados tabulados por ano com colunas de progresso
        df_novo['ANO'] = df_novo['ANO'].astype(str).str.replace(',', '')
        st.dataframe(df_novo[['ANO', 'PREFEITO', '3 filhos', '2 filhos', '1 filho', 'sem filhos']], column_config={
            "3 filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (3 filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_novo['3 filhos'].max())
            ),
            "2 filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (2 filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_novo['2 filhos'].max())
            ),
            "1 filho": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (1 filho)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_novo['1 filho'].max())
            ),
            "sem filhos": st.column_config.ProgressColumn(
                "Gasto da Renda Anual (sem filhos)", 
                format="%.2f%%", 
                min_value=0, 
                max_value=float(df_novo['sem filhos'].max())
            )
        }, height=913, width=1500)

        st.write('De acordo com os dados, é nítido que a gestão do Prefeito JHC foi o que mais benéficiou os cidadão Maceioense com o transporte público, em comparação com as gestões anteriores.')
        st.write('Diversas políticas públicas foram empregadas durante esse período, como a implantação do Domingo é Livre e o Passa Gratuito para estudantes e diversas opções de integração entre linhas.')

    # Expander para formato tabular por prefeito
    with st.expander('Formato tabular por prefeito'):
        # Calcular a média dos indicadores por prefeito
        df_media_prefeito = df_novo.groupby('PREFEITO').mean().reset_index()
        
        # Definir a ordem específica dos prefeitos
        ordem_prefeitos = ['KATIA BORN', 'CÍCERO ALMEIDA', 'RUI PALMEIRA', 'JHC']
        df_media_prefeito['PREFEITO'] = pd.Categorical(df_media_prefeito['PREFEITO'], categories=ordem_prefeitos, ordered=True)
        df_media_prefeito = df_media_prefeito.sort_values('PREFEITO')
        
        # Formatar os valores com duas casas decimais e adicionar o sinal de %
        df_media_prefeito[['3 filhos', '2 filhos', '1 filho', 'sem filhos']] = df_media_prefeito[['3 filhos', '2 filhos', '1 filho', 'sem filhos']].applymap(lambda x: f"{x:.2f}%")
        
        # Exibir os dados tabulados por prefeito sem a coluna de índice
        st.table(df_media_prefeito[['PREFEITO', '3 filhos', '2 filhos', '1 filho', 'sem filhos']])

    # Expander para formato tabular por ano
    with st.expander('Formato tabular por ano'):
        # Remover a vírgula dos anos
        df_novo['ANO'] = df_novo['ANO'].astype(str).str.replace(',', '')
        
        # Formatar os valores com duas casas decimais e adicionar o sinal de %
        df_novo[['3 filhos', '2 filhos', '1 filho', 'sem filhos']] = df_novo[['3 filhos', '2 filhos', '1 filho', 'sem filhos']].applymap(lambda x: f"{x:.2f}%")
        
        # Exibir os dados tabulados por ano
        st.table(df_novo[['ANO', 'PREFEITO', '3 filhos', '2 filhos', '1 filho', 'sem filhos']])





































if __name__ == "__main__":
    comparacao_gestao()