from tools.martix import Martix
from tools.tool import inputMartix

def test_martix():
  m1 = Martix([Martix([1,2,3]), Martix([4,2,7]), Martix([8,9,3])])
  m2 = Martix([Martix([1,2,3]), Martix([4,2,7]), Martix([8,9,3])])

  print(m1 * m2)

if __name__ == '__name__':
  test_martix()