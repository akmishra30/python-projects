import io
import requests
import pandas as pd

data = pd.read_csv('python-basics/data-analysis/data/daily_GOOGL.csv')
# csv files column :- timestamp,open,high,low,close,volume
data = data.dropna() # Drop the rows where atleast 1 column is missing

## Data slicing with pandas
df = pd.DataFrame(data)
# reading first two rows -- slicing
#print(df.head(2))
# reading last two rows -- slicing
#print(df.tail(2))
df = df.head(5)
# Data merging with pandas
df1 = df[['timestamp', 'open', 'close']]
df2 = df[['timestamp', 'high', 'low']]
print(df1)
print(df2)

df_mrgd = pd.merge(df1, df2)

# Joining two data frame
#Key point: The joining dataframe must have diff column
#df_mrgd = df1.join(df2)

print(df_mrgd)
