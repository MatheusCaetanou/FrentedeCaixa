# Sistema de Frente de Caixa (PDV) - Ponto de Venda

Este projeto tem como objetivo desenvolver um sistema de *Frente de Caixa (PDV)* para o registro de vendas em uma loja de roupas, com foco em modularidade, escalabilidade e análise de dados.

## Objetivo do Sistema

O sistema tem como objetivo:

- *Registrar as vendas* de uma loja de roupas, incluindo produtos como camisas, calças, tênis, e outros.
- *Armazenar os dados* das transações de vendas em formatos eficientes para análise posterior.
- *Transformar os dados em insights, utilizando tecnologias como **Big Data, para armazenar os dados em formatos como **Parquet* e integrá-los com *dashboards* e outras ferramentas de visualização.
- *Ser modular e escalável, permitindo a integração futura com ferramentas como **Kafka, **MongoDB, **AWS*, entre outras, para garantir que o sistema possa crescer conforme necessário.

## Funcionalidades

- *Registro de Vendas:*
  - O sistema permite registrar a venda de itens da loja (camisas, calças, tênis, etc.).
  - O cliente realiza a compra e o sistema registra a transação, incluindo detalhes como itens comprados, quantidade, preço, e forma de pagamento.

- *Armazenamento de Dados:*
  - Os dados das transações são armazenados de forma otimizada para análise posterior.
  - O sistema salva os dados em formatos como *CSV, **JSON* ou *Parquet*, de acordo com a necessidade de processamento e análise de dados.

- *Análise de Dados:*
  - O sistema possui a capacidade de gerar insights utilizando ferramentas de análise de dados, como *Dashboards* para visualização de vendas, estoque e outras métricas importantes.
  - Suporte para integração com ferramentas de Big Data, permitindo análises mais complexas em grandes volumes de dados.

- *Escalabilidade e Modularidade:*
  - O sistema foi projetado de forma modular, permitindo a adição de novas funcionalidades e integrações conforme necessário.
  - Preparado para integrar com *Apache Kafka* para fluxo de dados em tempo real, *MongoDB* para armazenamento de dados não relacionais e *AWS* para soluções em nuvem, entre outras tecnologias.

## Tecnologias Utilizadas

- *Backend:* (Exemplo: Python, Node.js, etc.)
- *Banco de Dados:* (Exemplo: PostgreSQL, MongoDB)
- *Big Data e Armazenamento:* Parquet, Kafka, AWS S3
- *Ferramentas de Análise:* Dashboards (Exemplo: Grafana, Power BI, Tableau)
- *Integrações Futuros:* Kafka, MongoDB, AWS

## Estrutura do Projeto

- */src:* Código-fonte do sistema.
  - */models:* Modelos de dados.
  - */controllers:* Controladores de interação com o banco de dados.
  - */services:* Lógica de negócios e serviços (ex: cálculo de vendas, agregação de dados).
  - */utils:* Funções utilitárias e helpers.
  
- */data:* Armazenamento de dados de vendas (pode incluir arquivos CSV, JSON ou Parquet).
  
- */dashboard:* Arquivos de integração com ferramentas de análise e visualização.

## Como Rodar o Sistema

1. *Instale as dependências*:
    bash
    npm install  # Para projetos em Node.js
    pip install -r requirements.txt  # Para projetos em Python
    

2. *Configure o banco de dados* (caso seja necessário):
    - Configuração de banco de dados relacional (PostgreSQL, MySQL) ou não-relacional (MongoDB).
    - Para a integração com *AWS S3* ou outro serviço, adicione suas credenciais na configuração.

3. *Execute o servidor*:
    bash
    npm start  # Para Node.js
    python app.py  # Para Python
    

4. *Acesse o sistema*:
    - Acesse o painel do PDV via navegador ou aplicativo, conforme implementado.

## Estrutura de Dados

### Transação de Venda

Exemplo de estrutura de dados para uma transação de venda:

```json
{
  "id_venda": "12345",
  "data_hora": "2025-06-08T14:30:00",
  "itens": [
    {
      "produto": "Camisa Polo",
      "quantidade": 2,
      "preco_unitario": 49.90,
      "total": 99.80
    },
    {
      "produto": "Tênis Esportivo",
      "quantidade": 1,
      "preco_unitario": 179.90,
      "total": 179.90
    }
  ],
  "total": 279.70,
  "forma_pagamento": "Cartão de Crédito"
}
