import re
items = ['lovely', 'dentist', 'lonely', 'eden', 'fly', 'dent']
a=[i for i in items if re.search('^den|ly$',i)]
print(a)
