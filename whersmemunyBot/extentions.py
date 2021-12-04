import requests
import json
from config import currencies_list


class APIException(Exception):
    pass


class CurrencyConverter():
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Вы ввели одинаковые валюты для конвертации ({base})!')

        try:
            base_tikr = currencies_list[base]
        except KeyError:
            raise APIException(f'Неверно введена исходная валюта ({base})!')

        try:
            quote_tikr = currencies_list[quote]
        except KeyError:
            raise APIException(f'Неверно введена валюта конвертации ({quote})!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неверно введенщ количество ({amount})!')

        r = requests.get(f'https://free.currconv.com/api/v7/convert'
                         f'?q={base_tikr}_{quote_tikr}'
                         f'&compact=ultra'
                         f'&apiKey=78d0998cb15931668107')
        conv_key = f'{currencies_list[base]}_{currencies_list[quote]}'
        result = json.loads(r.content)[conv_key] * amount

        return result

