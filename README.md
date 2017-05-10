# Crypto Prices

Crypto Prices is an application that uses the CryptoCompare API to get historic prices of different cryptocurrencies.

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

Each block is run separately by pressing the Play button (screenshot below) or with shortcut of Shift+Enter.

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
- Run the 2nd & 3rd blocks of code.

##### Graph
- In the 5th block:
  - Choose the time interval for the dates in the x-axis to be shown.
- Run the 5th block.

##### Export CSV
- In the 6th block:
  - Select File Name.
- Run the block. The file should now be saved in the repo directory.
