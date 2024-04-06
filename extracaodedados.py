import streamlit as st

def intro():
    import streamlit as st

    st.write("# Análise Estratégica de Vendas na Amazon: Compreendendo, Otimizando e Maximizando o Desempenho do Negócio")
    st.sidebar.success("Selecione um dos tópicos.")

    st.markdown(
        """
        Neste aplicativo, estamos realizando uma análise dos dados da Amazon. 
        Exploraremos as categorias de produtos, examinaremos as avaliações (ratings) e identificaremos tendências nos preços.   

        ** Selecione um dos tópicos ao lado para saber mais.

        ### Explorando os Tópicos de Análise: Insights para Estratégias de Vendas na Amazon

        * Extrair dados de vendas da Amazon: Isso inclui coletar informações sobre produtos, categorias, datas de venda e quantidades vendidas. Esses dados serão a base para as análises subsequentes.
        - Limpeza e Preparação de Dados: Antes de realizar qualquer análise, é essencial garantir que os dados estejam limpos e consistentes. Isso envolve lidar com valores ausentes, inconsistências e outliers que possam afetar a qualidade das análises.
        * Análise Descritiva: Calcular estatísticas descritivas, como média, mediana, desvio padrão, etc., nos permite entender a distribuição das vendas e identificar padrões importantes nos dados.
        - Análise de Preços: Comparar os preços de desconto e os preços reais para identificar a magnitude média dos descontos em cada categoria,.
        * Análise de Classificações: Explore as classificações e o número de avaliações para entender a reputação dos produtos em cada categoria, investigando a relação entre o número de avaliações e a classificação média.
        - Análise de Preços com Desconto: Analise a relação entre os preços de desconto e as classificações dos produtos. 
        * Visualizações Interativas: Por fim, criar gráficos e visualizações interativas nos permite comunicar insights de forma clara e acessível, facilitando a compreensão dos resultados e ajudando na tomada de decisões estratégicas.
        
    """
    )

def analise_descritiva():
    import streamlit as st
    import pandas as pd
    import os

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        
        """
    )

# Carregar os dados

page_names_to_funcs = {
    "Home": intro,
    "Análise Descritiva": analise_descritiva
    
}

demo_name = st.sidebar.selectbox("Escolha um dos tópicos", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()