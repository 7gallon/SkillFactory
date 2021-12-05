import requests
import json

currencies_list = {'Рубль':'RUB',
                    'Евро':'EUR',
                    'Доллар':'USD',}

curl = requests.get('https://free.currconv.com/api/v7/currencies?apiKey=78d0998cb15931668107')
c_list = json.loads(curl.content)['results']
for key in c_list.keys():
    # print(key)\
    currencies_list[c_list[key]['currencyName']] = key
