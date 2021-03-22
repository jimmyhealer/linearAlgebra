from tools.martix import Martix
from tools.tool import inputMartix

def test_martix():
  m1 = inputMartix(2)
  m2 = inputMartix(2)

  print(m1 * m2)

if __name__ == '____':
  test_martix()