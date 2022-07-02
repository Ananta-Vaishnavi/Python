import re

# Example string
s = """Hello from shubhamg199630@gmail.com
		to priya@yahoo.com about the meeting @2PM"""
lst = re.findall('\S+@\S+', s)	
print(lst)
