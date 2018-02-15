# =============================================================================
#          File: api_functions.py
#        Author: Andre Brener
#       Created: 08 May 2017
# Last Modified: 06 Jan 2018
#   Description: description
# =============================================================================
import json
import time

import requests
import pandas as pd


def get_coin_list():

    coin_list_url = 'https://www.cryptocompare.com/api/data/coinlist/'

    response_text = requests.get(coin_list_url).text

    d = json.loads(response_text)
    data = d['Data']

    coin_list = set(
        [
            val['Name'] for val in data.values()
            if all(kw not in val['Name'] for kw in ['*', ' '])
        ]
    )

    coin_list = sorted(list(coin_list), reverse=False)

    return coin_list


def get_current_prices(coin_list):

    coin_list_string = ','.join(coin_list)
    price_now_url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=USD'.format(
        coin_list_string
    )

    response_text = requests.get(price_now_url).text
    d = json.loads(response_text)

    coin_prices = [[coin, val['USD']] for coin, val in d.items()]

    return coin_prices


def get_price_history(coin_list, end_date, days_past, price_type, currency):
    ts = time.mktime(end_date.timetuple())
    df_list = []
    for l in coin_list:
        url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&toTs={}&limit={}'.format(
            l, currency, ts, days_past
        )
        response_text = requests.get(url).text
        d = json.loads(response_text)

        if not len(d['Data']):
            continue

        df = pd.DataFrame(d['Data'])[['time', price_type]]

        df['token'] = l

        df_list.append(df)
    total_df = pd.concat(df_list)
    total_df = total_df.pivot(
        index='time', columns='token', values=price_type
    ).reset_index()
    total_df['day'] = pd.to_datetime(total_df['time'], unit='s')
    cols = [col for col in total_df.columns if col not in ['time']]
    total_df = total_df[cols]
    return total_df


def get_graph(df, coin_name, day_interval, dates=True):
    import matplotlib.dates as mdates

    from matplotlib import pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a'))
    if dates:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=day_interval))
    plt.gcf().autofmt_xdate()
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    plt.title('{} Price History'.format(coin_name))
    y = df[coin_name]
    plt.plot(df['day'], y)


def plot_graphs(df, day_interval, dates=True):
    cols = [col for col in df.columns if col not in ['time', 'day']]
    for coin_name in cols:
        get_graph(df, coin_name, day_interval)


if __name__ == '__main__':
    from datetime import date

    coin_list = ['ETH']
    end_date = date(2017, 5, 30)
    days_past = 2

    df = get_price_history(coin_list, end_date, days_past, 'close')

    print(df)
