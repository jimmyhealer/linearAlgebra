def inverse(A, b):
  det = 0.0
  for i in range(3):
    _a = int(i == 0)
    _b = int(2 - int(i == 2))
    det += ((-1) ** i) * A[0][i] * (A[1][_a] * A[2][_b] - A[1][_b] * A[2][_a])
  if det == 0:
    print('det(A) = %s , A 不可逆' % det)
    return
  print('det(A) = %s , 可逆' % det)
  B = [[0.0, 0.0, 0.0] for _ in range(3)]
  test = 0
  for i in range(3):
    for j in range(3):
      _ja = int(j == 0)
      _ia = int(i == 0)
      _jb = 2 - int(j == 2)
      _ib = 2 - int(i == 2)
      B[i][j] = ((-1) ** (i + j)) * (A[_ja][_ia] * A[_jb][_ib] - A[_ja][_ib] * A[_jb][_ia]) / det
      test += B[i][j]
  x = [0, 0, 0]
  for i in range(3):
    for j in range(3):
      if B[i][j] == -0.0:
        print('B[%s][%s] = ' % (i, j), -B[i][j])
      else:
        print('B[%s][%s] = ' % (i, j), B[i][j])
      A[j][i], b[j] = b[j], A[j][i]
    for k in range(3):
      _a = int(k == 0)
      _b = int(2 - int(k == 2))
      x[i] += (-1) ** k * A[0][k] * (A[1][_a] * A[2][_b] - A[1][_b] * A[2][_a]) / det;
    for k in range(3):
      b[k], A[k][i] = A[k][i], b[k]
  text = ['x', 'y', 'z']
  for i in range(3):
    print('%s = %s' % (text[i], x[i]))
    

if __name__ == '__main__':
  A = [[0 for _i in range(3)] for _j in range(3)]
  b = [0 for _i in range(3)]
  print('輸入A矩陣(3 X 3):')
  for i in range(3):
    A[i] = list(map(float, (input().split())))
  b = list(map(float, (input('輸入B矩陣:\n').split())))
  inverse(A, b)
