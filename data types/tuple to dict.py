def tuple_dict(t):
  t=dict(t)
  t = {v: k for k, v in t.items()}
  return t
print(tuple_dict(((2, "w"),(3, "r"))))
