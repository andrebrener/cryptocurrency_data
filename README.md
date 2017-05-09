# Cryptocurrency Prices

The application uses the CryptoCompare API to get the prices.

## Getting Started

### Clone Repo

`git clone https://github.com/andrebrener/cryptocurrency_data.git`

### Install Packages Required

Go in the directory of the repo and run:
```pip install -r requirements.txt```

### Open Jupyter Notebook

To open the notebook run:

```jupyter notebook```

This should open a tab in your browser displaying information like a finder.

#### Brief tutorial to Jupyter Notebook

The notebook is divided into blocks. Each block is run separately by pressing the Play button or with shortcut of Shift+Enter.

The blocks must be run in order as the order of the code must be respected.

To delete all content and start from scratch press `Kernel` and then `Restart & Clear Output`

### Get historic Data

##### Data

- Open the file [historic_data.ipynb](https://github.com/andrebrener/cryptocurrency_data/blob/master/historic_data.ipynb).
- Choose the Coins that you like by adding them to the list. Make sure that their name is in the supported coin list and that it is written in capital letters. To know which coins are available see [coin_list.ipynb](http://localhost:8888/notebooks/coin_list.ipynb). 
- Choose the last day of your report.
- Choose how many days before the end date you want the data from.
- Choose the type of price from `close`, `high`, `low`, `open`.

##### Graph
Choose the time interval for the dates in the x-axis to be shown.

##### Export CSV
- Select File Name.
- Run the block.
- The file should be saved in the repo directory.
