tekst="Anna, paweł, JulIA"

lista=tekst.split(", ")
print(tekst)
print(lista)
print(type(lista))

imie1= lista[0]
print(imie1)
imieDuze=imie1.upper()
print(imieDuze)

imieMale= imie1.lower()
print(imieMale)
print ("\nPOdaj swoje nazw ", end="")
nazw=input()
zawartosc=nazw.isalpha()
print(zawartosc)
nazw=""
print(nazw.isalpha())

text1= "Julia"
test2="Nowak"
print(text1+test2)

text="{1},Java i {0}".format("PHP","Phyton")
print(text)