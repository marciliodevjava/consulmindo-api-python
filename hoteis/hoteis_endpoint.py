import requests

from diretorio.url_base import URL_HOTEIS
from login.login_headers import headers

LIST_ID_HOTEL = list()

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