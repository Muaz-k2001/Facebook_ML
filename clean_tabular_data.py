import pandas as pd

f = pd.read_csv('Products.csv', lineterminator='\n')
f['price'] = f['price'].str.strip('£')
f['price'] = f['price'].str.replace(',','')
f['price'] = f['price'].astype('float64')
print(f)