import pandas as pd
import numpy as np
from pandas_datareader import data, wb
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf

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
#print(std_banks_2015)

####
#### Plot defined as functions to manage number of figures
#### showing
####


def ms_distplot():
    sns.distplot(returns['MS Returns']['2015-01-01':'2015-12-31'],bins=100)
    plt.show()

def c_distplot():
    sns.distplot(returns['C Returns']['2008-01-01':'2008-12-31'],bins=100)
    plt.show()

#ms_distplot()
#c_distplot()


#### MORE VISUALIZATION SECTION
sns.set_style('whitegrid')
cf.go_offline()
init_notebook_mode(connected=True)

def eod_close_line_plot():
    bank_stocks.xs('Close',axis=1,level=1).plot()
    plt.legend(tickers)
    plt.show()

#eod_close_line_plot()

avg = pd.DataFrame()


#Create 30-day Moving Average DF
for tick in range(6):
    for row in range(29,len(bank_stocks)):
        avg.loc[row,tickers[tick] + ' 30-Day Moving Average'] = bank_stocks.xs('Close',axis=1,level=1).iloc[row-29:row,tick].mean()
avg.set_index(keys=bank_stocks.index[29:],inplace=True)

def price_vs_moving_avg(bank_tick):
    close = bank_stocks.xs('Close',axis=1,level=1).loc['2008-01-01':'2008-12-31'][bank_tick]
    t_day_avg = avg.loc['2008-01-30':'2008-12-31'][bank_tick + ' 30-Day Moving Average']

    fig = plt.Figure(figsize=(12,2))
    plt.plot(t_day_avg)
    plt.plot(close)

    plt.legend(['30-Day Avg',bank_tick +' Close'])

    plt.tight_layout()
    plt.show()

#price_vs_moving_avg('BAC')

def close_heatmap():
    bank_corr = bank_stocks.xs('Close',axis=1,level=1).corr()
    sns.heatmap(data=bank_corr,annot=True,cmap='coolwarm')
    plt.show()

#close_heatmap()
