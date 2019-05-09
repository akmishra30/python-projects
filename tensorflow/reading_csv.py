import numpy as np
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import matplotlib.style as style

dataset = pd.read_csv('tensorflow/data/stocks.csv')
dataset = dataset.dropna()
dataset = dataset[['Date', 'Open', 'High', 'Low', 'Close']]
#print(dataset)

dataset['change'] = (dataset['Open'] - dataset['Close']) / dataset['Open'] * 100

#print(dataset['Open'][0], dataset['Close'][0] , diff, change, sep=" | ")

#print(dataset['change'])

#plt.plot(dataset['Date'], dataset['change'])
#plt.show()


url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&apikey=U67HYK017B5XMM0T&datatype=csv"
res = requests.get(url).content
data = pd.read_csv(io.StringIO(res.decode('utf-8')))

style.use('ggplot')

x = data['open']
y = data['close']
plt.plot(x, y, 'g', label='Close', linewidth=2, color='B')
plt.ylabel('Open')
plt.xlabel('Close')
plt.title('Stock Movement')

plt.legend()
plt.grid(True, color='G')

plt.show()