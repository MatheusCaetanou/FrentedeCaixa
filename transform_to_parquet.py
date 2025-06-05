import pandas as pd
import os

# Caminhos de entrada e saída
entrada_json = os.path.join("data", "vendas_raw", "vendas_raw.json")
saida_parquet = os.path.join("data", "vendas_parquet", "vendas.parquet")

# Lê o JSON
print("Lendo arquivo JSON...")
df = pd.read_json(entrada_json, lines=True)

# Mostra dados lidos
print("Primeiras linhas do DataFrame:")
print(df.head())

# Salva como Parquet
print("Salvando como Parquet...")
df.to_parquet(saida_parquet, index=False)

print(f"Arquivo salvo em: {saida_parquet}")