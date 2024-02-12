import requests

from diretorio import nomes_hoteis
from diretorio.url_base import URL_HOTEIS, URL_SITES
from login.login_headers import headers

LIST_ID_SITES = nomes_hoteis.NOMES_ID_HOTEIS

resposta = None

resposta_hoteis = requests.request('GET', URL_HOTEIS, headers=headers)

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
