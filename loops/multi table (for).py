n=int(input('Enter a number '))
r=int(input('Enter the range '))
for i in range(1,r+1):
  a=i*n
  print('{}*{}={}'.format(n,i,a))
