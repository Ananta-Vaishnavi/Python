import re
items = items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']
a=[i for i in items if re.search('^hand.+',i)]
print(a)
