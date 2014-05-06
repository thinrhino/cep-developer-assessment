# Excersise 1

import pandas as pd

# Select only the required columns
use_cols = ['unique', 'fdntext', 'fldimp', 'undrfld', 'advknow', 'pubpol',
			'comimp', 'undrwr', 'undrsoc', 'orgimp', 'undrorg']

# Read in the data, converting values, '77' & '88' as NA
df = pd.read_csv('../input/xl.csv', index_col='unique', usecols=use_cols, na_values=('77', '88'))

# Preview the dataframe
df.head()

mean = df.groupby('fdntext').mean()
mean.to_csv('../output/mean_1.csv')
stats = mean.describe()
stats.to_csv('../output/stats_1.csv')