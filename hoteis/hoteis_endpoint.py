import requests

from diretorio.url_base import URL_HOTEIS
from login.login_headers import headers

requisao_get_hoteis = requests.request('GET', URL_HOTEIS, headers=headers)

if requisao_get_hoteis.status_code == 200:
    hoteis = requisao_get_hoteis.json()
    for h in hoteis['Hoteis']:
        print(h)
