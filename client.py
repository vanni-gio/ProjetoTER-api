# client.py
import requests

def get_secret_message():
    #response = requests.get("https://localhost:5683/", verify="ca-public-key.pem")
    response = requests.post("https://localhost:5683/token", json={"nome": "Teste", "senha": "1234"}, verify="ca-public-key.pem")
    token = response.json()['token']
    response = requests.get("https://localhost:5683/certificado",
        headers={'x-access-token': token}, 
        verify="ca-public-key.pem"
        )
    print(response.json())
    # recebeu o certificado

if __name__ == "__main__":
    get_secret_message()
# pass phrase for ca.key = APSODLSDKASKJ
# challenge password = abacaxi123