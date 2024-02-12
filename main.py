import requests

from diretorio import nomes_hoteis
from diretorio.url_base import URL_GET_LOGIN, URL_GET_HOTEIS, URL_SITES

LIST_ID_SITES = nomes_hoteis.NOMES_ID_HOTEIS

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
    print('Imprimendo Hoteis Cadastrados')
    for h in hotel:
        print(dict(h))

print('=======================================================================')

resposta_sites = requests.request('GET', URL_SITES)

if resposta_sites.status_code == 200:
    sites = resposta_sites.json()
    site = sites['Sites']
    print('Imprimento Sites Cadastrados')
    for s in site:
        print(dict(s))
