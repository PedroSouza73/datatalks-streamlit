import streamlit as st
import pandas as pd
import google.generativeai as genai
import plotly.express as px
from collections import Counter
import re
import time

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def analisar_sentimento(texto):
    prompt = f"Classifique o seguinte feedback como positivo, negativo ou neutro:\n\n'{texto}'"
    response = model.generate_content([prompt])
    return response.text.strip()

def resumir_texto(texto):
    prompt = f"Resuma objetivamente o seguinte feedback de cliente:\n\n'{texto}'"
    response = model.generate_content([prompt])
    return response.text.strip()

def analisar_sentimentos_com_delay(lista_feedbacks):
    resultados = []
    for i, texto in enumerate(lista_feedbacks):
        resultados.append(analisar_sentimento(texto))
        if (i + 1) % 15 == 0:
            time.sleep(60)
        else:
            time.sleep(4)
    return resultados

def resumir_feedbacks_com_delay(lista_feedbacks):
    resultados = []
    for i, texto in enumerate(lista_feedbacks):
        resultados.append(resumir_texto(texto))
        if (i + 1) % 15 == 0:
            time.sleep(60)
        else:
            time.sleep(4)
    return resultados

def extrair_palavras_chave(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    stopwords = set(["de", "da", "do", "que", "em", "para", "com", "uma", "os", "as", "por", "o", "a", "e"])
    palavras_filtradas = [p for p in palavras if p not in stopwords and len(p) > 3]
    return Counter(palavras_filtradas).most_common(10)

st.set_page_config(page_title="DataTalks - Análise Inteligente de Feedbacks", layout="wide")
st.title("DataTalks \U0001F4AC - Análise Inteligente de Feedbacks com IA")

st.markdown("""
Este aplicativo SaaS usa inteligência artificial para:
- Classificar sentimentos de feedbacks (positivo, negativo ou neutro)
- Resumir os feedbacks
- Extrair palavras-chave mais frequentes
""")

uploaded_file = st.file_uploader("\n\nFaça upload de um arquivo CSV com a coluna 'feedback'", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'feedback' not in df.columns:
        st.error("O arquivo deve conter uma coluna chamada 'feedback'.")
    else:
        st.subheader("Visualização inicial do arquivo")
        st.dataframe(df.head())

        if st.button("Analisar Feedbacks com IA"):
            with st.spinner("Analisando sentimentos (limite de 15 chamadas por minuto)..."):
                df['sentimento'] = analisar_sentimentos_com_delay(df['feedback'].tolist())
            
            with st.spinner("Resumindo feedbacks (limite de 15 chamadas por minuto)..."):
                df['resumo'] = resumir_feedbacks_com_delay(df['feedback'].tolist())

            texto_total = " ".join(df['feedback'].tolist())
            palavras_chave = extrair_palavras_chave(texto_total)

            st.subheader("Resultado da Análise")
            st.dataframe(df)

            st.subheader("Gráfico de Sentimentos")
            grafico = px.histogram(df, x='sentimento', title="Distribuição dos Sentimentos", color='sentimento')
            st.plotly_chart(grafico)

            st.subheader("Top 10 Palavras-chave")
            for palavra, freq in palavras_chave:
                st.markdown(f"- **{palavra}**: {freq} ocorrências")

            st.download_button("Baixar CSV com resultados", df.to_csv(index=False).encode('utf-8'), file_name="feedbacks_analisados.csv", mime='text/csv')

else:
    st.info("Aguardando upload de arquivo CSV com coluna 'feedback'.")
