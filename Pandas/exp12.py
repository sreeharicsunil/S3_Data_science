import pandas as pd
from pandas import date_range

sr = pd.Series(pd,date_range('2021-05-01','2021-05-12',freq = 'D'))
print(sr.to_string(index=False))