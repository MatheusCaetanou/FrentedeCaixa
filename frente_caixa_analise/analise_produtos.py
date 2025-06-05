import pandas as pd
import os

# Criar pasta de saída
os.makedirs("relatorios", exist_ok=True)

# Carregar CSV
df = pd.read_csv("C:/Users/Matheus/IdeaProjects/FRENTE DE CAIXA/frente_caixa_analise/Produtos.csv", sep=";", encoding="utf-8", engine="python")

# Limpeza e conversões
df.columns = df.columns.str.strip()
df["Preço de Custo"] = pd.to_numeric(df.get("Preço de Custo"), errors="coerce")
df["Preço Venda Varejo"] = pd.to_numeric(df.get("Preço Venda Varejo"), errors="coerce")
df["Quantidade Mínima Atacado"] = pd.to_numeric(df.get("Quantidade Mínima Atacado"), errors="coerce")
if "Ativo" in df.columns:
    df["Ativo"] = df["Ativo"].astype(str).str.strip().str.lower()

# Detectar coluna de estoque
estoque_col = next((col for col in df.columns if "estoque" in col.lower()), None)
if estoque_col:
    df[estoque_col] = pd.to_numeric(df[estoque_col], errors="coerce")

# Produtos inativos
if "Ativo" in df.columns:
    inativos = df[df["Ativo"] != "sim"]
    print("\n📌 PRODUTOS INATIVOS:")
    print(inativos[["Descrição", "Ativo"]])
    inativos.to_excel("relatorios/relatorio_inativos.xlsx", index=False)

# Estoque zerado e reposição
if estoque_col:
    zerado = df[df[estoque_col] <= 0]
    print("\n📌 PRODUTOS COM ESTOQUE ZERADO:")
    print(zerado[["Descrição", estoque_col]])
    zerado.to_excel("relatorios/relatorio_estoque_zerado.xlsx", index=False)

    if "Quantidade Mínima Atacado" in df.columns:
        reposicao = df[
            (df[estoque_col] < df["Quantidade Mínima Atacado"]) & 
            (df["Quantidade Mínima Atacado"] > 0)
        ]
        print("\n📌 PRODUTOS COM ESTOQUE ABAIXO DO MÍNIMO:")
        print(reposicao[["Descrição", estoque_col, "Quantidade Mínima Atacado"]])
        reposicao.to_excel("relatorios/relatorio_reposicao.xlsx", index=False)

# Margens de lucro
df = df[df["Preço de Custo"] > 0]
df["Margem Lucro (%)"] = ((df["Preço Venda Varejo"] - df["Preço de Custo"]) / df["Preço de Custo"]) * 100
df["Margem Lucro (R$)"] = df["Preço Venda Varejo"] - df["Preço de Custo"]

# Top 10 por lucro unitário
top_lucro = df.sort_values(by="Margem Lucro (R$)", ascending=False).head(10)
print("\n📌 TOP 10 PRODUTOS COM MAIOR LUCRO UNITÁRIO:")
print(top_lucro[["Descrição", "Margem Lucro (R$)", estoque_col]])
top_lucro.to_excel("relatorios/relatorio_promocoes.xlsx", index=False)
