# =============================================================================
#          File: gsheets.py
#        Author: Andre Brener
#       Created: 19 May 2017
# Last Modified: 20 May 2017
#   Description: description
# =============================================================================
from __future__ import print_function

import os

import httplib2

from apiclient import discovery
from api_functions import get_current_prices
from oauth2client import client, tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(
        credential_dir, 'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def read_data(service, spreadsheet_id, range_name):

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()

    values = result.get('values', [])

    if not values:
        return None

    return values


def update_data(service,
                spreadsheet_id,
                range_name,
                new_values,
                value_input_option='USER_ENTERED',
                major_dimension='ROWS'):
    body = {}
    body['range'] = range_name
    body['majorDimension'] = major_dimension
    body['values'] = new_values
    value_input_option = value_input_option
    return service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption=value_input_option,
        body=body).execute()


def get_id_from_link(link):
    spreadsheet_id = link.split('/')[5]
    return spreadsheet_id


def main(spreadsheet_id, range_name):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build(
        'sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

    values = read_data(service, spreadsheet_id, range_name)

    if not values:
        return None

    coin_list = [coin for coin, val in values]

    new_prices = get_current_prices(coin_list)

    update_data(service, spreadsheet_id, range_name, new_prices)


if __name__ == '__main__':

    spreadsheet_link = 'https://docs.google.com/spreadsheets/d/1K_pKyMs9QN8HixETIYT2caL-BQF5qBOLC3pN9Hyjbvk/edit#gid=0'
    spreadsheet_id = get_id_from_link(spreadsheet_link)
    range_name = 'crypto_prices!A1:B'

    main(spreadsheet_id, range_name)
