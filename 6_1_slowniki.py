
pracownik={'Imie':'Karol', 'Nazwisko':'Warzywniak','Miasto':'Charków', 'wiek':'30', 'ImionaDzieci':['Tomasz','Lukasz'], 'ImionaRodzicow':['Pawel','Nian']}
print(pracownik)

klucz='wiek'

if klucz in pracownik:
    del pracownik[klucz]
    print(f'Klucz {klucz} zostal usunienty')
else:
    print(f'klucz{klucz} nie zostal usunienty')

print(pracownik)
print(pracownik.keys())
print(pracownik.values())
print(list(pracownik.values()))
print(pracownik.items())

for value in pracownik.values():
    print(value, end=', ')

print()

for key, value in pracownik.items():
    print(key, value)