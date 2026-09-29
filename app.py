import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Prof. Dr(a). Larissa Mariana | Fisioterapia & Docência",
    page_icon="🩺",
    layout="wide"
)

# Renderizando o conteúdo HTML/CSS do site dentro do Streamlit
st.components.v1.html("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prof. Dr(a). Larissa Mariana | Fisioterapia & Docência</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .container {
            padding: 40px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h1 { color: #004a80; margin-bottom: 10px; }
        p { color: #555; font-size: 1.1rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Prof. Dr(a). Larissa Mariana</h1>
        <p>Fisioterapeuta | Coordenadora do Curso de Fisioterapia — PUC Goiás</p>
        <p>Bem-vinda ao seu ambiente acadêmico e clínico oficial.</p>
    </div>
</body>
</html>
""", height=600, scrolling=True)
