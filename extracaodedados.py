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
        - Análise de Preços com Desconto:: Analise a relação entre os preços de desconto e as classificações dos produtos. 
        * Visualizações Interativas: Por fim, criar gráficos e visualizações interativas nos permite comunicar insights de forma clara e acessível, facilitando a compreensão dos resultados e ajudando na tomada de decisões estratégicas.
        
    """
    )

def mapping_demo():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        This demo shows how to use
        [`st.pydeck_chart`](https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart)
        to display geospatial data.
        """
    )

    @st.cache_data
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def plotting_demo():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
        Streamlit. We're generating a bunch of random numbers in a loop for around
        5 seconds. Enjoy!
        """
    )

# Carregar os dados
@st.cache_data
def load_data():
    # Suponha que você já tenha carregado os 140 arquivos CSV e concatenado em um único DataFrame
    # data = pd.concat([pd.read_csv(file) for file in file_list])
    # Aqui, para fins de exemplo, estou criando um DataFrame de exemplo:
    # Lista para armazenar os DataFrames de cada arquivo CSV

# Lista para armazenar os DataFrames de cada arquivo CSV
dfs = []

# Diretório onde os arquivos CSV estão localizados
diretorio = "archive"

# Loop pelos arquivos CSV no diretório
for filename in os.listdir(diretorio):
    if filename.endswith(".csv"):
        # Caminho completo para o arquivo CSV
        filepath = os.path.join(diretorio, filename)
        # Carrega o arquivo CSV em um DataFrame
        df = pd.read_csv(filepath)
        # Adiciona o DataFrame à lista
        dfs.append(df)

# Concatena todos os DataFrames da lista em um único DataFrame
data = pd.concat(dfs, ignore_index=True)

# Função para calcular estatísticas descritivas e plotar gráficos
def descriptive_analysis(data):
    # Calcular estatísticas descritivas
    stats = data[['ratings', 'no_of_ratings', 'discount_price', 'actual_price']].describe()

    # Plotar histograma de ratings
    st.subheader('Histograma de Ratings')
    fig, ax = plt.subplots()
    sns.histplot(data['ratings'], kde=True, ax=ax)
    st.pyplot(fig)

    # Plotar boxplot de preços
    st.subheader('Boxplot de Preços')
    fig, ax = plt.subplots()
    sns.boxplot(data=data[['discount_price', 'actual_price']], ax=ax)
    st.pyplot(fig)

    # Exibir estatísticas descritivas
    st.subheader('Estatísticas Descritivas')
    st.write(stats)

def main():
    st.title('Análise Descritiva de Dados')

    # Carregar os dados
    data = load_data()

    # Realizar análise descritiva
    descriptive_analysis(data)

if __name__ == "__main__":
    main()




def data_frame_demo():
    import streamlit as st
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )

    @st.cache_data
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

page_names_to_funcs = {
    "Home": intro,
    "Análise Descritiva": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Escolha um dos tópicos", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()