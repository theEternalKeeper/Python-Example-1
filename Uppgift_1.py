# Tentamen 2024-12-02 - 2024-12-03 Uppgift 1 (5p)
print('Uppgift 1\n')

# Kom ihåg: Du får använda modulen ”Math” i denna uppgift.
# Skriv kod för ditt program med utskrift här:

import math #importerar math så att pi och sqrt (square root) värden och metoder kan användas

def V_kon(r, h):
    volume = round(math.pi*(r*r)*h/3, 2) #beräknar volymen och rundar av den till 2 decimaler
    return volume #returnerar volumen

def A_kon(r, h):
    area = round(math.pi*r*math.sqrt((r*r)*(h*h)), 2) #Beräknar ytarean av en ihålig kon. Vill man ha total area lägger man till en beräkning för en cirkel med radius r
    return area

def Main():
    while True:
        print("Vill du\n1. Beräknar volym av en kon\n2. Beräknar mantelytan av en kon\n3. Avsluta Programmet") #skriver ut menyn
        inputMetod = (input("Ange det menyalternativ du vill köra: ")) #tar emot användar input och använder strängen för att aktivera respective funktion. Om de inte skriver en giltig string aktiveras Else och de för försöka igen
        if inputMetod == "1":
            inputRadius = float(input("Ange värden på radien: ")) #låter användaren ange radius
            inputhöjd = float(input("Ange värden på höjden: ")) #låter användaren ange höjd
            print(f'Volym av konen är {V_kon(inputRadius, inputhöjd)} cm^3') #Printar resultatet. Använder en F-sträng så att funktionen kan kallas inne i strängen med radius och höjd som argument, och deras return visas
        elif inputMetod == "2":
            inputRadius = float(input("Ange värden på radien: "))
            inputhöjd = float(input("Ange värden på höjden: "))
            print(f"Arean av konen är {A_kon(inputRadius, inputhöjd)} cm^2")
        elif inputMetod == "3":
            break #Avslutar while loopen och därmed programmet
        else:
            print("Ej giltigt val")
    
        
Main()