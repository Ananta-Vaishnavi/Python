#9) Write a Pandas program to count of occurrence of a specified substring in a DataFrame column.
import pandas as pd
df = pd.DataFrame({
    'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
df['count'] = list(map(lambda x:x.count("2"),df['name_code']))
print(df)
