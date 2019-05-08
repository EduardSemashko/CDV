#listy

imiona=['Julia','Anna','Tomasz',]
print(type(imiona))
imiona.append('Pawel')
print(len(imiona))

#tuple
nazwiska=('Nowak','Kowalski')
print(nazwiska)
print(type(nazwiska))

#slowniki
osoba={'imie':'Julia', 'nazwisko':'Nowak', 'wiek': 25}
print(osoba)
print(type(osoba))
print(osoba['nazwisko'])
print(osoba.get('wzrost','brak danych'))
print(osoba.get('imie','brak danych'))
print(osoba.keys())