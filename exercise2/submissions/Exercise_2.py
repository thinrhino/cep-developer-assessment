
# coding: utf-8

# In[1]:

from scipy.stats import percentileofscore
import pandas as pd


# In[2]:

mean = pd.read_csv('./exercise2/input/mean.csv', index_col='fdntext')


# In[3]:

mean.head()


# In[4]:

def percentile(col):
    percentile_list = []
    for r in col:
        percentile = percentileofscore(col, r, kind='mean')
        percentile_list.append(percentile)
    return percentile_list
    
percentile_score = mean.apply(percentile, axis=0)
percentile_score.to_csv('./exercise2/output/pct.csv')

