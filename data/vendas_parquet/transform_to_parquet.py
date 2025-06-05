import pandas as pd
import os


entrada_json = os.path.join("data", "vendas_raw", "vendas_raw.json")
saida_parquet = os.path.join("data", "vendas_parquet", "vendas.parquet")


print("Lendo arquivo JSON...")
df = pd.read_json(entrada_json, lines=True)

print("Primeiras linhas do DataFrame:")
print(df.head())


print("Salvando como Parquet...")
df.to_parquet(saida_parquet, index=False)

print(f"Arquivo salvo em: {saida_parquet}")
