# Previsão de Indicadores Financeiros com ARIMA

Este repositório contém o código-fonte desenvolvido para o Trabalho de Conclusão de Curso
que avalia a aplicação do modelo ARIMA na previsão de séries temporais financeiras.

## Objetivo

Avaliar a capacidade preditiva do modelo ARIMA para os seguintes indicadores brasileiros:
- Ibovespa
- CDI
- IPCA

A análise utiliza dados mensais dos últimos 10 anos e realiza previsões para os 24 meses subsequentes.

## Metodologia

- Frequência: mensal  
- Janela histórica: 10 anos  
- Divisão dos dados:
  - 80% para treino
  - 20% para teste  
- Modelo: ARIMA (p, d, q)  
- Métricas de avaliação:
  - MAE (Erro Absoluto Médio)
  - MAPE (Erro Percentual Absoluto Médio)

O Ibovespa é modelado em logaritmo dos níveis, enquanto CDI e IPCA são tratados como séries de taxa.

## Estrutura do Repositório

trabalho-final/
├── arima_previsao.py
├── README.md
├── requirements.txt


## Como executar o código

1. Clone o repositório:
```bash
git clone https://github.com/Lucasmbausp/trabalho-final.git

cd trabalho-final


pip install -r requirements.txt

python arima_previsao.py


3. Desça a página
4. Em **Commit changes**:
   - Mensagem: `Atualização do README`
5. Clique em **Commit changes**

✅ Pronto. Seu README agora está **100% padrão acadêmico**.

---

# 🪜 PASSO 2 — Criar o arquivo `requirements.txt`

1. Volte para a página principal do repositório
2. Clique em **Add file → Create new file**

No campo **File name**, escreva exatamente:

requirements.txt

No campo de texto, cole:

```txt
pandas
numpy
matplotlib
yfinance
statsmodels
scikit-learn

Adiciona requirements
