hight = int(input("podaj wys"))
wight = int(input("POdaj szer"))
char = '&'
for i in range(hight):
    if i == 0 or i == hight - 1:
        for j in range(wight):
            print(char, end='')
    else:
        print(char, end='')
        for j in range(1, wight - 1):
            print(' ', end='')
        print(char, end='')
    print()


m =int(input("Podaj strone"))
n=m
middle=m
print(middle)
for i in range(m):
    for j in range(2*n-1):
        print('*' if j == n-1 - i or j == n-1 + i or i == m-1 else ' ', end='')
    print()
for a in range(1, middle-1):
    print(' ', end='')
print('888', end='')