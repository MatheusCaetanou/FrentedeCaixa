import pandas as pd
import streamlit as st
import os

os.chdir("C:/Users/Matheus/IdeaProjects/FRENTE DE CAIXA/frente_caixa_analise")  # Define o diretório correto
print("Diretório ajustado para:", os.getcwd())  # Verifica se foi alterado com sucess

print("Diretório atual:", os.getcwd())  # Mostra o diretório de execução
print("Arquivos na pasta:", os.listdir())  # Lista todos os arquivos na pasta
print("Arquivo existe?", os.path.exists("Produtos.csv"))  # Confirma se o CSV está acessível

df = pd.read_csv("C:/Users/Matheus/IdeaProjects/FRENTE DE CAIXA/frente_caixa_analise/Produtos.csv", sep=";", encoding="utf-8", engine="python")

# Carregar CSV
df = pd.read_csv("Produtos.csv", sep=";", encoding="utf-8", engine="python")

# Limpeza
df.columns = df.columns.str.strip()
df["Preço de Custo"] = pd.to_numeric(df.get("Preço de Custo"), errors="coerce")
df["Preço Venda Varejo"] = pd.to_numeric(df.get("Preço Venda Varejo"), errors="coerce")
df["Quantidade Mínima Atacado"] = pd.to_numeric(df.get("Quantidade Mínima Atacado"), errors="coerce")
if "Ativo" in df.columns:
    df["Ativo"] = df["Ativo"].astype(str).str.strip().str.lower()

# Detectar a coluna de estoque
estoque_col = next((col for col in df.columns if "estoque" in col.lower()), None)
if estoque_col:
    df[estoque_col] = pd.to_numeric(df[estoque_col], errors="coerce")

# Layout
st.set_page_config(page_title="Análise de Produtos", layout="wide")
st.title("📊 Análise de Produtos da Loja")

# Produtos inativos
if "Ativo" in df.columns:
    inativos = df[df["Ativo"] != "sim"]
    st.subheader("Produtos Inativos")
    st.dataframe(inativos[["Descrição", "Ativo"]])

# Estoque zerado e abaixo do mínimo
if estoque_col:
    zerado = df[df[estoque_col] <= 0]
    st.subheader("Produtos com Estoque Zerado")
    st.dataframe(zerado[["Descrição", estoque_col]])

    if "Quantidade Mínima Atacado" in df.columns:
        reposicao = df[
            (df[estoque_col] < df["Quantidade Mínima Atacado"]) &
            (df["Quantidade Mínima Atacado"] > 0)
        ]
        st.subheader("Produtos com Estoque Abaixo do Mínimo")
        st.dataframe(reposicao[["Descrição", estoque_col, "Quantidade Mínima Atacado"]])

# Calcular margens
df = df[df["Preço de Custo"] > 0]
df["Margem Lucro (%)"] = ((df["Preço Venda Varejo"] - df["Preço de Custo"]) / df["Preço de Custo"]) * 100
df["Margem Lucro (R$)"] = df["Preço Venda Varejo"] - df["Preço de Custo"]

# Top lucro absoluto
top_lucro = df.sort_values(by="Margem Lucro (R$)", ascending=False).head(10)
st.subheader("Top 10 Produtos com Maior Lucro Unitário")
st.dataframe(top_lucro[["Descrição", "Preço de Custo", "Preço Venda Varejo", "Margem Lucro (R$)"]])

st.subheader("Gráfico de Lucro Unitário")
st.bar_chart(top_lucro.set_index("Descrição")["Margem Lucro (R$)"])

# Sugestão de promoção
st.subheader("Sugestões de Promoções (Maior Lucro)")
if estoque_col:
    st.dataframe(top_lucro[["Descrição", "Margem Lucro (R$)", estoque_col]])
else:
    st.dataframe(top_lucro[["Descrição", "Margem Lucro (R$)"]])
