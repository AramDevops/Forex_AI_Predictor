from functools import lru_cache
from pandas import DataFrame
import pandas as pd
import requests

from utils import api_formatter, SIGNS_verification_str

# Definitions of requests
DECIMALS = str(6)
@lru_cache(1000)
def request_time_series_conversion(base: str, amount: float, start_date: str, end_date: str) -> DataFrame:
    symbols = SIGNS_verification_str(base)
    """url = f'https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}' \
          f'&base='+base+'&amount='+str(amount) +'&places='+DECIMALS+'&symbols='+ symbols"""
    url = f'https://freecurrencyapi.net/api/v2/historical?apikey=2f059550-4442-11ec-9edd-a55e2712eb4c&base_currency={base}&date_from={start_date}&date_to={end_date}'
    response = requests.get(url)
    time_series_conversion_dict = api_formatter(response.json(), ['base_currency', 'data'])
    df = pd.DataFrame(time_series_conversion_dict['data']).T
    df = df.round(5)
    return df



