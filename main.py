import requests

from diretorio import nomes_hoteis

URL_BASE = 'http://127.0.0.1:5000'
HOTEIS = '/hoteis'
LOGIN = '/login'

URL_GET_HOTEIS = URL_BASE + HOTEIS
URL_GET_LOGIN = URL_BASE + LOGIN
LIST_ID_SITES = nomes_sites.NOMES_ID_sites

resposta = None
BEARER = 'Bearer '
TOKEN = None

login = {
    "login": "marcilio",
    "senha": "123"
}

resposta_login = requests.request('POST', URL_GET_LOGIN, json=login)

if resposta_login.status_code == 200:
    resposta = resposta_login.json()
    access_token = resposta.get('acces-token')
    TOKEN = BEARER + access_token

headers = {
    'Authorization': TOKEN
}

resposta_hoteis = requests.request('GET', URL_GET_HOTEIS, headers=headers)

if resposta_hoteis.status_code == 200:
    hoteis = resposta_hoteis.json()
    hotel = hoteis['Hoteis']
    for h in hotel:
        print(dict(h))
