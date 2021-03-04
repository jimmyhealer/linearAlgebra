from tools.fraction import Fraction
from tools.martix import Martix

class Plug:
  one = Fraction(1, 1)
  zero = Fraction(0, 1)

def inputMartix(rank: int, display=False, displayText=None, isextend=False):
  martix = []
  for _ in range(rank):
    temp = input().split()
    number = []
    for i in temp:
      if i[0] == '/':
        number.append(Fraction(0,1))
      elif '/' in i and i[-1] != '/':
        tempnumber = list(map(int, i.split('/')))
        if tempnumber[1] == 0:
          number.append(Fraction(tempnumber[0], 1))
        else:
          number.append(Fraction(tempnumber[0], tempnumber[1]))
      else:
        number.append(Fraction(int(i.split('/')[0]), 1))
    martix.append(Martix(number, isextend=isextend))
  if display:
    if displayText: print(displayText)
    printMartix(martix)
  return martix

def printMartix(martix) -> bool:
  for i in martix:
    print(i)
  return True