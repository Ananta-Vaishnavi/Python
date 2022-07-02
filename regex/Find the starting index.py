import re
s1 = 'match after the last newline character'
s2 = 'and then you want to test'
s3 = 'this is good bye then'
s4 = 'who was there to see?'
a=re.search('is|the|was|to',s1)
print(a.span()[0])
