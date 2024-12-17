# Tentamen 2024-12-02 - 2024-12-03 Uppgift 4 (5p)
print('Uppgift 4\n')

# Kom ihåg: Du får inte lägga till eller ta bort kod, utan du får enbart justera redan skriven kod för att hitta felen och korrigera dessa. 
# OBS!!! Skriv en kommentar till varje ändring du gör, okommenterade ändringar ger inga poäng. 

rader = int(input("Ange antal rader: "))

k = 0

for i in range(1, rader+1):
    for j in range(-10, (rader-i)-1): #skiftate alla + i denna rad till - så att det blir en pyramid, då "startpunkten" blid mindre och mindre istället för högre, och satte startpunkten some negativt för att ge mer ytrymme, då denna loop läggertill tomt utrymme i början.
        print(end= " ")

    while k!=(3*i-2): #Bytte 2 mot 3 och +1 till -2 för att se till att antalet stjärnor ökar i stagi takt och att det startar vid 1 istället för 3, och ** till * för att göra så att takten inte ökar
        print("*", end="") # Balanserade "* " till "*" så att pyramiden ser bättre ut
        k += 1
    
    k = i
    print()