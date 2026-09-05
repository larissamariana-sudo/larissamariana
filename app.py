import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Prof. Dr(a). Larissa Mariana | Fisioterapia & Docência",
    page_icon="🩺",
    layout="wide"
)

# Estilização visual para os espaços de imagem e layout
st.markdown("""
    <style>
    .placeholder-img { 
        background-color: #f0f2f6; 
        color: #555; 
        padding: 40px; 
        text-align: center; 
        border: 2px dashed #b0c4de; 
        border-radius: 8px;
        margin-bottom: 15px; 
        font-weight: 500;
    }
    .main-header { font-size: 2.5rem; color: #004a80; }
    </style>
""", unsafe_allow_html=True)

# Função para carregar os dados da sua planilha do Google Sheets
@st.cache_data(ttl=600)
def carregar_dados_planilha():
    # Substitua o link abaixo pelo link CSV público da sua planilha do Google Sheets (/export?format=csv)
    url_csv = "COLE_O_LINK_CSV_DA_SUA_PLANILHA_AQUI"
    try:
        df = pd.read_csv(url_csv)
        return df
    except:
        return pd.DataFrame(columns=["Secao", "Titulo", "Descricao", "Link"])

df_site = carregar_dados_planilha()

# ==========================================
# 1. FOTO DE CAPA DO SITE
# ==========================================
# Para substituir: st.image("imagens/capa.jpg", use_container_width=True)
st.markdown('<div class="placeholder-img">🖼️ Coloque sua foto de capa aqui (Sugestão: 1200x300px)</div>', unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Prof. Dr(a). Larissa Mariana Veloso de Oliveira</h1>', unsafe_allow_html=True)
st.markdown("### Fisioterapeuta | Coordenadora do Curso de Fisioterapia — PUC Goiás[cite: 1, 2]")
st.markdown("---")

# Abas de Navegação
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📂 Sobre & Lattes", 
    "💼 Serviços", 
    "🎓 Cursos & Pesquisas", 
    "🔍 Validar Certificado", 
    "📚 E-books & Publicações"
])

# ==========================================
# ABA 1: SOBRE & LATTES
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        # Para substituir: st.image("imagens/perfil.jpg", use_container_width=True)
        st.markdown('<div class="placeholder-img" style="padding: 60px 10px;">📷 Foto de Perfil</div>', unsafe_allow_html=True)
        st.caption("Fisioterapeuta - PUC Goiás[cite: 1, 2]")
        
    with col2:
        st.header("Sobre Mim")
        st.write("""
        Graduada pela UNESP, Mestre pela Universitat Internacional de Catalunya e Doutoranda pela Universidad de Palermo[cite: 2]. 
        Docente da PUC Goiás desde 2005 e Coordenadora do Curso de Fisioterapia desde 2011[cite: 2]. Atuação destacada em reabilitação, 
        saúde pública, preceptoria e gestão acadêmica, com premiações pelo Ministério da Saúde e Assembleia Legislativa de Goiás (ALEGO)[cite: 2].
        """)
        
        # Pilares institucionais
        c1, c2, c3 = st.columns(3)
        c1.metric("Docência", "PUC Goiás[cite: 1, 2]")
        c2.metric("Coordenação", "Fisioterapia[cite: 1, 2]")
        c3.metric("Atuação", "Clínica & Pesquisa[cite: 2]")
        
        st.markdown("---")
        st.link_button("📄 Ver Currículo Lattes Completo", "http://lattes.cnpq.br/1002411477807507")

# ==========================================
# ABA 2: SERVIÇOS
# ==========================================
with tab2:
    st.header("Contratação de Serviços")
    st.write("Agende avaliações especializadas, mentorias clínicas ou consultorias na área de Fisioterapia.")
    
    # Para substituir: st.image("imagens/servicos.jpg", use_container_width=True)
    st.markdown('<div class="placeholder-img">🖼️ Coloque a imagem ilustrativa dos serviços aqui</div>', unsafe_allow_html=True)
    
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
# ABA 3: CURSOS E PESQUISAS (PET-Saúde)
# ==========================================
with tab3:
    st.header("Projetos, Cursos e Extensão")
    st.write("Acompanhe as iniciativas acadêmicas, tutorias do PET-Saúde e capacitações.")
    
    # Para substituir: st.image("imagens/cursos.jpg", use_container_width=True)
    st.markdown('<div class="placeholder-img">🖼️ Coloque a imagem de eventos ou banner aqui</div>', unsafe_allow_html=True)
    
    # Puxando dados da planilha categorizados como 'cursos' ou 'pesquisa'
    dados_pesq = df_site[df_site['Secao'].isin(['cursos', 'pesquisa'])] if not df_site.empty else pd.DataFrame()
    
    if not dados_pesq.empty:
        for _, row in dados_pesq.iterrows():
            with st.container(border=True):
                st.subheader(row['Titulo'])
                st.write(row['Descricao'])
                if pd.notna(row['Link']) and row['Link'] != "":
                    st.link_button("Acessar Detalhes", row['Link'])
    else:
        st.info("Cadastre seus cursos e projetos na planilha do Google Sheets para exibi-los aqui.")

# ==========================================
# ABA 4: VERIFICAÇÃO DE CERTIFICADOS
# ==========================================
with tab4:
    st.header("Verificação de Autenticidade de Certificados")
    st.write("Digite o código alfanumérico impresso no seu certificado para comprovar sua validade na PUC Goiás.")
    
    # Para substituir: st.image("imagens/certificados.jpg", use_container_width=True)
    st.markdown('<div class="placeholder-img">🖼️ Coloque uma imagem ilustrativa de validação/certificados aqui</div>', unsafe_allow_html=True)
    
    codigo_input = st.text_input("Código do Certificado (Ex: PUC-FISIO-2026-001)").strip()
    
    if st.button("Verificar Autenticidade"):
        base_certificados = {
            "PUC-FISIO-001": {"valido": True, "curso": "Atualidades em Fisioterapia", "data": "2026", "carga": "20h"}
        }
        if codigo_input in base_certificados:
            cert = base_certificados[codigo_input]
            st.success("✅ **Certificado Válido e Autêntico!**")
            st.write(f"- **Curso/Evento:** {cert['curso']}")
            st.write(f"- **Instituição:** PUC Goiás[cite: 1, 2]")
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
    
    dados_pub = df_site[df_site['Secao'].isin(['ebooks', 'publicacoes'])] if not df_site.empty else pd.DataFrame()
    
    if not dados_pub.empty:
        for _, row in dados_pub.iterrows():
            with st.container(border=True):
                st.subheader(row['Titulo'])
                st.write(row['Descricao'])
                if pd.notna(row['Link']) and row['Link'] != "":
                    st.link_button("📖 Acessar Publicação / Lattes", row['Link'])
    else:
        st.write("Cadastre seus e-books e artigos na planilha do Google Sheets.")

# Rodapé padrão
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 Prof. Dr(a). Larissa Mariana Veloso de Oliveira • Fisioterapia PUC Goiás[cite: 1, 2] • Todos os direitos reservados.</p>", 
    unsafe_allow_html=True
)
