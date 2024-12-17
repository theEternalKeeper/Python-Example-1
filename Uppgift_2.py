# Tentamen 2024-12-02 - 2024-12-03 Uppgift 2 (5p)
print('Uppgift 2\n')

# Kom ihåg: Du får använda modulen importera "randint" från modulen ”random” i denna uppgift.
# Skriv kod för ditt program med utskrift här:

from random import randint #Importerar randint från random

nummerlista = []
listlängd = randint(0, 100) #Genererar en slumpmässig längd på listan

for i in range(listlängd):
    nummerlista.append(randint(0,9)) #Lägger till ett slumpmässigt tal mellan 0 och 9, inklusive dessa nummer, till listan, tills listan är tillräckligt lång

print("Nummer i listan är: ")

print(nummerlista)
    
for i in range(0, 10):
    print(f'Det finns {nummerlista.count(i)} exempel av {i} i listan') #beräknar och skriver ut hur många exempel det finns av varje nummer i listan.