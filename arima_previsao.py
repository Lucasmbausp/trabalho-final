# =========================================================
# Previsão de Indicadores Financeiros com ARIMA
# Indicadores: Ibovespa, CDI e IPCA
# Frequência: mensal
# Janela histórica: últimos 10 anos
# Previsão: próximos 24 meses
# =========================================================

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

# ---------------------------------------------------------
# 1. Configurações gerais
# ---------------------------------------------------------
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"
FORECAST_HORIZON = 24
TEST_SIZE = 0.2

# ---------------------------------------------------------
# 2. Função para baixar séries do Banco Central (SGS)
# ---------------------------------------------------------
def download_sgs(code):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=csv"
    df = pd.read_csv(url, sep=";")
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)
    df["valor"] = df["valor"].str.replace(",", ".").astype(float)
    return df.set_index("data")["valor"]

# ---------------------------------------------------------
# 3. Coleta dos dados
# ---------------------------------------------------------
print("Coletando dados...")

# Ibovespa
ibov = yf.download("^BVSP", start=START_DATE, end=END_DATE, progress=False)["Adj Close"]

# CDI e IPCA
cdi = download_sgs(12)     # CDI
ipca = download_sgs(433)   # IPCA

# ---------------------------------------------------------
# 4. Tratamento mensal
# ---------------------------------------------------------
ibov_m = ibov.resample("M").last()
cdi_m = (cdi.resample("M").last()) / 100
ipca_m = (ipca.resample("M").last()) / 100

df = pd.concat([ibov_m, cdi_m, ipca_m], axis=1)
df.columns = ["IBOV", "CDI", "IPCA"]
df = df.dropna()

print("Dados prontos para modelagem.\n")

# ---------------------------------------------------------
# 5. Funções auxiliares
# ---------------------------------------------------------
def split_train_test(series, test_size=0.2):
    split_point = int(len(series) * (1 - test_size))
    return series[:split_point], series[split_point:]

def calculate_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return mae, mape

# ---------------------------------------------------------
# 6. Ajuste do ARIMA e avaliação
# ---------------------------------------------------------
results = {}

for column in ["IBOV", "CDI", "IPCA"]:
    print(f"Ajustando modelo ARIMA para {column}...")

    series = df[column]
    train, test = split_train_test(series, TEST_SIZE)

    if column == "IBOV":
        model = ARIMA(np.log(train), order=(1, 1, 1))
        fitted = model.fit()
        forecast_test = np.exp(fitted.forecast(steps=len(test)))
    else:
        model = ARIMA(train, order=(1, 0, 1))
        fitted = model.fit()
        forecast_test = fitted.forecast(steps=len(test))

    mae, mape = calculate_metrics(test.values, forecast_test.values)
    results[column] = {"MAE": mae, "MAPE": mape}

    # Gráfico treino x teste x previsão
    plt.figure(figsize=(10, 5))
    plt.plot(train.index, train, label="Treino")
    plt.plot(test.index, test, label="Teste")
    plt.plot(test.index, forecast_test, "--", label="Previsão ARIMA")
    plt.title(f"{column} - Ajuste e Previsão (Teste)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ---------------------------------------------------------
# 7. Previsão final para os próximos 24 meses
# ---------------------------------------------------------
print("\nGerando previsões para os próximos 24 meses...\n")

future_forecasts = {}

for column in ["IBOV", "CDI", "IPCA"]:
    series = df[column]

    if column == "IBOV":
        model = ARIMA(np.log(series), order=(1, 1, 1))
        fitted = model.fit()
        forecast = np.exp(fitted.forecast(FORECAST_HORIZON))
    else:
        model = ARIMA(series, order=(1, 0, 1))
        fitted = model.fit()
        forecast = fitted.forecast(FORECAST_HORIZON)

    future_forecasts[column] = forecast

    plt.figure(figsize=(10, 5))
    plt.plot(series.index, series, label="Histórico")
    plt.plot(forecast.index, forecast, "--", label="Previsão ARIMA (24 meses)")
    plt.title(f"{column} - Previsão Futura")
    plt.legend()
    plt.grid(True)
    plt.show()

# ---------------------------------------------------------
# 8. Resultados finais
# ---------------------------------------------------------
print("Avaliação dos modelos (amostra de teste):\n")
for k, v in results.items():
    print(f"{k}: MAE = {v['MAE']:.6f} | MAPE = {v['MAPE']:.2f}%")

print("\nExecução finalizada com sucesso.")
