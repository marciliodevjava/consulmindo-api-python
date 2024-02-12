import requests

from diretorio.url_base import URL_LOGIN

BEARER = 'Bearer '
TOKEN = None

login = {
    "login": "marcilio",
    "senha": "123"
}

print('Efetuando login na aplicação')
resposta_login = requests.request('POST', URL_LOGIN, json=login)

if resposta_login.status_code == 200:
    print('Login efetuado com sucesso"')
    print("=======================================================================")
    resposta = resposta_login.json()
    access_token = resposta.get('acces-token')
    TOKEN = BEARER + access_token
else:
    print('Login Falhou.')
    print("=======================================================================")

headers = {
    'Authorization': TOKEN
}