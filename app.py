import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Larissa Mariana | Fisioterapia e Docência",
    page_icon="🩺",
    layout="wide",
)

URL_PLANILHA = (
    "https://docs.google.com/spreadsheets/d/"
    "1A0ZHnATInlMHMjp44SEb8VlwyQvXS34gkLS2SrYiGUE/"
    "export?format=csv"
)
URL_LATTES = "http://lattes.cnpq.br/1002411477807507"

# Estilização profissional incorporando o design system da LAMAVEO
st.markdown(
    """
    <style>
    /* Configuração de fundo global e tipografia */
    .stApp {
        background-color: #f7f7f5 !important;
        color: #182746 !important;
        font-family: Inter, Arial, sans-serif !important;
    }
    
    /* Cabeçalho estilo Barra LAMAVEO no topo */
    .lamaveo-header {
        background-color: #182746;
        color: white;
        padding: 16px 28px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 8px;
        margin-bottom: 30px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .lamaveo-brand {
        font-family: Georgia, serif;
        font-weight: bold;
        font-size: 24px;
        letter-spacing: 0.12em;
        color: white;
        text-decoration: none;
    }
    .lamaveo-tag {
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: #f5aa89;
        font-weight: 700;
    }

    /* Títulos e Tipografia com Georgia */
    h1, h2, h3, .titulo {
        color: #182746 !important;
        font-family: Georgia, serif !important;
    }
    
    .titulo {
        font-size: 2.8rem; 
        font-weight: 700; 
        line-height: 1.15;
    }
    
    .subtitulo {
        font-size: 1.15rem; 
        color: #536073;
        font-family: Inter, Arial, sans-serif;
        margin-bottom: 20px;
    }

    /* Estilização moderna das abas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd0d6 !important;
        border-radius: 6px 6px 0px 0px !important;
        font-weight: 600;
        color: #182746 !important;
        padding: 10px 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #182746 !important;
        color: #ffffff !important;
        border-color: #182746 !important;
    }

    /* Botões interativos com o tom coral LAMAVEO */
    .stButton button, .stLinkButton a {
        background-color: #182746 !important;
        color: #ffffff !important;
        border-radius: 6px;
        font-weight: 600;
    }
    .stButton button:hover, .stLinkButton a:hover {
        background-color: #f39472 !important;
        color: #182746 !important;
    }
    </style>
    
    <!-- Barra de Navegação Superior da Marca -->
    <div class="lamaveo-header">
        <span class="lamaveo-brand">LAMAVEO & ACADÊMICO</span>
        <span class="lamaveo-tag">Plataforma Profissional & Editora</span>
    </div>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(ttl=600)
def carregar_conteudo():
    try:
        dados = pd.read_csv(URL_PLANILHA).fillna("")
        dados.columns = [
            coluna.strip().lower()
            for coluna in dados.columns
        ]
        return dados
    except Exception:
        return pd.DataFrame(
            columns=["secao", "titulo", "descricao", "link", "isbn/doi"]
        )


def itens_da_secao(dados, secoes):
    if "secao" not in dados.columns:
        return pd.DataFrame()

    return dados[
        dados["secao"].astype(str).str.strip().str.lower().isin(secoes)
    ]


def mostrar_cards(dados, mensagem_vazia, mostrar_link=True):
    if dados.empty:
        st.info(mensagem_vazia)
        return

    for _, item in dados.iterrows():
        with st.container(border=True):
            st.subheader(str(item.get("titulo", "")))

            descricao = str(item.get("descricao", "")).strip()
            if descricao:
                st.write(descricao)

            identificador = str(
                item.get("isbn/doi", item.get("isbn", item.get("doi", "")))
            ).strip()
            if identificador:
                st.caption(f"ISBN/DOI: {identificador}")

            link = str(item.get("link", "")).strip()
            if mostrar_link and link.startswith(("https://", "http://")):
                st.link_button("Acessar conteúdo", link)


dados = carregar_conteudo()

# Bloco Principal do Perfil
st.markdown(
    '<div class="titulo">Larissa Mariana Veloso de Oliveira</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitulo">Fisioterapeuta • Docente • Coordenadora do curso de Fisioterapia da PUC Goiás</p>',
    unsafe_allow_html=True,
)

st.divider()

# Abas de Navegação
sobre, servicos, projetos, cursos, publicacoes = st.tabs(
    [
        "Sobre",
        "Serviços",
        "Projetos",
        "Cursos e palestras",
        "Publicações",
    ]
)

with sobre:
    st.header("Sobre")
    st.write(
        "Graduada pela UNESP, mestre pela Universitat Internacional de "
        "Catalunya e doutoranda pela Universidad de Palermo. É docente da "
        "PUC Goiás desde 2005 e coordenadora do curso de Fisioterapia "
        "desde 2011."
    )
    st.write(
        "Sua atuação reúne reabilitação, saúde pública, preceptoria e "
        "gestão acadêmica."
    )
    st.link_button("Ver currículo Lattes", URL_LATTES)

with servicos:
    st.header("Serviços")
    st.write(
        "Informações sobre fisioterapia especializada, consultoria "
        "científica e mentoria acadêmica."
    )

    with st.form("solicitacao"):
        nome = st.text_input("Nome completo")
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone / WhatsApp")
        servico = st.selectbox(
            "Serviço",
            [
                "Fisioterapia especializada",
                "Consultoria científica",
                "Mentoria acadêmica",
                "Outros",
            ],
        )
        mensagem = st.text_area("Descreva sua necessidade")
        enviar = st.form_submit_button("Preparar solicitação")

    if enviar:
        if not nome or not email:
            st.warning("Preencha seu nome e e-mail.")
        else:
            st.info(
                "Solicitação preparada. Para receber mensagens pelo site, "
                "é necessário configurar um endereço de destino ou "
                "serviço de envio de e-mails."
            )
            st.code(
                f"Nome: {nome}\n"
                f"E-mail: {email}\n"
                f"Telefone: {telefone}\n"
                f"Serviço: {servico}\n"
                f"Mensagem: {mensagem}"
            )

with projetos:
    st.header("Projetos de pesquisa e extensão")
    mostrar_cards(
        itens_da_secao(dados, {"pesquisa"}),
        "Nenhum projeto cadastrado no momento.",
    )

with cursos:
    st.header("Cursos e palestras")
    st.write("Atividades de formação continuada disponíveis.")
    mostrar_cards(
        itens_da_secao(dados, {"cursos", "palestra", "palestras"}),
        "Nenhum curso ou palestra cadastrado no momento.",
        mostrar_link=False,
    )

with publicacoes:
    st.header("E-books e publicações")
    mostrar_cards(
        itens_da_secao(dados, {"ebooks", "publicacoes"}),
        "Nenhuma publicação cadastrada no momento.",
    )

st.divider()
st.caption("© 2026 Larissa Mariana Veloso de Oliveira • LAMAVEO Acadêmico")
