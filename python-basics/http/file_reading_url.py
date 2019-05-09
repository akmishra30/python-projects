import io
import requests
import pandas as pd

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&apikey=U67HYK017B5XMM0T&datatype=csv"

## Reading data in text format
#res = requests.get(url).text
## Reading data in text format
#res = requests.get(url).json
## Reading data in stream format
res = requests.get(url).content

data = pd.read_csv(io.StringIO(res.decode('utf-8')))

print(data)