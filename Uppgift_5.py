# Tentamen 2024-12-02 - 2024-12-03 Uppgift 5 (20p)
print('Uppgift 5\n')

# Kom ihåg: Kommentera intentionen med din kod, vad ska hända
# Modulen "pandas" får inte användas när ni skriver ut graferna. Annars är det valfritt vilka moduler ni använder
import csv
import matplotlib.pyplot as plt

def Read_file(file_name):
    with open(file_name, mode ='r', encoding='utf-8') as file: #läser in filerna vars namn har skickats i read mode
        csvFile = list(csv.reader(file, delimiter=";")) #skapar en lista av filen
    return csvFile

def Antal_bilar(kamera_Data):
    current_speed_lista = []
    fart_lista = []
    speed_tally = []
    
    for i in range(1, len(kamera_Data)):
        if kamera_Data[i][1] not in current_speed_lista: #Skapar en lista med de olika fart begränsningarna
            current_speed_lista.append(kamera_Data[i][1])
        fart_lista.append(kamera_Data[i][1]) #gör en lista med alla fart begränsningar
    
    current_speed_lista.sort()
    fart_lista.sort()
    
    for i in current_speed_lista:
        print(f"Det finns {fart_lista.count(i)} mätningar där gällande hastighet är {i} km/h") #Använder current_speed_lista som referens för att se hur många exempel av varje hastighet dyker up, då den har bara ett exempel av varje hastighet
        speed_tally.append(fart_lista.count(i)) #skapar en lista med hur många resultat det finns av varje hastighet för att användas i grafen

    print(f"Totalt passerade {len(fart_lista)} bilar.")
    print("\n \n")

    plt.ylabel("Antal Bilar")
    plt.xlabel("Gällande hastighet")
        
    plt.bar(current_speed_lista, speed_tally, width=0.1) 
    plt.show()       

def Antal_kameror(plats_data):
    plats_räkning = []
    plats_lista = []
    
    for i in range(1, len(plats_data)):
        if plats_data[i][3] not in plats_lista: #Samma princip som i den förra uppgiften, men snarare än hastigheter är det baserat på platser
            plats_lista.append(plats_data[i][3])
        plats_räkning.append(plats_data[i][3])
    
    plats_lista.sort() #Sorterar så det blir if alfabetisk ordning
    plats_räkning.sort()
    
    print(f"{"Kommun":15} {"Antal Kameror":3}")
    print("==============================")
    for i in plats_lista:
        print(f"{i:15} {plats_räkning.count(i):3}")
    print("==============================")
    print(f"Det finns totalt {len(plats_data)} antal kameror")
    print("\n \n")
    
def Bilar_timme(kamera_data):
    hour_list = []
    hour_count = []
    
    for i in range(1, len(kamera_data)):
        hour = kamera_data[i][4]
        if int(hour[0:2])>=7 and int(hour[0:2])<17: #skapar en lista med alla timslag up till 16:59:59
            hour_list.append(int(hour[0:2]))

    hour_list.sort()
    
    hour_dict = list(dict.fromkeys(hour_list)) #skapar en extra lista där alla extranummer är borttagna
    
    for i in hour_dict:
        hour_count.append(hour_list.count(i)) #Gör en lista med antalet gånger varje timmslag dyker upp 
        
    plt.ylabel("Antal registrerade fordon")
    plt.xlabel("Tid")
    plt.title("Antal fordon per timma mellan 07 och 17")
    plt.plot(hour_dict, hour_count)
    plt.show()
    
    #Försökte använda datetime men kunde ej få det att funka lika smidigt då jag inte kunde få plt att använda timmarna som x-axel utan att det blev en massa konverseings krångel. Mer övning på det behövs
    
    

def Main():
    kameraData = []
    platsData = []
    
    while True:
        print(f"{"Meny":^5}")
        print("===================")
        print("1. Hämta Data\n2. Analysera Data\n3. Analysera Data\n4. Analysera Data\n5. Avsluta Program")
        val = input("Välj meny alternativ (1-5): ")
        
        if val == "1":
            fil_val = input("Vilken fil? kameraData.csv eller platsData.csv? ")
            if fil_val == "kamera data" or fil_val == "Kamera data" or fil_val == "kameraData-1-1.csv" or fil_val == "kameraData.csv": #Kollar om Input matchar något av de givna namnen. Lade till några extra
                try:
                    kameraData = Read_file("kameraData-1-1.csv") #Kallar Read_file med fil namnet
                    print(kameraData[0:3])
                except:
                    print("Filen hittas inte") #En exception som hindrar att programmet krashar om man råkar skriva fel eller har filen på fel ställe
            elif fil_val == "plats data" or fil_val == "Plats data" or fil_val == "platsData-1-1.csv" or fil_val == "platsData.csv":
                try:
                    platsData = Read_file("platsData-1-1.csv")
                    print(platsData[0:3])
                except:
                    print("Filen hittas inte")
            else:
                print("Inget giltigt svar")
        elif val == "2":
            try:
                Antal_bilar(kameraData)
            except:
                print("Kamera data ej hämtad.")
        elif val == "3":
            try: 
                Antal_kameror(platsData)
            except: 
                print("Platsdata ej hämtad")
        elif val == "4":
            try:
                Bilar_timme(kameraData)
            except:
                print("Kamera data ej hämtad.")
        elif val == "5":
            break
        else:
            print("Inget giltigt val")      
        
Main()