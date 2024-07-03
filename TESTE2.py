import streamlit as st
from datetime import datetime
from babel.dates import format_date
import pandas as pd

# Incluir a logo acima do menu de navegação lateral
st.image("baner.png", use_column_width=True)

# Adicionar ícones de redes sociais
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
        <a href="https://www.instagram.com/williams_rvs85" target="_blank" style="margin-right: 20px;">
            <img src="instagram.png" width="40" height="40">
        </a>
        <a href="https://www.linkedin.com/in/Williams (Williams Rodrigues)
" target="_blank">
            <img src="linkedin.png" width="40" height="40">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

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


# Campo de texto para entrada do número de WhatsApp
numero_zap = st.sidebar.text_input('converta um número WhatsApp (com código do país, ex: 5582999999999)')

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
    st.title('ESTAMOS EM MANUTENÇÃO')
    
    
elif pagina == 'Fale Conosco':
    st.title('Saiba mais sobre nossos serviços ou solicite uma proposta agora mesmo')
    st.markdown(f'<iframe width="800" height="600" src="{Url_Form_contato}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

