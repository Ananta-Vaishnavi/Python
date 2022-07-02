import re
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
a=[x for x in items if re.search(r'[aw]',x)]
print(a)
