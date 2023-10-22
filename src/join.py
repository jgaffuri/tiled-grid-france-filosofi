import pandas as pd

# /home/juju/pythonvenvgridDE/bin/python ./src/join.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/join.py

# read
geo = "met"
d19 = pd.read_csv("./tmp/2019_" + geo + ".csv")
d17 = pd.read_csv("./tmp/2017_" + geo + ".csv")
d15 = pd.read_csv("./tmp/2015_" + geo + ".csv")



# join 1
#result1 = pd.merge(df1, df2, on='common_column1', how='inner')

# join 2
#result2 = pd.merge(result1, df3, on='common_column2', how='inner')

# save
#result2.to_csv('out.csv', index=False)
