import requests
import os
import json
from datetime import datetime, timedelta

# Parâmetros de acesso
access_key = "e0e908c7f9ecddbd8659ed42098006c4"
currencies = "USD,EUR,BRL,CLP"

# Diretório para salvar local
output_dir = "currencylayer_data"

# URL da API (endpoint modificado)
url = "https://api.currencylayer.com/timeframe"

# Data atual
current_date = datetime.now().date()

# Data de início 30 dias atrás
start_date = current_date - timedelta(days=30)

# Diretório de saída se ele não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

while start_date < current_date:
    # Data final é a data de início + 30 dias ou a data atual, o que ocorrer primeiro
    end_date = min(start_date + timedelta(days=30), current_date)

    # Formatando Data
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    # Parâmetros da solicitação
    params = {
        "access_key": access_key,
        "currencies": currencies,
        "start_date": start_date_str,
        "end_date": end_date_str
    }

    # Solicitação GET para a API
    response = requests.get(url, params=params)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        data = response.json()

        # Salve os dados em um arquivo JSON com base nas datas
        output_file = os.path.join(output_dir, f"currencylayer_data_{start_date_str}.json")
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"Dados salvos em {output_file}")

    # Atualizando a data de início para a próxima iteração
    start_date = end_date

print("Extração de dados concluída.")
