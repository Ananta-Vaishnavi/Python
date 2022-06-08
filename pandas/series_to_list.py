#2) Write a Pandas program to convert a Panda module Series to Python list type.
import pandas as pd
df = pd.Series([1,2,3,4,5,6,7])
print(df.tolist())
