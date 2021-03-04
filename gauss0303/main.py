from tools.tool import inputMartix
import sys

if __name__ == '__main__':
  inline = sys.argv[1] == 'inline'
  while True:
    problem = int(input('題號：'))  
    if inline: print(problem)
    if problem == 0: break
    
    if problem == 1:
      gaussJordan()
    elif problem == 2:
      martix = inputMartix(2)
      for i in martix:
        print(i)
      print('\n反矩陣結果：')
      for i in inverse(martix):
        for j in i:
          print(j, end=' ')
        print()
      print()      
    elif problem == 3:
      rank = int(input('幾階:'))
      if inline: print(rank)
      martix = inputMartix(rank)
      martix2 = inputMartix(rank)
      if inline:
        for i in martix:
          print(i)
        for i in martix2:
          print(i)
      print('結果：%s' % '相同' if isabequalba(martix, martix2) else '不同')
      print()      
