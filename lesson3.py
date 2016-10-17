import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import urllib.request as req


style.use('fivethirtyeight')


df = pd.read_csv('dataSources\\ZILL-Z77006_3B.csv')
df.set_index('Date', inplace=True)

df.to_csv('newcsv2.csv')
df['Value'].to_csv('a.csv')

# reference multiple columns df[['a','b']]

# set index on import
df = pd.read_csv('dataSources\\ZILL-Z77006_3B.csv',index_col=0)

# set column name
df.columns = ['House_Prices']
df.head()

# save file without headers
df.to_csv('newcsv3.csv', header=false)

# read file and pass headers
df = pd.read_csv('newcsv3.csv', names = ['Date', 'House_Price'], index_col=0)

# rename column

df.rename(columns={'House_Price': 'House_Prices'}, inplace=True)

# download data from url

url = 'https://www.quandl.com/api/v3/datasets/FMAC/HPI.csv?api_key=qBzz2SFfJXUQw3sNF4X4'
fp = req.urlopen(url)
df = pd.read_csv(fp,index_col=0)


# challenge 2
f = open('dataSources\\tough_text_file.csv')
ham_spam = []
text = []
for line in f:
    arr = line.split(',', 1)
    ham_spam.append(arr[0])
    text.append(arr[1])

df = pd.DataFrame({'ham_spam':ham_spam,'text':text})