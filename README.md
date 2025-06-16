# datatalks-streamlit

# 💬 DataTalks - Análise Inteligente de Feedbacks com IA

DataTalks é um aplicativo SaaS desenvolvido com Streamlit que utiliza Inteligência Artificial (Google Gemini) para analisar feedbacks de clientes. Ele processa arquivos CSV contendo comentários e fornece:

# 💬 Funcionalidades

✅ Upload de arquivos .csv contendo feedbacks
✅ Análise de sentimento (positivo, negativo ou neutro)  
✅ Resumo dos feedbacks  
✅ Extração das 10 palavras-chave mais frequentes  
✅ Visualizações com gráficos interativos  
✅ Exportação dos resultados em CSV  

---

## 📌 Resumo do Projeto

O DataTalks foi desenvolvido para ajudar empresas e analistas a entenderem melhor os feedbacks recebidos de seus clientes. Através de IA, ele automatiza a leitura e análise de grandes volumes de comentários, revelando sentimentos, resumos e padrões de palavras importantes, permitindo decisões mais rápidas e baseadas em dados.

---

## 🧠 Tecnologias utilizadas

- [Python 3.13](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- [Regex / Counter (collections)](https://docs.python.org/3/library/collections.html)

---

## ✅ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/PedroSouza73/datatalks-streamlit.git
cd datatalks-streamlit


### 1.1 Instale as dependências
pip install -r requirements.txt

### 1.2 Crie e configure o arquivo secrets.toml

Crie um diretório chamado .streamlit na raiz do projeto e, dentro dele, crie o arquivo secrets.toml com o seguinte conteúdo:
GEMINI_API_KEY = "sua-chave-aqui"
Substitua "sua-chave-aqui" pela sua chave da API Gemini.

### 1.3 Rode o projeto
streamlit run app.py
