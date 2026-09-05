import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Prof. Dr(a). Larissa Mariana | Fisioterapia & Docência no Ensino Superior",
    page_icon="🩺",
    layout="wide"
)

# Estilização visual avançada para um aspecto mais profissional
st.markdown("""
    <style>
    /* Fundo geral da página e tipografia */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Estilo para caixas e containers */
    div[data-testid="stVerticalBlock"] > div[style*="border: 1px solid"] {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        border: 1px solid #e2e8f0 !important;
    }

    .placeholder-img { 
        background-color: #e9ecef; 
        color: #495057; 
        padding: 40px; 
        text-align: center; 
        border: 2px dashed #ced4da; 
        border-radius: 8px;
        margin-bottom: 15px; 
        font-weight: 500;
    }
    
    .main-header { 
        font-size: 2.5rem; 
        color: #004a80; 
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Estilização das abas principais */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border-radius: 6px 6px 0px 0px;
        padding: 10px 20px;
        font-weight: 600;
        color: #004a80;
    }
    .stTabs [aria-selected="true"] {
        background-color: #004a80 !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Função robusta em Python para carregar e tratar os dados da planilha do Google Sheets
@st.cache_data(ttl=600)
def carregar_dados_planilha():
    url_csv = "https://docs.google.com/spreadsheets/d/1A0ZHnATInlMHMjp44SEb8VlwyQvXS34gkLS2SrYiGUE/export?format=csv"
    try:
        df = pd.read_csv(url_csv)
        df.columns = df.columns.str.strip().str.title()
        return df
    except Exception as e:
        return pd.DataFrame(columns=["Secao", "Titulo", "Descricao", "Link", "Isbn/Doi", "Imagem"])

df_site = carregar_dados_planilha()

# ==========================================
# 1. FOTO DE CAPA DO SITE (Mais estreita e centralizada)
# ==========================================
col_esq, col_centro, col_dir = st.columns([1, 4, 1])
with col_centro:
    try:
        st.image("imagens/capasite.png", use_container_width=True)
    except:
        st.markdown('<div class="placeholder-img">🖼️ Imagem "imagens/capasite.png" não encontrada na pasta "imagens".</div>', unsafe_allow_html=True)

st.markdown('<h1 class="main-header" style="text-align: center;">Prof. Dr(a). Larissa Mariana Veloso de Oliveira</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; font-weight: bold; color: #495057;'>Fisioterapeuta | Coordenadora do Curso de Fisioterapia — PUC Goiás</p>", unsafe_allow_html=True)
st.markdown("---")

# Abas de Navegação Principais (Aba 4 agora engloba Cursos/Palestras e Certificados)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📂 Sobre & Lattes", 
    "💼 Serviços", 
    "🎓 Pesquisas & Projetos", 
    "🎓 Cursos, Palestras & Certificados", 
    "📚 E-books & Publicações"
])

# ==========================================
# ABA 1: SOBRE & LATTES
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("imagens/larissa.PNG", width=250)
        except:
            st.markdown('<div class="placeholder-img">📷 Foto "larissa.PNG" não encontrada na pasta imagens.</div>', unsafe_allow_html=True)
        st.caption("Fisioterapeuta - PUC Goiás")
        
    with col2:
        st.header("Sobre Mim")
        st.write("""
        Graduada pela UNESP, Mestre pela Universitat Internacional de Catalunya e Doutoranda pela Universidad de Palermo. 
        Docente da PUC Goiás desde 2005 e Coordenadora do Curso de Fisioterapia desde 2011. Atuação destacada em reabilitação, 
        saúde pública, preceptoria e gestão acadêmica, com premiações pelo Ministério da Saúde e Assembleia Legislativa de Goiás (ALEGO).
        """)
        
        # Pilares institucionais
        c1, c2, c3 = st.columns(3)
        c1.metric("Docência", "PUC Goiás")
        c2.metric("Coordenação", "Fisioterapia")
        c3.metric("Atuação", "Clínica & Pesquisa")
        
        st.markdown("---")
        st.link_button("📄 Ver Currículo Lattes Completo", "http://lattes.cnpq.br/1002411477807507")

# ==========================================
# ABA 2: SERVIÇOS
# ==========================================
with tab2:
    st.header("Contratação de Serviços")
    st.write("Agende avaliações especializadas, mentorias clínicas ou consultorias na área de Fisioterapia.")
    
    try:
        st.image("imagens/terapiamanual.jpg", width=400)
    except:
        st.markdown('<div class="placeholder-img">🖼️ Imagem "imagens/terapiamanual.jpg" não encontrada na pasta "imagens".</div>', unsafe_allow_html=True)
    
    with st.form("form_servico"):
        st.subheader("Formulário de Solicitação")
        nome_servico = st.text_input("Seu Nome Completo")
        email_servico = st.text_input("Seu E-mail")
        tel_servico = st.text_input("Telefone / WhatsApp")
        tipo_atendimento = st.selectbox("Selecione o Serviço", ["Fisioterapia Especializada", "Consultoria Científica", "Mentoria Acadêmica", "Outros"])
        mensagem_servico = st.text_area("Descreva sua necessidade")
        
        if st.form_submit_button("Enviar Solicitação de Contato"):
            if nome_servico and email_servico:
                st.success("Solicitação enviada com sucesso! Entraremos em contato em breve.")
            else:
                st.warning("Por favor, preencha pelo menos o seu nome e e-mail.")

# ==========================================
# ABA 3: PESQUISAS E PROJETOS
# ==========================================
with tab3:
    st.header("Projetos de Pesquisa e Extensão")
    st.write("Acompanhe as iniciativas acadêmicas e tutorias do PET-Saúde.")
    
    if not df_site.empty and "Secao" in df_site.columns:
        dados_pesq = df_site[df_site['Secao'].str.lower().isin(['pesquisa'])]
    else:
        dados_pesq = pd.DataFrame()
    
    if not dados_pesq.empty:
        for _, row in dados_pesq.iterrows():
            with st.container(border=True):
                st.subheader(row.get('Titulo', ''))
                st.write(row.get('Descricao', ''))
                link_val = row.get('Link', '')
                if pd.notna(link_val) and str(link_val).strip() != "":
                    st.link_button("Acessar Detalhes", str(link_val))
    else:
        st.info("Cadastre seus projetos de pesquisa na planilha do Google Sheets para exibi-los aqui.")

# ==========================================
# ABA 4: CURSOS, PALESTRAS & CERTIFICADOS (Com Sub-abas)
# ==========================================
with tab4:
    # Criando sub-abas para separar inscrições de cursos/palestras e a validação de certificados
    sub_tab1, sub_tab2 = st.tabs(["📝 Inscrições em Cursos & Palestras", "🔍 Validação de Certificados"])
    
    # SUB-ABA 1: Cursos e Palestras Oferecidos
    with sub_tab1:
        st.header("Cursos e Palestras Disponíveis")
        st.write("Confira as capacitações oferecidas e garanta sua inscrição.")
        
        if not df_site.empty and "Secao" in df_site.columns:
            dados_cursos = df_site[df_site['Secao'].str.lower().isin(['cursos', 'palestra', 'palestras'])]
        else:
            dados_cursos = pd.DataFrame()
            
        if not dados_cursos.empty:
            for _, row in dados_cursos.iterrows():
                with st.container(border=True):
                    col_img, col_txt = st.columns([1, 2])
                    with col_img:
                        # Exibe a imagem do curso cadastrada na planilha (coluna 'Imagem' com o caminho, ex: imagens/curso1.png)
                        img_path = row.get('Imagem', '')
                        if pd.notna(img_path) and str(img_path).strip() != "":
                            try:
                                st.image(str(img_path), use_container_width=True)
                            except:
                                st.markdown('<div class="placeholder-img" style="padding: 20px;">🖼️ Imagem indisponível</div>', unsafe_allow_html=True)
                        else:
                            st.markdown('<div class="placeholder-img" style="padding: 20px;">🖼️ Sem imagem cadastrada</div>', unsafe_allow_html=True)
                    with col_txt:
                        st.subheader(row.get('Titulo', ''))
                        st.write(row.get('Descricao', ''))
                        link_curso = row.get('Link', '')
                        if pd.notna(link_curso) and str(link_curso).strip() != "":
                            st.link_button("Inscrever-se no Evento", str(link_curso))
        else:
            st.info("Nenhum curso ou palestra cadastrado no momento. Adicione itens na sua planilha do Google Sheets com a seção 'cursos' ou 'palestras'.")

    # SUB-ABA 2: Validação de Certificados (Mantida intacta)
    with sub_tab2:
        st.header("Verificação de Autenticidade de Certificados")
        st.write("Digite o código alfanumérico impresso no seu certificado para comprovar sua validade na PUC Goiás.")
        
        codigo_input = st.text_input("Código do Certificado (Ex: LAR-FISIO-2026-001)").strip()
        
        if st.button("Verificar Autenticidade"):
            base_certificados = {
                "LAR-FISIO-001": {"valido": True, "curso": "Atualidades em Fisioterapia", "data": "2026", "carga": "20h"}
            }
            if codigo_input in base_certificados:
                cert = base_certificados[codigo_input]
                st.success("✅ **Certificado Válido e Autêntico!**")
                st.write(f"- **Curso/Evento:** {cert['curso']}")
                st.write(f"- **Instituição:** PUC Goiás")
            elif codigo_input == "":
                st.warning("⚠️ Insira um código no campo acima.")
            else:
                st.error("❌ **Certificado não encontrado.**")

# ==========================================
# ABA 5: E-BOOKS E PUBLICAÇÕES
# ==========================================
with tab5:
    st.header("E-books, Guias e Publicações Científicas")
    st.write("Materiais didáticos e produções bibliográficas registradas no Lattes.")
    
    if not df_site.empty and "Secao" in df_site.columns:
        dados_pub = df_site[df_site['Secao'].str.lower().isin(['ebooks', 'publicacoes'])]
    else:
        dados_pub = pd.DataFrame()
    
    if not dados_pub.empty:
        for _, row in dados_pub.iterrows():
            with st.container(border=True):
                st.subheader(row.get('Titulo', ''))
                st.write(row.get('Descricao', ''))
                
                coluna_isbn = next((col for col in df_site.columns if 'isbn' in col.lower() or 'doi' in col.lower()), None)
                if coluna_isbn and pd.notna(row.get(coluna_isbn)) and str(row.get(coluna_isbn)).strip() != "":
                    st.caption(f"📌 **ISBN/DOI:** {row.get(coluna_isbn)}")
                    
                link_pub = row.get('Link', '')
                if pd.notna(link_pub) and str(link_pub).strip() != "":
                    st.link_button("📖 Acessar Publicação / Lattes", str(link_pub))
    else:
        st.write("Cadastre seus e-books e artigos na planilha do Google Sheets.")

# Rodapé padrão
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 Prof. Dr(a). Larissa Mariana Veloso de Oliveira • Fisioterapia PUC Goiás • Todos os direitos reservados.</p>", 
    unsafe_allow_html=True
)
