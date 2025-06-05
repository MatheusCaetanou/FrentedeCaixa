# Sistema de Análise de Produtos – Frente de Caixa

Este sistema realiza análises automáticas com base nos dados do arquivo `Produtos.csv`, identificando:

- Produtos inativos
- Produtos com estoque zerado
- Produtos com estoque abaixo do mínimo
- Margem de lucro por produto
- Sugestões de promoções (alta margem + bom estoque)

Também gera **relatórios Excel prontos** com um clique para uso em decisões gerenciais.

---


---



- Python 3.10 ou superior
- Bibliotecas:
  - `pandas`

### Para instalar as dependências:
```bash
pip install pandas
