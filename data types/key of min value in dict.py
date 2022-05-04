def min_value_dict(student_info):
  l=[]
  for k,v in student_info.items():
    l.append(v)
  a=min(l)
  for x,y in student_info.items():
    if a==y:
      return x
print(min_value_dict({'sri': 82,'rama': 65,'vishnu': 75}))
