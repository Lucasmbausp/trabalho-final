Previsão de Indicadores Financeiros com ARIMA

Este repositório contém o código-fonte desenvolvido para o Trabalho de Conclusão de Curso que avalia a aplicação do modelo ARIMA na previsão de séries temporais financeiras.

Objetivo

Avaliar a capacidade preditiva do modelo ARIMA para os seguintes indicadores brasileiros:

Ibovespa

CDI

IPCA

A análise utiliza dados mensais dos últimos 10 anos e realiza previsões para os 24 meses subsequentes.

Metodologia

Frequência dos dados: mensal

Janela histórica: 10 anos

Divisão dos dados:

80% para treino

20% para teste

Modelo: ARIMA (p, d, q)

Métricas de avaliação:

MAE (Erro Absoluto Médio)

MAPE (Erro Percentual Absoluto Médio)

O Ibovespa é modelado em logaritmo dos níveis, enquanto CDI e IPCA são tratados como séries em nível.

Estrutura do Repositório
trabalho-final/
├── arima_previsao.py
├── README.md
├── requirements.txt

Como executar o projeto

Clone o repositório:

git clone https://github.com/Lucasmbausp/trabalho-final.git


Acesse a pasta:

cd trabalho-final


Instale as dependências:

pip install -r requirements.txt


Execute o script:

python arima_previsao.py

🎯 Conclusão

Este repositório disponibiliza de forma transparente o código utilizado no Trabalho de Conclusão de Curso, permitindo a reprodução integral dos resultados e assegurando boas práticas de pesquisa científica.
