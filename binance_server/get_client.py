import logging
import _creds

from binance.spot import Spot

import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

from binance.lib.utils import config_logging
config_logging(logging, logging.CRITICAL)

def get_spot_client(api_key, secret_key):
    """
    Функция для инициализации спотового клиента
    для Тестнета binance
    :return:
    """
    return Spot(
        base_url='https://testnet.binance.vision',
        key=api_key,
        secret=secret_key,
    )
