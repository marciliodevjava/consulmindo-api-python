import requests

from diretorio.url_base import URL_SITE, URL_SITES
from login.login_headers import headers

requisicao = None
SITE_URL = list()

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
