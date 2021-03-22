n = 30000
p = 0.03
t = 0

for i in range(60):
  t += (t + n) * p
  if i <= 20:
    t += n
  print(t, t - n * (20 if (i + 1) > 20 else (i + 1))) 
