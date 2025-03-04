# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pandas_datareader import data as pdr
import yfinance as yf
import seaborn as sns
>>> y_symbols = ['SPY','AMZN', 'A']
>>> from datetime import datetime
>>> startdate = datetime(2019,12,1)
>>> enddate = datetime(2022,12,15)
>>> data = yf.download(y_symbols, start=startdate, end=enddate)
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from arch import arch_model
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.stattools import jarque_bera
from statsmodels.stats.stattools import durbin_watson

returns = data.Close.pct_change().dropna()

Z = returns[['SPY','AMZN']]  
# Compute correlation matrix
corr_matrix = Z.corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

X1 = returns[['SPY']]
Y1 = returns['AMZN']

X1 = X.iloc[1:]
Y1 = y.iloc[1:]







X1 = sm.add_constant(X1, prepend=True)
modelo = sm.OLS(endog= Y1, exog=X1)
modelo = modelo.fit()
print(modelo.summary())

modelo.summary()



white_test = het_white(modelo.resid,  modelo.model.exog)
labels = ['Test Statistic', 'Test Statistic p-value']
print(dict(zip(labels, white_test)))

# Prueba de Jarque-Bera (normalidad de residuos)
jb_test = jarque_bera(modelo.resid)
print("Jarque-Bera Test: Estadístico =", jb_test[0], ", p-valor =", jb_test[1])

# Prueba de Durbin-Watson (autocorrelación)
dw_test = durbin_watson(modelo.resid)
print("Durbin-Watson Test:", dw_test)




data = data.iloc[1:]
fig, ax = plt.subplots(1, 1, figsize=(6,4))
ax.scatter(x=returns.AMZN, y=returns.SPY, alpha= 0.8)
ax.set_xlabel('S&P')
ax.set_ylabel('ret');

d = np.polyfit(returns.AMZN,returns.SPY , 1)

p = np.poly1d(d)

plt.plot(returns.AMZN, p(returns.AMZN), "r--")

plt.show()