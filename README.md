# Perceptron - klasifikace ryb (Kapr × Štika)

Tento projekt implementuje 2 algoritmy (verze perceptronového algoritmu) - dávkový perceptronový a přihrádkový algoritmus. Program lineárně klasifikuje 2 druhy ryb na základě dvou jejich fyzických vlastností:

- **Hmotnost (kg)**
- **Šířka (cm)**

Cílem algoritmů je najít dělící nadrovinu (přímku v 2D), která oddělí a bude správně klasifikovat kapry a štiky.

---

### Funkcionalita
- Možné generování náhodných trénovacích dat (kapr / štika)
- Načtení dat ze souboru `ucici.txt`
- Trénování perceptronu:
  - Dávkový perceptron
  - Přihrádkový perceptron
- Vykreslení:
  - Trénovacích bodů
  - Výsledné dělící nadroviny
- Uložení výsledků běhu do textového souboru (pojmenována jako `vysledek_{timestamp}.txt`, kde `{timestamp}` je nahrazen přesným datumem, kdy byl soubor vytvořen)

---

### Struktura projektu
```
stanclova_rocnikova_prace/
├── main.py            # program
├── ucici.txt          # trénovací data (hmotnost, šířka, třída)
├── README.md
├── Postupný perceptronový algoritmus
    ├── Jednotlivé textové soubory se zaznamenanými výsledky
    └── Obrázky k výsledkům (stejné názvy s určeným textovým souborem)
└── Přihrádkový algoritmus
    ├── Jednotlivé textové soubory se zaznamenanými výsledky
    └── Obrázky k výsledkům (stejné názvy s určeným textovým souborem)
```

---

### Použitý model
#### Perceptron
Model hledající rozšířený váhový vektor nadroviny:
```
[a, b, c]
```

který by měl správně klasifikovat body po dosazení do rovnice nadroviny:
```
Bod[a,b] 

-> a*x + b*y + c > 0  →  pro třídu 1 (štika)
-> a*x + b*y + c <= 0  →  pro třídu 1 (štika)
```

Více je tento model a jeho varianty modely vysvětlen v mé ročníkové práci "Lineární klasifikátory".

---

### Vstupní data (`ucici.txt`)
Každý řádek má tvar:

```
hmotnost,šířka,třída
```

Příklad:
```
3.25,18.4,-1
1.10,7.3,1
```

---

### Spuštění programu a výstup
0. Před spuštěním programu:
- Změna parametru učení v průběhu učení není v programu řešena interaktivně, ale je nastavována přímo v kódu.
- Uživatel má možnost zvolit různé strategie změny parametru učení úpravou příslušných částí programu.
  - Pokud je cílem mít parametr učení konstantní, stačí v daném algoritmu pouze zakomentovat:
    - `self.parametrUceni = self.parametr_uceni_zmena()`
  - Pakliže uživatel chce nastavit jinou změnu parametru učení, je to možné provést ve funkci?
    - `parametr_uceni_zmena()`, kde jsou připraveny 2 varianty, které lze zakomentovat a odkomentovat (1/cyklus nebo 1/$\sqrt{cyklu}$)
    
1. Spuštění programu:
```bash
python main.py
```

2. Po spuštění:
- Po spuštění je uživatel vyzván k výběru jednoho ze dvou implementovaných algoritmů:
  - 1 - postupný perceptronový algoritmus
  - 2 - přihrádkový perceptronový algoritmus
- Výběr se provádí zadáním odpovídajícího čísla do konzole.

3. Zadání počátečních parametrů
- Počáteční rozšířený váhový vektor (nadrovina) se zadává ve tvaru:
  - `w1,w2,b`, kde w1, w2 jsou váhy příslušné jednotlivým vstupním parametrům a b je bias (posun)
- Parametr učení se zadává jako reálné číslo, například:
  - `1`, `0.5` nebo `0.1`

4. Program:
- Program začíná v momentě, kdy uživatel zadá do konzole parametr učení.

5. Výstup programu:
- Natrénovaný perceptron
- Vypsané informace v konzoli
  - Rozšířený váhový vektor spočtené nadroviny
  - Počet cyklů
  - Špatně klsaifikované body finální nadrovinou
- Vykreslený graf bodů a nadroviny 
- Uložení výsledků do souboru `vysledek_YYYY-MM-DD_HH-MM-SS.txt`

---

### Generování dat
Pro vytvoření nových náhodných dat je možné odkomentovat v hlavní části programu označenou komentářem `# GENEROVÁNÍ DAT` a ukončenou komentářem `# KONEC GENEROVÁNÍ DAT`:
- V této části je možné změnit počet generovaných dat:
  - `for i in range(10):`, kde místo `10` se napíše libovolné kladné nenulové číslo
- Tato část vygeneruje dvakrát daný pčoet dat - jednou pro kapry a dále pro štiky.
---

### Poznámky
- Postupný perceptronový algoritmus neřeší lineárně neseparovatelná data. Po dovršení časového limitu algoritmu skončí a výstupem je poslední upravená nadrovina. Zároveň do konzole se vypíše hláška "TIME-OUT na počet cyklů - nejspíš lineárně neseparovatelný případ".
- Pakliže v grafu není vykreslena nadrovina, ve většině případu to znamená, že její rovnice je mimo graf. Nadrovina existuje, ale je naprosto mimo vykreslené body.

---

### Autor
*Štanclová Tereza*


