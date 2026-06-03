# cryptocurrency_data

Fetch and chart historical & current cryptocurrency prices from the
[CryptoCompare](https://www.cryptocompare.com/) API in a Jupyter notebook,
with an optional (legacy) Google Sheets export.

The core price-fetching helpers live in `api_functions.py` and are driven
interactively from `historic_data.ipynb`.

## What it does

- Pulls historical daily prices for a list of coins (`get_price_history`).
- Pulls current prices for a list of coins (`get_current_prices`).
- Looks up the list of supported coins (`get_coin_list`, see `coin_list.ipynb`).
- Plots price history with matplotlib (`get_graph` / `plot_graphs`).
- Optionally pushes current prices to a Google Sheet (`gsheets.py`, see the
  caveat below).

## Requirements

- Python 3.6+ (this project was originally built and last updated in 2018).
- The packages in `requirements.txt` (`numpy`, `pandas`, `matplotlib`,
  `ipython`, `jupyter`, `requests`, `pyyaml`, and `google-api-python-client`).
- No CryptoCompare API key is strictly required for the endpoints used here,
  but CryptoCompare now encourages an `api_key` and applies tighter rate
  limits, so heavy or bulk unauthenticated use may be throttled.

## Getting Started

### 1. Clone Repo

`git clone https://github.com/andrebrener/cryptocurrency_data.git`

### 2. Install Packages Required

Go in the directory of the repo and run:
```pip install -r requirements.txt```

### 3. Open Jupyter Notebook

To open the notebook run:

```jupyter notebook```

This should open a tab in your browser displaying information like a finder.

#### Brief tutorial to Jupyter Notebook

The notebook is divided into blocks. The different blocks with code can be identified in the following screenshot.

![img](http://i.imgur.com/JrRyW5j.png)

Each block is run separately by pressing the Play button (screenshot below) or with shortcut `Shift+Enter`.

![img](http://i.imgur.com/0EWhMFo.png)

To delete all content and start from scratch press `Kernel` and then `Restart & Clear Output`

![img](http://i.imgur.com/MmWNLh8.png)

### 4. Get historic Data

##### Data

- Open the file [historic_data.ipynb](https://github.com/andrebrener/cryptocurrency_data/blob/master/historic_data.ipynb).
- Run the first block of code to import dependencies.
- In the second block of code insert:
  - The Coins you like by adding them to the list. Make sure that the Coin is included in the [supported coins list](https://github.com/andrebrener/cryptocurrency_data/blob/master/coin_list.ipynb).
  - The last day of your report.
  - How many days before the end date you want the data from.
  - The type of price from `close`, `high`, `low`, `open`.
  - The currency for the prices.
- Run the 2nd & 3rd blocks of code.

##### Graph
- In the 4th block of code:
  - Choose the time interval for the dates in the x-axis to be shown.
- Run the block.

##### Export CSV
- In the 5th block of code:
  - Select File Name. Run the block.
- Run the 6th block. The file should now be saved in the directory printed below. Note that the directory is relative to the repo path.

## Google Sheets export (legacy / unsupported)

`gsheets.py` can push the current prices into a Google Sheet. **This path is
legacy and is not expected to run as-is today.** It relies on the deprecated
`oauth2client` / `apiclient` authentication libraries (end-of-life, no longer
bundled with the current `google-api-python-client`) and on a local
`google_credentials.py` module that is intentionally **not** committed to this
repo.

If you want to use it, you would need to:

1. Create a Google Cloud project, enable the Google Sheets API, and download
   the OAuth client secrets as `client_secret.json`.
2. Create a `google_credentials.py` file (kept out of version control by
   `.gitignore`) that defines at least:
   ```python
   PRICES_SHEET_LINK = "<your spreadsheet id>"
   RANGE_NAME = "<sheet!A1:B100>"
   ```
3. Modernise the auth stack (e.g. migrate to `google-auth` /
   `google-auth-oauthlib`), since `oauth2client`/`apiclient` are no longer
   installable in a modern environment.

These credential files (`google_credentials.py`, `client_secret.json`) and any
generated `*.log` / `data/*.csv` files are ignored via `.gitignore` and should
never be committed.

## License

[MIT](./LICENSE)
