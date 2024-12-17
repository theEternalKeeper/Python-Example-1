# Tentamen 2024-12-02 - 2024-12-03 Uppgift 3 (5p)
print('Uppgift 3\n')

# Kom ihåg: Du får använda modulen importera "randint" från modulen ”random” i denna uppgift.
# Skriv kod för ditt program med utskrift här:

from random import randint #Importerar randint från random

listA = []
listB = []
listC = []

längd = int(input("Hur långs ska listorna vara? Ange ett nummer: "))

for i in range(längd): #Lägger till antal slumpmässiga värden till listor A och B, och en sträng som kombinerar dem i lista C. Antalet värden är lika med längden
    listA.append(randint(1, 20))
    listB.append(randint(1, 20))
    listC.append(f"{listA[i]} + {listB[i]} = {listA[i]+listB[i]}")
    
print("Lista A | Lista B | Lista C")
print("---------------------------")
for i in range(längd):
    print(f"{listA[i]:^8}| {listB[i]:^8}| {listC[i]}") #Skriver ut listorna med korrekt utrymme för att tabellen ska se bra ut