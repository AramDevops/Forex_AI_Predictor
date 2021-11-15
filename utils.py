from pandas import DataFrame
import pandas as pd
import copy
import json

SIGNS = sorted(['USD', 'EUR', 'BRL', 'CHF', 'GBP', 'ARS', 'CAD', 'CNY', 'JPY'])
SIGNS_DESCRIPTIONS = {'USD': "United States Dollar", 'EUR': "Euro", 'BRL': "Brazilian Real", 'CHF': "Swiss Franc",
                      'GBP': "British Pound Sterling", 'ARS': "Argentine Peso", 'CAD': "Canadian Dollar",
                      'CNY': "Chinese Yuan", 'JPY': "Japanese Yen"}
DAYS_OF_PREDICTION = 7

def api_formatter(json_data: json, returned_keys_list: list) -> dict:
    test = {key: value for key, value in dict(json_data).items()
            if key in returned_keys_list}
    return test


def SIGNS_verification_str(base: str) -> str:
    symbols = copy.copy(SIGNS)
    symbols.remove(base)

    return ','.join(symbols)


def SIGNS_verification_lst(base: str) -> list:
    symbols = copy.copy(SIGNS)
    symbols.remove(base)
    return symbols


def divide_currencies(df: DataFrame, base: str) -> dict:
    SIGNS = SIGNS_verification_lst(base)
    df.reset_index(level=0, inplace=True)
    dataframes_dict = dict()
    for currency in SIGNS:
        df_aux = pd.DataFrame()
        df_aux['ds'] = df['index']
        df_aux['y'] = df[currency]
        dataframes_dict[currency] = df_aux
    return dataframes_dict
