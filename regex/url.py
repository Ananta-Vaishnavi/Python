import re
a='''Now a days you can learn almost anything by just visiting http://www.google.com. But if you are completely new to computers or internet then first you need to leanr those fundamentals. Next
you can visit a good e-learning site like - https://www.tutorialspoint.com to learn further on a variety of subjects.'''
print(re.findall(r'http.+?com',a))
