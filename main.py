from tools.tool import inputMartix, printMartix
from gauss0303.homework import gaussJordan, inverse, isabequalba

import sys

if __name__ == '__main__':

  display = 'display' in sys.argv
  while True:
    problem = int(input('problem: '))  
    print()
    if display: print(problem)
    if problem == 0: break
    

    if problem == 1:
      martix = inputMartix(3, display=display, displayText='input: ', isextend=True)
      gaussJordan(martix)

    elif problem == 2:
      martix = inputMartix(2, display=display, displayText='input: ')
      print('\nresult: ')
      printMartix(inverse(martix))
      
    elif problem == 3:
      rank = int(input('num: '))
      if display: print(rank)
      martix = inputMartix(rank, display=display, displayText='input: ')
      martix2 = inputMartix(rank, display=display, displayText='input: ')
      print('result: %s' % 'similar' if isabequalba(martix, martix2, rank=rank) else 'unsimilar')

    print()      