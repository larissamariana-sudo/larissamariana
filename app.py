import streamlit as st

# Configuração da página (deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="Nome do Seu Site / Projeto",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CARREGAR ESTILOS OPCIONAIS (CSS customizado se necessário) ---
# st.markdown('<link rel="stylesheet" href="./assets/style.css">', unsafe_allow_html=True)

# --- MENU LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image(
        "https://via.placeholder.com/150", width=120
    )  # Substitua pelo seu logo em assets/
    st.title("Navegação")
    st.markdown("---")
    st.markdown("### Contato & Links")
    st.markdown(
        "- [GitHub](https://github.com/seu-usuario)\n- [LinkedIn](https://linkedin.com/in/seu-perfil)"
    )
    st.markdown("---")
    st.caption("Desenvolvido com Streamlit & Python")

# --- CONTEÚDO PRINCIPAL (HERO SECTION) ---
st.title("Bem-vindo ao Portal Profissional 🚀")
st.subheader(
    "Soluções inovadoras, educação baseada em evidências e tecnologia."
)

st.markdown("""
Este espaço foi construído para centralizar projetos, recursos educacionais e ferramentas interativas. 
Utilize o menu lateral para navegar entre as seções ou explorar as páginas dedicadas.
""")

st.markdown("---")

# --- SEÇÃO DE DESTAQUES / MÉTRICAS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Projetos Ativos", value="12+", delta="2 novos este mês"
    )

with col2:
    st.metric(label="Recursos Publicados", value="45", delta="100% Acesso Livre")

with col3:
    st.metric(label="Colaborações", value="8 Instituições", delta="Internacional")

st.markdown("---")

# --- SEÇÃO DE ABAS (TABS INTERATIVAS) ---
tab1, tab2, tab3 = st.tabs(
    ["Visão Geral", "Áreas de Atuação", "Últimas Atualizações"]
)

with tab1:
    st.markdown("### Sobre a Iniciativa")
    st.write(
        "Aqui você pode detalhar a proposta principal do seu site, missão, visão e objetivos estratégicos."
    )
    # Exemplo de container visual
    with st.container(border=True):
        st.info(
            "💡 **Dica:** Você pode organizar seções complexas utilizando cards e containers."
        )

with tab2:
    st.markdown("### Principais Focos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("- **Educação e Metodologias Ativas**")
         experiential_text = "Desenvolvimento de ferramentas gamificadas e plataformas de ensino."
        st.write(experiential_text)
    with col_b:
        st.markdown("- **Pesquisa e Tecnologia**")
        st.write(
            "Análise de dados, automação em Python e soluções web eficientes."
        )

with tab3:
    st.markdown("### Linha do Tempo / Notícias")
    st.write("- **Setembro/2026:** Lançamento da nova arquitetura do portal.")
    st.write("- **Julho/2026:** Atualização de materiais e novas publicações.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 — Todos os direitos reservados.</p>",
    unsafe_allow_html=True,
)
