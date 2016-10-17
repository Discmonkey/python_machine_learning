import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 10, 12)

df = web.DataReader('XOM', 'yahoo', start, end)


# only plot on column

df['High'].plot()
df['Low'].plot()
plt.legend()
plt.show()