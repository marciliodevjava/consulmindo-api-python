import requests

from diretorio.url_base import URL_SITE, URL_SITES
from login.login_headers import headers
from diretorio.nomes_sites import NOMES_SITES

requisicao = None
SITE_URL = list()
SITE_ID = list()

requisicao_get_sites = requests.request('GET', URL_SITES)

if requisicao_get_sites.status_code == 200:
    print('GET SITES')
    requisicao = requisicao_get_sites.json()
    site = requisicao['Sites']
    for s in site:
        SITE_URL.append(s.get('url'))
        print(s)
    print('=======================================================================')

print('GET SITES URL')
for id in SITE_URL:
    print('Chamando site por url:{}'.format(id))
    id_site = '/' + id
    requisicao_get_id = requests.request('GET', URL_SITE+id_site, headers=headers)

    if requisicao_get_id.status_code == 200:
        print(requisicao_get_id.json())

print('=======================================================================')
print('POST SITE')
for site in NOMES_SITES:
    resposta_site_cadastrado = requests.request('POST', URL_SITE, json=site, headers=headers)
    if resposta_site_cadastrado.status_code == 201:
        print('Site cadastrado com sucesso!')
        site_cadastrado = resposta_site_cadastrado.json()
        print(site_cadastrado)
        id = site_cadastrado.get('Site').get('site_id')
        SITE_ID.append(id)
    else:
        url_site = site.get('url')
        print('Site {} já está cadastrato, tente outro site.'.format(url_site))
print('=======================================================================')

