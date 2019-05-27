def delenie(a,b):
    try:
          result = (a**2+b)/(a+b)**2
          print(f'\n{a}^2+b/({a}+{b})^2={result}')
          
    except ZeroDivisionError:
          print('Error')

a= input('POdaj a\t')
b= input('POdaj b\t')

print(delenie(float (a),float(b)))

####################################################


def obliczneia(a,b,c):
    try:
         if (c>0):
            result = a+b**2
            print(f'\n{a}+{b}^2={result}')
         elif (c<0):
            result = a-b**2
            print(f'\n{a}-{b}^2={result}')
         else:
            result= 1/(a-b)
            print(f'\n1/({a}-{b})={result}')         
    except ZeroDivisionError:
          print('Error')
a= input('Podaj a\t')
b= input('Podaj b\t')
c= input('Podaj C\t')

print(obliczneia(float(a), float(b), float(c)))


###################################################

