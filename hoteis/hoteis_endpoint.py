import requests

from diretorio.dados_hoteis import DADOS_HOTEIS
from diretorio.nomes_hoteis import NOMES_ID_HOTEIS
from diretorio.url_base import URL_HOTEIS
from login.login_headers import headers

LIST_ID_HOTEL = list()
LIST_HOTEL_DELETE = list()

requisao_get_hoteis = requests.request('GET', URL_HOTEIS, headers=headers)

if requisao_get_hoteis.status_code == 200:
    print('GET TODOS HOTEIS')
    hoteis = requisao_get_hoteis.json()
    for h in hoteis['Hoteis']:
        print(h)
        LIST_ID_HOTEL.append(h.get('hotel_id'))

print('=======================================================================')
print('GET HOTEL ID')
for hotel in LIST_ID_HOTEL:
    URL_GET = f'{URL_HOTEIS}/{hotel}'
    requesicao_id = requests.request('GET', URL_GET)
    if requesicao_id.status_code == 200:
        hotel_json = requesicao_id.json()
        print(hotel_json['hotel'])

if len(NOMES_ID_HOTEIS) == len(DADOS_HOTEIS):
    for posicao in range(len(NOMES_ID_HOTEIS)):
        hotel_id = NOMES_ID_HOTEIS[posicao].get('site_id')
        URL_GET = f'{URL_HOTEIS}/{hotel_id}'
        requsicao_post = requests.request('POST', URL_GET, json=DADOS_HOTEIS[posicao], headers=headers)
        if requsicao_post.status_code == 201:
            dados_cadastro_hotel = requsicao_post.json()
            id = dados_cadastro_hotel['hotel']['hotel_id']
            LIST_HOTEL_DELETE.append(id)

for id in LIST_HOTEL_DELETE:
    URL_GET = f'{URL_HOTEIS}/{id}'
    requisicao_delete = requests.request('DELETE', URL_GET, headers=headers)
