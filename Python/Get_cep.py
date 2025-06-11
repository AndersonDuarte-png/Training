import requests
base_url =  "https://viacep.com.br/ws/"

def obter_cep(cep: str)-> dict:
    response = requests.get(f"{base_url}{cep}/json", timeout=30)
    if response.status_code == 200:
        return response.json()
    return {}

cep = (input("CEP: "))

dados_cep = obter_cep(cep)
print(dados_cep)