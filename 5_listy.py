programowanie=['Python','C#','JS','PHP','Java']
print(programowanie)
print(type(programowanie))

pierwszy= programowanie[0]
print(pierwszy)

trzyElementy= programowanie[0:3]
print(trzyElementy)

ostatni= programowanie[-1]
print(ostatni)

# dodawanie do listy

programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementow listy
ile= programowanie.count('Python')
print(ile)

#ilosc elementow
iloscElem=len(programowanie)
print(iloscElem)

#polaczenie list
innejezyki=['C++','C']
print('Poloczenie list')
programowanie.extend(innejezyki)
print(programowanie)

#cleaar
nowa=programowanie
print('Lista nowa: ', end='')
print(nowa)
programowanie.clear()
print('Programowanie: ', end='')
print(programowanie)

#