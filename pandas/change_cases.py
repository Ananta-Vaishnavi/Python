#8) Write a Pandas program to convert all the string values to upper, lower cases in a given pandas series. Also find the length of the string values.
import pandas as pd
import numpy as np
s = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print("Original series:")
print(s)
print("Convert all string values of the said Series to upper case:")
print(s.str.upper())
print("Convert all string values of the said Series to lower case:")
print(s.str.lower())
print("Length of the string values of the said Series:")
print(s.str.len()) 
