# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:12:57 2022

@author: USER
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf

from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.diagnostic import het_white
#%%
# import data

def get_data(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start, end)
    stockData = stockData['Close']

#%%
stockList = ['META', '^GSPC']

stocks = [stock + '.AX' for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)
data = yf.download(stockList, start=startDate, end=endDate)['Close']
data = data.dropna()

#%%

data['FBret'] = data['META'].pct_change()
data['SP'] = data['^GSPC'].pct_change()

X = data[['SP']]
y = data['FBret']

X1 = X.iloc[1:]
Y1 = y.iloc[1:]

X1 = sm.add_constant(X1, prepend=True)
modelo = sm.OLS(endog= Y1, exog=X1)
modelo = modelo.fit()
print(modelo.summary())
#%%
#modelo.summary()
#print

#%%
white_test = het_white(modelo.resid,  modelo.model.exog)
labels = ['Test Statistic', 'Test Statistic p-value']
print(dict(zip(labels, white_test)))

#%%
data = data.iloc[1:]
fig, ax = plt.subplots(1, 1, figsize=(6,4))
ax.scatter(x=data.FBret, y=data.SP, alpha= 0.8)
ax.set_xlabel('S&P')
ax.set_ylabel('ret');

d = np.polyfit(data.FBret,data.SP , 1)

p = np.poly1d(d)
#%%
plt.plot(data.FBret, p(data.FBret), "r--")

plt.show()

#%%
z=np.polyfit(data.FBret, data.SP, 2)
p= np.poly1d(z)
import pylab as plb
plb.plot(data.FBret,p(data.FBret), 'r-.')
plt.show()


# %%
