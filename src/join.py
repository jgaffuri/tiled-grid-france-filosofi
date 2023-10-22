import pandas as pd


# read
d19 = pd.read_csv('2019_met.csv')
d17 = pd.read_csv('2017_met.csv')
d15 = pd.read_csv('2015_met.csv')



# join 1
#result1 = pd.merge(df1, df2, on='common_column1', how='inner')

# join 2
#result2 = pd.merge(result1, df3, on='common_column2', how='inner')

# save
#result2.to_csv('out.csv', index=False)
