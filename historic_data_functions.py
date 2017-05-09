# =============================================================================
#          File: historic_data_functions.py
#        Author: Andre Brener
#       Created: 08 May 2017
# Last Modified: 08 May 2017
#   Description: description
# =============================================================================
import json
import time

import requests
import pandas as pd
import matplotlib.dates as mdates

from matplotlib import pyplot as plt


def get_price_history(coin_list, end_date, days_past, price_type):
    ts = time.mktime(end_date.timetuple())
    df_list = []
    for l in coin_list:
        url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym=USD&toTs={}&limit={}'.format(
            l, ts, days_past)
        response_text = requests.get(url).text
        d = json.loads(response_text)

        df = pd.DataFrame(d['Data'])[['time', price_type]]
        df['coin'] = l
        df_list.append(df)
    total_df = pd.concat(df_list)
    total_df = total_df.pivot(
        index='time', columns='coin', values=price_type).reset_index()
    total_df['day'] = pd.to_datetime(total_df['time'], unit='s')
    return total_df


def get_graph(df, coin_name, day_interval, dates=True):
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
