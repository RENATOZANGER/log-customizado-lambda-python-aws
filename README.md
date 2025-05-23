# log-customizado-lambda-python-aws

Este projeto é um exemplo de como criar logs customizados em Python em uma função AWS Lambda.

## 📌 Objetivo

Permitir que os logs gerados pela função Lambda tenham:
- Correlation ID para rastreamento entre serviços
- Informações detalhadas do local do código (arquivo, linha, classe, função)
- Timestamps no fuso horário de Brasília
- Payloads adicionais no log
- Formatação estruturada em JSON para facilitar a análise via CloudWatch Logs Insights

---

## ⚙️ Requisitos

- Python 3.11 ou superior
- AWS Lambda configurado para usar o **Runtime Python**
- Log content em Logging Configuration do Lambda com:
  - **Log format:** `Text`

> ⚠️ Importante: O AWS Lambda sobrescreve campos como `timestamp`, `message`, `level` e `requestId` no log padrão. Por isso, incluí esses dados como campos internos dentro do JSON do log.

---

## 🚀 Como usar

1. Clone o projeto:

```bash
git clone https://github.com/seu-usuario/log-customizado-lambda-python-aws.git
