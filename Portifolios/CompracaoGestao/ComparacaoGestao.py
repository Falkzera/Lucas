import streamlit as st
import pandas as pd
import plotly.express as px

def comparacao_gestao():

    # Título
    st.subheader("Projeto: Análise do Custo do Transporte Público em Maceió ao longo dos anos")
    st.caption("Equipe: Cleydner Maurício, Maria Eduarda, Lucas Falcão.")
    with st.expander('Sobre o Projeto', expanded=True):
        st.subheader('Objetivo:')
        st.write('O objetivo central é visualizar o quanto que os cidadãos maceioenses precisam desembolsar anualmente, com base no salário minimo de cada época, para se locomover através do Transporte Público de Maceió. Foi considerado duas passagens por dia (Ida e Volta, de domingo a domingo) e adicionado o cenário de dependentes: (01 filho, 02 filhos e 03 filhos).')
        st.write('Considerando o salário minimo de cada época, foi calculado o percentual do salário minimo que o cidadão precisaria desembolsar para se locomover através do transporte público de Maceió.')

    with st.expander('Nota técnica: ', expanded=True):
        st.write("""
        PREMISSAS:
        1. Renda de um Salário Mínimo, considerando o valor do salário a cada mês do ano.
        2. Gasto com transporte considerando 2 (duas) passagens por dia. O número de dias durante o ano com o respectivo valor da tarifa no dia.
        3. Foi aplicada a política pública do “Domingo é meia” e do "Domingo é Livre", bem como a do passe livre estudantil, sendo admitidos 200 dias letivos.
        4. Foram consideradas uma família sem gastos com transporte dos filhos e outra com gastos, sendo admitido 2 (dois) filhos em idade escolar (meia passagem ou passe livre, conforme política pública do ano).
        """)

    st.write("---")

    with st.container():
        st.subheader('Visualização Gráfica')
        # Carregar o novo DataFrame
        df_novo = pd.read_excel("Portifolios/CompracaoGestao/GASTOS_GROUPED.xlsx")
        df_individual = pd.read_csv("Portifolios/CompracaoGestao/custoindividual.csv")
        df_familiar = pd.read_csv("Portifolios/CompracaoGestao/custofamiliar.csv")
        # Remover de PREFEITO as '[]' e as aspas
        df_novo['PREFEITO'] = df_novo['PREFEITO'].str.replace('[', '').str.replace(']', '').str.replace("'", '')

        # Colunas de gasto para comparação
        colunas_gasto1 = ['GASTO_1_PESSOA_FILHO_3_PERCENT', 'GASTO_1_PESSOA_FILHO_2_PERCENT', 'GASTO_1_PESSOA_FILHO_1_PERCENT', 'GASTO_ANUAL_SEM_FILHO_PERCENT']
        colunas_gasto = ['3 filhos', '2 filhos', '1 filho', 'sem filhos']

        mapeamento_colunas = dict(zip(colunas_gasto1, colunas_gasto))

        # Renomear as colunas no DataFrame
        df_novo.rename(columns=mapeamento_colunas, inplace=True)

        # Adicionar um selectbox para selecionar a coluna a ser visualizada
        colunas_gestao = colunas_gasto + ['Comparativo']
        coluna_selecionada = st.selectbox('Selecione os cenários', colunas_gestao)

        # Adicionar um slider para filtrar o DataFrame por ano
        ano_inicial = st.slider('Selecione o périodo de análise', min_value=2000, max_value=2024, value=2000)
        df_novo = df_novo[df_novo['ANO'] >= ano_inicial]

        if coluna_selecionada == 'Comparativo':
            # Adicionar checkboxes para selecionar as colunas de comparação
            colunas_comparacao = st.multiselect('Selecione as colunas para comparação:', colunas_gasto)
            if not colunas_comparacao:
                st.write('Selecione os gráficos de comparação')
            colunas_para_comparar = colunas_comparacao
        else:
            colunas_para_comparar = [coluna_selecionada]

        if colunas_para_comparar:
            # Fazer a comparação de gestão para as colunas selecionadas
            df_gestao = df_novo.groupby(['PREFEITO', 'ANO'])[colunas_para_comparar].mean().reset_index()

            # Ordenar os prefeitos pelos seus anos de gestão
            df_gestao = df_gestao.sort_values(by='ANO')

            # Adicionar uma checkbox para permitir a seleção de exibir pontos ou não
            exibir_pontos = st.checkbox('Clique para Exibir pontos no gráfico', value=True)

            # Combinar os DataFrames para comparação
            df_comparacao = pd.melt(df_gestao, id_vars=['PREFEITO', 'ANO'], value_vars=colunas_para_comparar, 
                                    var_name='Tipo', value_name='Proporção do Gasto')

            # Criar o gráfico de linha com ou sem pontos
            fig = px.line(df_comparacao, x='ANO', y='Proporção do Gasto', color='PREFEITO', line_dash='Tipo',
                        labels={'Proporção do Gasto': 'Proporção do Gasto (%)', 'ANO': 'Ano', 'PREFEITO': 'Gestão'}, 
                        markers=exibir_pontos)

            # Atualizar as cores das linhas
            fig.for_each_trace(
                lambda trace: trace.update(line=dict(color='green')) if trace.name == 'JHC' else (
                    trace.update(line=dict(color='darkred')) if trace.name == 'KATIA BORN' else (
                        trace.update(line=dict(color='red')) if trace.name == 'CÍCERO ALMEIDA' else (
                            trace.update(line=dict(color='darkorange')) if trace.name == 'RUI PALMEIRA' else ()
                        )
                    )
                )
            )

            # Adicionar anotações de texto para cada ponto, se a opção de exibir pontos estiver selecionada
            if exibir_pontos:
                for i in range(len(df_comparacao)):
                    fig.add_annotation(x=df_comparacao['ANO'].iloc[i], y=df_comparacao['Proporção do Gasto'].iloc[i],
                                    text=f"{df_comparacao['Proporção do Gasto'].iloc[i]:.2f}%",
                                    showarrow=True, arrowhead=2, ax=0, ay=-20)

            fig.update_layout(xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig)

    st.write('---')

    st.subheader('Visualização Tabular')
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
        st.write('Selecione o formato tabular desejado abaixo: ')

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

    st.write('---')

    # % CTransporte/Renda Familiar
    with st.container():
        st.subheader("Resumo do Custo do Transporte Público em Maceió")
        
        # Adicionar uma seleção para escolher entre custo familiar, custo individual e comparação
        opcao_grafico = st.selectbox('Selecione o gráfico para visualizar', ['Custo Familiar', 'Custo Individual', 'Comparação'])
        
        def atualizar_cores(fig):
            fig.for_each_trace(
                lambda trace: trace.update(line=dict(color='green')) if trace.name == 'JHC' else (
                    trace.update(line=dict(color='darkred')) if trace.name == 'KATIA' else (
                        trace.update(line=dict(color='red')) if trace.name == 'CICERO' else (
                            trace.update(line=dict(color='darkorange')) if trace.name == 'RUI' else ()
                        )
                    )
                )
            )
        
        if opcao_grafico == 'Custo Familiar':
            st.subheader('Custo Familiar Anual com Transporte Público em Maceió')
            # df_familiar = pd.read_csv("new_data/custofamiliar.csv")
            
            # Adicionar uma opção para exibir pontos no gráfico
            exibir_pontos = st.checkbox('Clique para Exibir pontos no gráfico:', value=True)
            
            # Criar o gráfico de linha com ou sem pontos
            fig = px.line(df_familiar, x='ANO', y='GASTO_ANUAL', color='GESTAO', 
                        labels={'GASTO_ANUAL': 'Gasto Anual (R$)', 'ANO': 'Ano'}, 
                        markers=exibir_pontos)
            
            # Atualizar as cores das linhas
            atualizar_cores(fig)
            
            # Adicionar anotações de texto para cada ponto, se a opção de exibir pontos estiver selecionada
            if exibir_pontos:
                for i in range(len(df_familiar)):
                    fig.add_annotation(x=df_familiar['ANO'].iloc[i], y=df_familiar['GASTO_ANUAL'].iloc[i],
                                    text=f"{df_familiar['GASTO_ANUAL'].iloc[i]:.2f}%",
                                    showarrow=True, arrowhead=2, ax=0, ay=-20)
            
            fig.update_layout(xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig)
        
        elif opcao_grafico == 'Custo Individual':
            st.subheader('Custo Individual Anual com Transporte Público em Maceió')
            # df_individual = pd.read_csv("new_data/custoindividual.csv")
            
            # Adicionar uma opção para exibir pontos no gráfico
            exibir_pontos = st.checkbox('Clique para Exibir pontos no gráfico: ', value=True)
            
            # Criar o gráfico de linha com ou sem pontos
            fig = px.line(df_individual, x='ANO', y='GASTO_ANUAL', color='GESTAO',
                        labels={'GASTO_ANUAL': 'Gasto Anual (R$)', 'ANO': 'Ano'},
                        markers=exibir_pontos)
            
            # Atualizar as cores das linhas
            atualizar_cores(fig)
            
            # Adicionar anotações de texto para cada ponto, se a opção de exibir pontos estiver selecionada
            if exibir_pontos:
                for i in range(len(df_individual)):
                    fig.add_annotation(x=df_individual['ANO'].iloc[i], y=df_individual['GASTO_ANUAL'].iloc[i],
                                    text=f"{df_individual['GASTO_ANUAL'].iloc[i]:.2f}%",
                                    showarrow=True, arrowhead=2, ax=0, ay=-20)
                    
            fig.update_layout(xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig)
        
        elif opcao_grafico == 'Comparação':
            st.subheader('Comparação do Custo Familiar e Individual Anual com Transporte Público em Maceió')
            # df_familiar = pd.read_csv("new_data/custofamiliar.csv")
            # df_individual = pd.read_csv("new_data/custoindividual.csv")
            
            # Adicionar uma opção para exibir pontos no gráfico
            exibir_pontos = st.checkbox('Clique para Exibir pontos no gráfico:', value=True)
            
            # Combinar os DataFrames para comparação
            df_familiar['Tipo'] = 'Familiar'
            df_individual['Tipo'] = 'Individual'
            df_comparacao = pd.concat([df_familiar, df_individual])
            
            # Criar o gráfico de linha com ou sem pontos
            fig = px.line(df_comparacao, x='ANO', y='GASTO_ANUAL', color='GESTAO', line_dash='Tipo',
                        labels={'GASTO_ANUAL': 'Gasto Anual (R$)', 'ANO': 'Ano', 'GESTAO': 'Gestão'}, 
                        markers=exibir_pontos)
            
            # Atualizar as cores das linhas
            atualizar_cores(fig)
            
            # Adicionar anotações de texto para cada ponto, se a opção de exibir pontos estiver selecionada
            if exibir_pontos:
                for i in range(len(df_comparacao)):
                    fig.add_annotation(x=df_comparacao['ANO'].iloc[i], y=df_comparacao['GASTO_ANUAL'].iloc[i],
                                    text=f"{df_comparacao['GASTO_ANUAL'].iloc[i]:.2f}%",
                                    showarrow=True, arrowhead=2, ax=0, ay=-20)
            
            fig.update_layout(xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig)
            st.write("A gestão do Prefeito JHC foi a que mais beneficiou os cidadãos Maceioenses com o transporte público, em comparação com as gestões anteriores.")
            st.write("JHC conseguiu equiparar o custo do transporte público individual com o custo do transporte público familiar, o que não ocorreu nas gestões anteriores.")
    st.write("---")
    st.subheader("Conclusão")
    st.write("O presente trabalho buscou desenvoler um estudo técnico sobre o custo do transporte público em Maceió, com base no salário mínimo de cada época. Foi possível observar que a gestão de 2023 e 2024 foi a que mais beneficiou os cidadãos Maceioenses com o transporte público, em comparação com as gestões anteriores. A gestão através de politícas públicas onseguiu equiparar o custo do transporte público individual com o custo do transporte público familiar, o que não ocorreu nas gestões anteriores. Diversos fatores contribuiu para esse resultado, o mais impactante foi a gratuidade do transporte público para estudantes, o que reduziu significativamente o custo do transporte público para as famílias com filhos em idade escolar.")

if __name__ == "__main__":
    comparacao_gestao()