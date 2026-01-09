import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime


#-------------------------------------- POMOCNÉ FUNKCE -------------------------------------#
#------------------ GENEROVÁNÍ BODŮ ------------------#
def Stika():
    vaha = round(random.uniform(0.5, 4.2), 2) #vygenerování náhodných čísel od 0.5 do 4 (na 2 desetinná místa)
    sirka = round(random.uniform(5, 12), 2) 

    format = str(vaha) + "," + str(sirka) + "," + str(1) #ve formátu např.: 1,1,1 
    return format

def Kapr():
    vaha = round(random.uniform(4, 10), 2) 
    sirka = round(random.uniform(13, 25), 2) 
    
    format = str(vaha) + "," + str(sirka) + "," + str(-1)
    return format
#-----------------------------------------------------#

#------------------- NAČÍTÁNÍ BODŮ -------------------#
def NacteniBodu():
    mnozinaboduX = [] #pomocná proměnná k uložení x-souřadnic bodů
    mnozinaboduY = [] #pomocná proměnná k uložení y-souřadnic bodů
    mnozinaboduTrida = [] #pomocná proměnná k uložení tříd bodů (3. číslo)

    try:
        with open("ucici.txt", "r") as file:
            while(True):
                radek = file.readline()

                if (radek == ""): #pakliže je řádek prázdný = konec dokumentu (konec načítání)
                        break
                
                hodnoty = radek.strip().split(",") #"Split" pomocí čárek (protože vše uložené ve formátu např.: 1,1,1)

                x = float(hodnoty[0]) #"Plt" potřebuje floaty, aby správně vykreslovalo 
                y = float(hodnoty[1])
                trida = int(hodnoty[2])

                mnozinaboduX.append(x)
                mnozinaboduY.append(y)
                mnozinaboduTrida.append(trida)

    except FileNotFoundError:
        print("Soubor nenalezen.")

    return mnozinaboduX, mnozinaboduY, mnozinaboduTrida
#-----------------------------------------------------#

#------------------ ZAPSÁNÍ VÝSLEDKŮ -----------------#
def ZapsaniVysledku(nadrovina, cyklus, krok, celkemSpatneKlas, pocatecniParametrUceni, pocetBodu, konecPU, konecSpatneK):
    cas = datetime.now() #název souboru je vždy přesné datum, kdy byl program dokončen (každý nový výsledek/spuštění programu se ukládá do nové textového souboru s jiným názvem)
    timestamp = cas.strftime("%Y-%m-%d_%H-%M-%S") #rok-měsíc-den-hodina-minuta-sekunda
    nazev_file = f"vysledek_{timestamp}.txt"
    
    with open(nazev_file, "w", encoding="utf-8") as file:
        try:
            file.write(f"Finalni nadrovina: {nadrovina}\n")
            file.write(f"Pocatecni parametr uceni: {pocatecniParametrUceni}\n")
            file.write(f"Konecny parametr uceni: {konecPU}\n")
            file.write(f"Pocet cyklu: {cyklus}\n")
            file.write(f"Pocet kroku (pocet zmen nadroviny): {krok}\n")
            file.write(f"Spatne klasifikovane body na konci: {konecSpatneK}\n")
            file.write(f"Pocet celkem spatne klasifikovanych bodu: {celkemSpatneKlas}\n")
            file.write(f"Pocet bodu: {pocetBodu}\n\n")  

        except FileNotFoundError:
            print("Soubor nenalezen.")
#-----------------------------------------------------#

#------------------ VYKRESLENÍ BODŮ ------------------#
def SpusteniVykresleni(): #pomocná funkce, která předchozí funkce zavolá
    X, Y, Trida = NacteniBodu()

    class0_X, class0_Y, class1_X, class1_Y = SouradniceBodu(X, Y, Trida)

    VykresleniBodu(class0_X, class0_Y, class1_X, class1_Y)

def SouradniceBodu(souradniceX, souradniceY, trida): #pomocná funkce k vykreslení bodů 
    class0_X = []
    class0_Y = []
    class1_X = []
    class1_Y = []

    for i in range(len(trida)): #podle třídy (zde označeno jako třída 0 a 1) rozdělím x a y souřadnice 
        if trida[i] == -1:
            class0_X.append(souradniceX[i])
            class0_Y.append(souradniceY[i])
        
        else:
            class1_X.append(souradniceX[i])
            class1_Y.append(souradniceY[i])

    return class0_X, class0_Y, class1_X, class1_Y

def VykresleniBodu(class0_X, class0_Y, class1_X, class1_Y): #samotné vykreslení bodů
    plt.plot(
        class0_X,
        class0_Y,
        marker='x',
        markersize=5,
        linestyle='',
        color='blue',
        label='Kapři' #vykreslení bodů ze třídy "-1", tedy kapři
    )

    plt.plot(
        class1_X,
        class1_Y,
        marker='x',
        markersize=5,
        linestyle='',
        color='red',
        label='Štiky' #vykreslení bodů ze třídy "1", tedy štiky
    )

    #legenda přesunuta mimo graf - nad graf doprostřed
    plt.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, 1.15),
        ncol=2
    )

    #důležité, aby "plt" správně škáloval velikost osy x a y
    xmin = min(class0_X + class1_X)
    xmax = max(class0_X + class1_X)
    ymin = min(class0_Y + class1_Y)
    ymax = max(class0_Y + class1_Y)

    plt.xlim(xmin - 1, xmax + 1)
    plt.ylim(ymin - 1, ymax + 1)

    #popis os
    plt.xlabel("Hmotnost (kg)", fontsize=12)
    plt.ylabel("Šířka (cm)", fontsize=12)

    #mřížka
    plt.grid()
#-----------------------------------------------------#

#---------------- VYKRESLENÍ NADROVINY ---------------#
def VykresliNadrovinu(nadrovina, bodyPocatecni): #je potřeba vyjádřit přímku jako y = ...
    '''
    x_data = [x for x, y in bodyPocatecni]
    
    x_min, x_max = min(x_data), max(x_data) #naleznu nejmenší a největší hodnotu x z dat
    x = np.linspace(x_min, x_max, 200) #"rovnoměrné" vytvoření osy x - vytvoří se 200 rovnoměrně vybraných hodnot mezi x_min a x_max
    '''
          
    xlim = plt.xlim()
    ylim = plt.ylim()

    #OBECNÝ PŘÍPAD: b != 0 ... y = (-c - a*x) / b ... neboli případ ax + by + c 
    if (nadrovina[1] != 0): #klasický případ y = ...
        x = np.array(xlim) #jen začátek a konec x-ose
        y = ( ( (((-1) * nadrovina[0]) * x) - (nadrovina[2]) ) / (nadrovina[1]) ) 
        plt.plot(x, y, color='green', label='Nadrovina') #label ponechán pro případ budoucí nutnosti přidání do legendy (popis, že daná "čára") je dělící nadrovina

    #PŘÍPAD SVISLÁ ČÁRA: a != 0 ... b = 0 ... ax + c = 0 ... neboli případ x = -c / a
    elif nadrovina[0] != 0:  # svislá čára
        x0 = ( ( (-1) * nadrovina[-1] ) / (nadrovina[0]) )
        plt.axvline(x=x0, color='green', label='Nadrovina')

    #PŘÍPAD 3: a = 0 ... b = 0 ... neboli případ c = 0 ... neměl by nastat
    else:
        plt.axvline(x = 0, color='green', label='Nadrovina')

#-----------------------------------------------------#
#-------------------------------------------------------------------------------------------#





#--------------------------------------- TŘÍDA NEURON --------------------------------------#
class Neuron:
    def __init__(self, nadrovina, parametrUceni, body):
        self.nadrovina = nadrovina
        self.parametrUceni = parametrUceni
        self.body = body
        self.cyklus = 0 #počet projetí všech bodů 
        self.krok = 1 #počet změn nadroviny
        self.celkemSpatneKlas = 0

        self.nejlepsiNadrovina = []
        self.nejmensiPocetSpatneKlas = float("inf")


    #---- POMOCNÉ FUNKCE PRO POČÍTÁNÍ S MATICEMI ----#
    def nasobeni_matic_cislem(self, matice, nasobek): #násobení matice skalárem
        vysledek = []

        for prvek in matice:
            novyPrvek = prvek * nasobek
            vysledek.append(novyPrvek)

        return vysledek 

    def soucet_matic(self, matice1, matice2):
        vysledek = []

        if (len(matice1) != len(matice2)): #pro součet matic musí být stejně dlouhé obě matice
            raise ValueError("Matice musí být stejně velké!")
        
        for i in range (len(matice1)):
            soucet = matice1[i] + matice2[i]
            vysledek.append(soucet)

        return vysledek
    
    def skalarni_soucin_matic(self, matice1, matice2):
        vysledek = 0

        if (len(matice1) != len(matice2)): #pro skalární součin matic musí být stejně dlouhé obě matice
            raise ValueError("Matice musí být stejně velké!")
        
        for i in range (len(matice1)):
            nasobek = matice1[i] * matice2[i]
            vysledek += nasobek

        return vysledek
    #------------------------------------------------#


    #----------- PERCEPTRONOVÝ ALGORITMUS -----------#
    def kontrola_bodu(self, bod):
        trida = bod[-1]                              
        kontrolovanyBod = bod[:-1] + (1,) #vytvořím rozšířený bod (\vec{x}^*) ... (1,) = tuple s jedním prvkem ... přepíšu poslední prvek na 1

        kontrola = self.skalarni_soucin_matic(self.nadrovina, kontrolovanyBod)
        
        if ((trida == 1) and (kontrola < 0)) or ((trida == -1) and (kontrola >= 0)):
            return bod
        
        return None #bod je správně klasifikován 
            
        ''' v případě, že bych chtěla udělat variantu perceptronového alg., která nejprve všechny špatně klasifikované sečte a poté dle toho upraví nadrovinu
        for i in range (len(self.body)):
            trida = self.body[i][2]
            kontrola = ( (self.nadrovina[0] * self.body[i][0]) + (self.nadrovina[1] * self.body[i][1]) + self.nadrovina[2] )  # {[1,2],[3,4],[5,6]} ... [1][1]

            if ((trida == 1) and (kontrola <= 0)) or ((trida == -1) and (kontrola >= 0)):
                return [self.body[i][0], self.body[i][1], trida]
        
            return None #když to projde a nebude nic špatně klasifikované, tak to vrátí začáteční prázdnoý list
        '''

    def uprava_nadroviny(self, spatneKlasBod): 
        rozsirenyBod = spatneKlasBod[:-1] + (1,) #vytvořím rozšířený bod (\vec{x}^*) -- ponechám stejná čísla jen na konec je přidána 1 
        trida = spatneKlasBod[-1]

        korekce = self.nasobeni_matic_cislem(rozsirenyBod, (trida * self.parametrUceni)) #bod * třída (delta) * parametr učení (ró)
        self.nadrovina = self.soucet_matic(self.nadrovina, korekce) #korekce nadroviny

        self.krok += 1
        
    def parametr_uceni_zmena(self):
        if (self.cyklus == 0):
            return 1
        return 1 /  np.sqrt(self.cyklus) #vezmu druhou odmocinu čísla cyklu - zjemní to velikost úpravy nadroviny. ve velkých cyklech bude oprava malá, ale ne zas úplně tak nepatrná
        #return 1 /  self.cyklus

    def spusteni_percep_alg(self): #upravuji nadrovinu rovnou dle 1 špatně klsaifikovaného bodu
        pocetSpravneKlasifikovanych = 0
        pocetSpatneKlasifikovanych = float("inf") #nastavení na začátku na nekonečno

        while (pocetSpatneKlasifikovanych > 0 and self.cyklus < 2000000): ##všechny body klasifikovány dobře nebo time-out na počet kroků          
            self.cyklus += 1  #po průchodu všemi body se zvýší cyklus
            self.parametrUceni = self.parametr_uceni_zmena()
            pocetSpatneKlasifikovanych = 0 #sledování, kolik bylo špatně klsaifikovaných bodů v každém cyklu

            for bod in self.body: #procházení všech bodů z trénovací množiny ... projetí všech = 1 cyklus
                spatneKlasBod = self.kontrola_bodu(bod)

                if (spatneKlasBod is not None): #je klasifikován špatně
                    #upravím rovinu na základě špatně klasifikovaného bodu
                    self.uprava_nadroviny(spatneKlasBod) #rovnou to přepíše self.nadrovina v cele classe
                    #print("Cyklus: ", self.cyklus, " ro: ", self.parametrUceni, " ", spatneKlasBod, " -> ", self.nadrovina) ... kontrola
                    pocetSpatneKlasifikovanych += 1

                else:
                    pocetSpravneKlasifikovanych += 1
            
            self.celkemSpatneKlas += pocetSpatneKlasifikovanych

            if ((self.cyklus) == 2000000): #to znamená, že další krok už neproběhně, protože ho podmínka zastaví
                print("TIME-OUT na počet cyklů - nejspíš lineárně neseparovatelný případ")

        return self.nadrovina, self.cyklus, self.krok, self.celkemSpatneKlas, self.parametrUceni, pocetSpatneKlasifikovanych
    #------------------------------------------------#


    #------------ PŘIHRÁDKOVÝ ALGORITMUS ------------#
    def spusteni_prihrad_alg(self):
        pocet_spatneKlas = float("inf") #nastavení na začátku na nekonečno

        self.nejlepsiNadrovina = self.nadrovina

        while (pocet_spatneKlas > 0 and self.cyklus < 20): #jakmile všechny body klasifikovány dobře (pocet_spatneKlas == 0) a abych nejela do nekonečna, zastavím a vypíšu nejlepší možné řešení (self.cyklus == 10000) -- konec
            soucet_korekci = [0] * len(self.nadrovina) #pokud rovina např. [1,1,1] -> len = 3 -> soucet_korekci = [0,0,0 ]         
            pocet_spatneKlas = 0 #pro tento cyklus - pokaždé vynuluji
            
            self.cyklus += 1
            #self.parametrUceni = self.parametr_uceni_zmena()

            #místo úpravy nadroviny se hodnoty ukládají do pomocné proměnné - až po průchodu celé množiny se upraví nadrovina (princip dávkového učení perceptronu - až po průchodu celé množiny upravuji nadrovinu)
            for bod in self.body:
                spatneKlasBod = self.kontrola_bodu(bod)

                if (spatneKlasBod is not None):  
                    rozsirenyBod = spatneKlasBod[:-1] + (1,) #místo posledního čísla dám 1 ... takže např.: [1,2,1]
                    nu = spatneKlasBod[-1] * (-1) #pokud třída 1 ... pak nu = -1 ... pokud třída -1 ... pak nu = 1

                    print("Nadrovina: ", self.nadrovina, "SPatne ", spatneKlasBod)

                    korekce = self.nasobeni_matic_cislem(rozsirenyBod, nu*self.parametrUceni*(-1)) #vektor bodu * chyba
                    soucet_korekci = self.soucet_matic(soucet_korekci, korekce) 
                    
                    pocet_spatneKlas += 1

            if (self.cyklus == 1):
                self.nejmensiPocetSpatneKlas = pocet_spatneKlas

            if pocet_spatneKlas < self.nejmensiPocetSpatneKlas:
                self.nejmensiPocetSpatneKlas = pocet_spatneKlas
                self.nejlepsiNadrovina = self.nadrovina.copy()

            #po průchodu celé množiny upravím nadrovinu ... a nejprve změním nejlepší nadrovinu, protože jsem počet špatně klasifikovaných kontrolovala pro tu předchozí nadrovinu 
            self.nadrovina = self.soucet_matic(self.nadrovina, soucet_korekci)
            print("Po zmene: ", self.nadrovina)
            self.krok += 1

            self.celkemSpatneKlas += pocet_spatneKlas

        return self.nejlepsiNadrovina, self.cyklus, self.krok, self.celkemSpatneKlas, self.parametrUceni, self.nejmensiPocetSpatneKlas
    #------------------------------------------------#
#-------------------------------------------------------------------------------------------#






#------------------------------------------ PROGRAM ----------------------------------------#
# GENEROVÁNÍ DAT
''' - pokud chceme vytvořit nová náhodná data 
for i in range(5): #možné změnit počet vytvořených bodů ze třídy Kapr
    kapr = str(Kapr())

    with open("ucici.txt", "a") as file: #a = append ... dam tam cislo a nový řádek
        file.writelines(kapr + "\n")    


for i in range(5):
    stika = str(Stika()) #možné změnit počet vytvořených bodů ze třídy Štika
    
    with open("ucici.txt", "a") as file:
        file.writelines(stika + "\n")  
#'''
# KONEC GENEROVÁNÍ DAT

souradniceX, souradniceY, trida = NacteniBodu()

#---- POČÁTEČNÍ INICIALIZACE ----#
pocatecniBody = list(zip(souradniceX, souradniceY, trida)) #[(1,2,1),(1,2,-1),(1,3,1),...] ... tuple
pocatecniBodyKVykresleni = list(zip(souradniceX, souradniceY))

pocetBodu = len(pocatecniBody)

#nadrovina = [1,1,1]
#parametrUceni = 1

#pro přihrádkový algoritmus
nejlepsiNadrovina = []
nejmensiPocetSpatneKlas = []
#--------------------------------#


#spuštění trénování
while(True):
    rozhodnuti = input("Chcete spustit postupný perceptronový algoritmus (1) nebo přihrádkový algoritmus (2)?: ")

    if (rozhodnuti == "1"):
        x = input('Zadejte počáteční nadrovinu (ve tvaru např.: "1,1,1"): ')
        nadrovina = list(map(float, x.split(",")))

        y = input ('Zadejte počáteční parametr učení (ve tvaru např.: "1"): ')
        parametrUceni = float(y)

        perceptron = Neuron(nadrovina, parametrUceni, pocatecniBody)
        finalniNadrovina, cyklus, krok, celkemSpatneKlas, finalniParametrUceni, konecSpatneKlas = perceptron.spusteni_percep_alg()      
        break

    elif (rozhodnuti == "2"):
        x = input('Zadejte počáteční nadrovinu (ve tvaru např.: "1,1,1"): ')
        nadrovina = list(map(float, x.split(",")))

        y = input ('Zadejte počáteční parametr učení (ve tvaru např.: "1"): ')
        parametrUceni = float(y)

        perceptron = Neuron(nadrovina, parametrUceni, pocatecniBody)
        finalniNadrovina, cyklus, krok, celkemSpatneKlas, finalniParametrUceni, konecSpatneKlas = perceptron.spusteni_prihrad_alg()
        break

    else:
        print("Neplatná volba, zadejte znovu.")


#vykreslení bodů a finální nadroviny
SpusteniVykresleni()
VykresliNadrovinu(finalniNadrovina, pocatecniBodyKVykresleni)

#výstup
print("-------------------------------------------------------")
print("Finální nadrovina:", [float(x) for x in finalniNadrovina])
print("Počet cyklů (počet projetí všech bodů):", cyklus)
print("Špatně klasifikované body touto nadrovinou:", konecSpatneKlas)

ZapsaniVysledku(finalniNadrovina, cyklus, krok, celkemSpatneKlas, parametrUceni, pocetBodu, finalniParametrUceni, konecSpatneKlas)

plt.show() 
#-------------------------------------------------------------------------------------------#
