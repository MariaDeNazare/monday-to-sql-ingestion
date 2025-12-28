# Monday.com → SQL Server | Data Ingestion

Projeto didático de ingestão de dados a partir da API GraphQL do Monday.com,
com persistência em banco de dados relacional (SQL Server).

A solução foi pensada para demonstrar conceitos de engenharia de dados,
priorizando clareza, organização e boas práticas para pipelines de ingestão.

---

## Visão Geral

O script realiza a extração de dados hierárquicos (items e subitems) de um board
do Monday.com e persiste as informações em tabelas relacionais no SQL Server.

O foco deste projeto é demonstrar:
- Consumo de API GraphQL
- Tratamento de dados dinâmicos
- Persistência em banco relacional
- Estruturação de código para pipelines de dados

---

## Arquitetura Simplificada

Monday.com (GraphQL API)  
→ Script Python  
→ SQL Server  

---

## Tecnologias Utilizadas

- Python
- API GraphQL (Monday.com)
- SQL Server
- pyodbc
- Variáveis de ambiente para credenciais

---

## Observações

Este repositório apresenta uma versão simplificada e didática da solução.
Em cenários reais, a ingestão pode ser expandida com:
- Paginação por cursor
- Retentativas automáticas (retry / backoff)
- Controle de duplicidade
- Orquestração via pipelines (ex: Azure DevOps)

---

## Objetivo

Demonstrar capacidade técnica em engenharia de dados,
com foco em integração de sistemas, automação e persistência de dados.

