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
