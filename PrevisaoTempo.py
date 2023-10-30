import requests

def consultar_previsao_tempo(cidade, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": cidade,
        "appid": api_key,
        "units": "metric"  # Use "imperial" para Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperatura = data["main"]["temp"]
            descricao = data["weather"][0]["description"]
            print(f"Previsão do tempo para {cidade}:")
            print(f"Temperatura: {temperatura}°C")
            print(f"Descrição: {descricao}")
        else:
            print("Cidade não encontrada.")
    except Exception as e:
        print(f"Erro ao consultar a previsão do tempo: {e}")

def main():
    api_key = "SUA_CHAVE_DE_API_AQUI"
    cidade = input("Digite o nome da cidade: ")
    consultar_previsao_tempo(cidade, api_key)

if __name__ == "__main__":
    main()
