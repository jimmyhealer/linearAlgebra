from random import randint
print(1)
for i in range(100):
  for j in range(100):
    if randint(0, 100) < 50:
      print(randint(1, 10000), end=' ')
    else:
      print('{}/{}'.format(randint(1, 500), randint(1, 10000)), end=' ')
  print()
print(0)
