def F(x):
  if x == 0:
    l = 1
  elif x == 1:
    l = 3
  elif x ==2:
    l = 2
  else:
    l = F(x-1)*F(x-3)
  return l