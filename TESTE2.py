import streamlit as st
from datetime import datetime
from babel.dates import format_date
import locale
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError
import altair as alt


# Definir localidade para Português do Brasil
import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')

# Incluir a logo acima do menu de navegação lateral
st.image("baner.png", use_column_width=True)

# Título streamlit
titulo = st.title("""
PORTIFÓLIO DE TRABALHO E ANÁLISE DE DADOS
Formado em Administração de Empresas pela faculdade Pitágoras e Pós graduado em Ciência e Analise dados pela faculdade Estacio.
Projeto desenvolvido em linguagem 100% Python com Streamlit.
                  
                     "Quanto mais profundo e sólidos forem os motivos básicos de uma pessoa, 
                        maior será a certeza do sucesso de sua empreitada" Lucas 6:48.
""")

# Incluir CSS para estilizar o menu de navegação
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f0;  /* Cor de fundo clara */
    }
    .sidebar .sidebar-content img {
        margin-bottom: 20px;  /* Espaço abaixo da imagem */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Adicionar a logo acima do menu de navegação lateral
st.sidebar.image("logo.png", use_column_width=True)  # Substitua "logo.png" pelo caminho da sua imagem

# Componentes na barra lateral para navegação
st.sidebar.title('Menu de Navegação')

# Menu PBIX
pagina = st.sidebar.selectbox(
    'Projetos Com Power BI:',
    ['Selecione uma opção','_____Power BI______','Página Principal', 'Análise Roteirização', 'Análise Combustível',
     'Análise Financeira - Manutenção','______Python_______','Analise Dados','______Microsoft Excel_______','Aulas e Consultoria','Analise Dados e Dashboards','______Microsoft Access_______','Fale Conosco']
)

# Adicionar calendário abaixo do selectbox
data_selecionada = st.sidebar.date_input('Selecione uma data')

# Formatar a data selecionada em Português do Brasil
data_formatada = format_date(data_selecionada, format='long', locale='pt_BR')

# Exibir a data formatada
st.sidebar.write('Data selecionada:', data_formatada)

# Campo de texto para entrada do destino
destino = st.sidebar.text_input('Selecione um destino')

# Geocodificação para converter o destino em coordenadas
if destino:
    geolocator = Nominatim(user_agent="myGeocoder")
    try:
        location = geolocator.geocode(destino)
        if location:
            map_data = pd.DataFrame({
                'lat': [location.latitude],
                'lon': [location.longitude]
            })
            st.sidebar.write(f"Coordenadas de {destino}: {location.latitude}, {location.longitude}")
            st.map(map_data)
        else:
            st.sidebar.write("Destino não encontrado")
    except GeocoderServiceErroraaa as e:
        st.sidebar.write(f"Erro ao buscar o destino: {e}")
else:
    st.sidebar.write("Insira um destino para visualizar no mapa")

# Campo de texto para entrada do número de WhatsApp
numero_zap = st.sidebar.text_input('Digite o número WhatsApp (com código do país, ex: 5582999999999)')

# Converter o número em link do WhatsApp
if numero_zap:
    link_whatsapp = f"https://wa.me/{numero_zap}"
    st.sidebar.markdown(f"[Link gerado com sucesso - Clique aqui]({link_whatsapp})")

# Condicional para exibir conteúdo com base na seleção do usuário
roteirizacao = "https://app.powerbi.com/view?r=eyJrIjoiZGYyYzcwMDYtYzZmZC00YjlhLWJjYzQtYmE4MmMyOTc5MTdmIiwidCI6ImY1OGYxNjE2LWZkYWEtNGRhZS1hN2ZjLTc1ODI5YzkxOWE2YSJ9"
Url_Form_contato = "https://forms.gle/KxkxER6rRhgAmmxMA"
combustivel = "https://app.powerbi.com/view?r=eyJrIjoiODkzNmZmY2ItNTVhYy00ZTEwLWJkYTMtZTJjNjZlNzE1NzgzIiwidCI6ImFiNWQ1NWI3LWU3ZWYtNDM1ZS04NTAwLWJjOWY0NTE1ZTU2MiJ9"

if pagina == 'Página Principal':
    st.markdown("""
    ## Bem-vindo (a) à minha página de trabalhos produzidos em Power BI, Python, Microsoft Access e Microsoft Excel
    
    Me chamo Williams Rodrigues, sou pós-graduando em Ciência de Dados e bacharel em administração de empresas. Atualmente, trabalho no setor logístico de planejamento e controle de um dos maiores home centers do país.
    
    Sempre tive paixão pela área de tecnologia, onde fiz vários cursos como Web Designer, linguagem CSS6, HTML, Portugol, Python, VBA com Access.
    
    Agradeço a Deus por toda sabedoria em meus estudos, e também gostaria de agradecer a meu pai, Luiz da Silva, por ser meu motivador e inspirador em meus valores, princípios e ética pessoal. Também quero agradecer minha esposa, Luciene Gomes, pelos momentos de compreensão e paciência durante meu aprendizado.
    
    O Desenvolvimento em Python ocorreu em meu currículo em 2024 após realizar um desejo e vontade pessoal em retomar os estudos na área de tecnólogia,
    Foi ai que resolvi me matricular no curso de pós graduação em CIÊNCIA E BIG DATA ANALYTICS pela faculdade Estacio e ai fiquei tão fascinado com esta linguagem,
    que comecei a realizar alguns projetos pessoais.
                
    Contatos: [WhatsApp](https://wa.me/5582988639394) 
                
    Email: wr.rodriguesvieira@outlook.com
    """)

elif pagina == 'Análise Roteirização':
    st.title('Mapeamento e Análise de Dados do Planejamento de Roteirização')
    st.markdown(f'<iframe width="800" height="600" src="{roteirizacao}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif pagina == 'Análise Combustível':
    st.title('Mapeamento e Análise de Consumo de Combustíveis')
    st.markdown(f'<iframe width="800" height="600" src="{combustivel}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif pagina == 'Análise Financeira - Manutenção':
    st.title('Análise Financeira - Manutenção')

elif pagina == 'Analise Dados':
    st.title('Análise de Dados')
    uploaded_file = st.file_uploader("Selecione seu arquivo XLSX ou CSV", type=['xlsx', 'csv'])
    
    if uploaded_file is not None:
        # Carrega os dados do arquivo
        df = __loader__(uploaded_file)
        
        # Verifica se o dataframe não está vazio
        if df is not None:
            st.subheader('Dados Importados:')
            st.write(df.head())  # Exibe os primeiros registros do dataframe
            
            # Exemplo de criação de gráfico usando Altair
            st.subheader('Gráfico de Exemplo:')
            chart = alt.Chart(df).mark_bar().encode(
                x='Year:O',
                y='value:Q',
                color='category:N'
            ).properties(
                width=600,
                height=400
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.error('Erro ao carregar o arquivo. Verifique o tipo de arquivo selecionado.')

elif pagina == 'Fale Conosco':
    st.title('Saiba mais sobre nossos serviços ou solicite uma proposta agora mesmo')
    st.markdown(f'<iframe width="800" height="600" src="{Url_Form_contato}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
