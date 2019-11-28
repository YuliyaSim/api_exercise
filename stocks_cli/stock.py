from datetime import datetime, tzinfo

import pytz
import requests


class Stock:
    def __init__(self, symbol: str,
                 name: str,
                 currency: str,
                 price: float,
                 stock_exchange_name: str,
                 last_trade_time: datetime,
                 timezone: tzinfo):
        self._symbol = symbol.upper()
        self._name = name
        self._currency = currency
        self._price = price
        self._stock_exchange_name = stock_exchange_name
        self._last_trade_name = last_trade_time
        self._timezone = timezone

    @property # so user not able to change value of symbol, name etc. / makin git imutable
    def symbol(self):
        return self._symbol

    @property
    def name(self):
        return self._name

    @property
    def currency(self):
        return self._currency

    @property
    def price(self):
        return self._price

    @property
    def stock_exchange_name(self):
        return self._stock_exchange_name

    @property
    def last_trade_time(self):
        return self._last_trade_time

    @property
    def timezone(self):
        return self._timezone

    @staticmethod
    def get(symbol: str, api_token: str):
        response = requests.get("https://api.worldtradingdata.com/api/v1/stock",
                                {
                                    'symbol': symbol,
                                    'api_token': api_token
                                })
        response.raise_for_status()
        deserialized_response = response.json()  #if we search for symbol that is not exist, it will raise an Error
        if 'Message' in deserialized_response:
            raise ValueError(deserialized_response['Message'])
        stock_data = response.json()['data'][0]
        return Stock(
            stock_data['symbol'],
            stock_data['name'],
            stock_data['currency'],
            float(stock_data['price']),
            stock_data['stock_exchange_long'],
            datetime.strptime(stock_data['last_trade_time'], '%Y-%m-%d %H:%M:%S'),
            pytz.timezone(stock_data['timezone_name'])
        )





