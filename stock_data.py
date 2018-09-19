import pandas as pd
import numpy as np
from pandas_datareader import data, wb
import datetime

df = pd.read_pickle('all_banks')
start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

#Bank of America
BAC = df.loc[:,'BAC']

#Citi
C = df.loc[:,'C']

#Goldman
GS = df.loc[:,'GS']

#JP
JPM = df.loc[:,'JPM']

#Morgan Stanley
MS = df.loc[:,'MS']

#Wells Fargo
WFC = df.loc[:,'WFC']

tickers = ['BAC','C','GS','JPM','MS','WFC']

####
#### This is redundant but done to practice concat
####
bank_stocks = pd.concat([df[tickers]],axis=1)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

max_close = bank_stocks.xs(key='Close',axis=1,level=1).max()

returns = pd.DataFrame()

for bank in tickers:
    returns[bank] = bank_stocks.loc[:,bank]['Close'].pct_change()

print(returns.head())
