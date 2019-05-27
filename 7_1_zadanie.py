def div(x,y):
     try:
          result = x//y
          print(f'\n{x}/{y}={result}')
          return x/y
     except:
          print('Error')

print(div(3,0))