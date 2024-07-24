import streamlit as st
from datetime import datetime
from babel.dates import format_date
import pandas as pd

# Incluir a logo acima do menu de navegação lateral
st.image("baner.png", use_column_width=True)

# Imagens redes sociais
 
# Título streamlit
titulo = st.title("""
PORTIFÓLIO DE TRABALHO E ANÁLISE DE DADOS
Formado em Administração de Empresas pela faculdade Pitágoras e Pós graduado em Ciência e Analise dados pela faculdade Estacio.
Projeto desenvolvido em linguagem 100% Python com Streamlit.
                  
"Quanto mais profundo e sólidos forem os motivos básicos de uma pessoa, 
maior será a certeza do sucesso de sua empreitada" Lucas 6:48.
""")

# Adicionar a logo acima do menu de navegação lateral
st.sidebar.image("LOGO.png", use_column_width=True)  # Substitua "logo.png" pelo caminho da sua imagem

# Componentes na barra lateral para navegação
st.sidebar.title('Menu de Navegação')


# Menu PBIX
pagina = st.sidebar.selectbox(
    'Conheça mais sobre meus serviços:',
    ['Selecione uma opção','_____Power BI______','Apresentação',
     'Análise Roteirização',
     'Gestão',
     'Fale Conosco']
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
gestao = "https://app.powerbi.com/reportEmbed?reportId=4d5370c4-4720-44b0-a195-bd194ed3531a&autoAuth=true&ctid=32341a06-b690-4834-94a3-d0b2f7bda7e0"

if pagina == 'Apresentação':
    st.markdown("""
    ## Bem-vindo (a) à minha página de trabalhos produzidos em Power BI, Python, Microsoft Access e Microsoft Excel
    
    Me chamo Williams Rodrigues, sou pós-graduando em Ciência de Dados e bacharel em administração de empresas. Atualmente, trabalho no setor logístico.
    
    Sempre tive paixão pela área de tecnologia, onde fiz vários cursos como Web Designer, linguagem CSS6, HTML, Portugol, Python, VBA com Access.
    
    Agradeço a Deus por toda sabedoria em meus estudos, e também gostaria de agradecer a meu pai, Luiz da Silva, por ser meu motivador e inspirador em meus valores, princípios e ética pessoal. Também quero agradecer minha esposa, Luciene Gomes, pelos momentos de compreensão e paciência durante meu aprendizado.
    
    O Desenvolvimento em Python ocorreu em meu currículo em 2024 após realizar um desejo e vontade pessoal em retomar os estudos na área de tecnólogia,
    Foi ai que resolvi me matricular no curso de pós graduação em CIÊNCIA E BIG DATA ANALYTICS pela faculdade Estacio e ai fiquei tão fascinado com esta linguagem,
    que comecei a realizar alguns projetos pessoais.
                
    Contatos: (082)98863-9394
                
    Email: wr.rodriguesvieira@outlook.com
    """)

elif pagina == 'Análise Roteirização':
    st.title('Mapeamento e Análise de Dados do Planejamento de Roteirização')
    st.markdown(f'<iframe width="800" height="600" src="{roteirizacao}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif pagina == 'Gestão':
    st.title('Mapeamento e Analise de gestão Completa')
    st.markdown('Este projeto visa realizar uma analise de indicadores de gesão para acompanhar uma gestão empresarial em diversos setores')
    st.markdown(f'<iframe width="800" height="600" src="{gestao}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

        
elif pagina == 'Fale Conosco':
    st.title('Saiba mais sobre nossos serviços ou solicite uma proposta agora mesmo')
    st.markdown(f'<iframe width="800" height="600" src="{Url_Form_contato}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

#Redes Sociais
st.title('Siga-nos em nossas redes sociais')
st.link_button('Whatsapp','https://wa.me/5582988639394')
st.link_button('Linkedin','https://www.linkedin.com/in/williams-rodrigues-9b350a6a')
st.link_button('Instagram','https://www.instagram.com/williams_rvs85')
#link de apoio:
link_instagram=('https://www.instagram.com/williams_rvs85') 
link_linkedin=('https://www.linkedin.com/in/williams-rodrigues-9b350a6a')
link_whatsapp=('https://wa.me/5582988639394')

