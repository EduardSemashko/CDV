wysokosc_input= input('POdaj strone:\t')
wysokosc=int(wysokosc_input)
for i in range (0, wysokosc):
    for j in range(0, i+i):
        print ("*", end='')
    print("*\r")
    
##############################

a= int(input("Podaj pierwsa granice przedzialu:\t"))
b= int(input("Podaj druga granice przedzialu\t:"))
zapas=b
if(b<a):
    b=a
    a=zapas
    print(a,b,zapas)
    for i in range(a,b):
        if(i%2==0):
            print(i)
else:
    for i in range(a,b):
        if(i%2==0):
            print(i)
