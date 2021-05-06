import pandas as pd

df = pd.read_csv('registro botanas.csv')

print(df.loc[[2], ['Accion']])