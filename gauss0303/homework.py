from tools.martix import Martix
from tools.fraction import Fraction
from tools.tool import printMartix, Plug


def gaussJordan(martix):
  # for i in range(len(martix)):
  #   extend = []
  #   for j in range(len(martix)):
  #     if i == j:
  #       extend.append(Plug.one)
  #     else:
  #       extend.append(Plug.zero)
  #   martix[i].extend(extend)

  print(martix)
  # process
  # for i in range(1, 3):
  #   martix[i] = martix[i] * (-martix[0][0] / martix[i][0]) + martix[0]

  # martix[2] = martix[2] * (-martix[1][1] / martix[2][1]) + martix[1]
  
  # for i in range(3):
  #   martix[i] = martix[i] * (Plug.one / martix[i][i])

  # for i in range(2):
  #   martix[i] = martix[2] * (-martix[i][2] / martix[2][2]) + martix[i]

  # martix[0] = martix[1] * (-martix[0][1] / martix[1][1]) + martix[0]

  # printMartix(martix)


def inverse(martix):
  det = martix[0][0] * martix[1][1] - martix[0][1] * martix[1][0]
  det = Plug.one / det 
  if det == Plug.zero:
    print('No inverse martix!')
    return
  return [Martix([martix[1][1] * det, -martix[0][1] * det]),
          Martix([-martix[1][0] * det, martix[0][0] * det])]

def ismartixeq(martix, martix2):
  for i in range(len(martix)):
    if martix[i] != martix2[i]:
      return 0
    return 1

def isabequalba(martix, martix2, rank=2):
  if ismartixeq(martix, martix2): return 1
  if rank == 2:
    q = inverse(martix)
    for i in range(len(martix)):
      if martix2[i] != q[i]:
        return 0
    return 1
  else:
    q = gaussJordan(martix)  

if __name__ == '__main__':
  gaussJordan()
