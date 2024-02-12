import requests

from diretorio.url_base import URL_LOGIN

BEARER = 'Bearer '
TOKEN = None

login = {
    "login": "marcilio",
    "senha": "123"
}

resposta_login = requests.request('POST', URL_LOGIN, json=login)

if resposta_login.status_code == 200:
    resposta = resposta_login.json()
    access_token = resposta.get('acces-token')
    TOKEN = BEARER + access_token

headers = {
    'Authorization': TOKEN
}