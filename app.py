
import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Perfil Profissional", layout="wide")

# Estilização básica
st.markdown('''
    <style>
    .placeholder-img { background-color: #e0e0e0; color: #757575; padding: 50px; text-align: center; border: 2px dashed #9e9e9e; margin-bottom: 10px; }
    </style>
''', unsafe_allow_html=True)

# 1. Capa
st.markdown('<div class="placeholder-img">Coloque sua foto de capa aqui (1200x300px)</div>', unsafe_allow_html=True)

st.title("Prof. Dr(a). [Seu Nome]")
st.subheader("Fisioterapeuta | Docente da PUC Goiás")

# Abas
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Sobre/Lattes", "Serviços", "Cursos/Palestras", "Certificados", "E-books"])

with tab1:
    st.header("Sobre Mim")
    st.markdown('<div class="placeholder-img">Foto de perfil aqui</div>', unsafe_allow_html=True)
    st.write("Atuação dedicada à reabilitação funcional, pesquisa e ensino na PUC Goiás.")
    st.link_button("Acessar Currículo Lattes", "https://lattes.cnpq.br/")

with tab2:
    st.header("Serviços")
    st.markdown('<div class="placeholder-img">Imagem representativa de serviços</div>', unsafe_allow_html=True)
    with st.form("form_servico"):
        nome = st.text_input("Nome")
        contato = st.text_input("WhatsApp/E-mail")
        msg = st.text_area("O que deseja contratar?")
        if st.form_submit_button("Enviar Solicitação"):
            st.success("Solicitação enviada!")

with tab3:
    st.header("Cursos e Palestras")
    st.markdown('<div class="placeholder-img">Imagem de evento</div>', unsafe_allow_html=True)
    st.write("Próximos eventos...")
    st.button("Inscrever-se")

with tab4:
    st.header("Validação de Certificados")
    codigo = st.text_input("Insira o código do certificado")
    if st.button("Verificar"):
        st.info(f"Validando código: {codigo}...")

with tab5:
    st.header("E-books")
    st.markdown('<div class="placeholder-img">Imagem/Capa do E-book</div>', unsafe_allow_html=True)
    st.write("Material acadêmico disponível para download.")
    st.button("Baixar E-book")
