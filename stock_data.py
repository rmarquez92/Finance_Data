import pandas as pd
import numpy as np
from pandas_datareader import data, wb
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

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
    returns[bank + ' Returns'] = bank_stocks.loc[:,bank]['Close'].pct_change()

# sns.pairplot(data=returns[1:])
# plt.show()

min_returns_dates = returns.idxmin()
max_returns_dates = returns.idxmax()
std_banks = returns.std()
std_banks_2015 = returns['2015-01-01':'2015-12-31'].std()
print(std_banks_2015)
