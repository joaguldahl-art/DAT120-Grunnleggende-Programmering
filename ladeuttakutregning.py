# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 10:10:21 2025

@author: joagu
"""

# lading på 1-fas eller 3-fas?

import math

verdi10 = int(input("For å regne ut effekt og energi ved lading, velg 1-fas eller 3-fas strømuttak. Skriv 1 for 1-fas eller 3 for 3fas: "))
if verdi10 == 1:
    spenning = 230 #spenning i volt (V)

    verdi3 = input ("Skriv inn størrelse på sikring (I) oppgitt i ampere: ")
    strom = (float(verdi3))    #strøm i ampere (A)

    effekt = spenning*strom
    print (f"Effekt er {effekt:.0f} watt")
    
    # energi utregning

    verdi5 = input ("Skriv inn antall tid (t) oppgitt i timer: ")
    tid = (float(verdi5))    #tid i timer (t)

    energi = effekt*tid/1000
    print (f"Energi er {energi:.1f} kilowatt-timer (kWh)")
    
    verdi11 = input("Onsker du å vite hvor mange joule dette er?: ")
    if verdi11 == "ja":
        joule = energi*3.6
        print (f"Dette blir {joule} kiloJoule (kJ)")
    elif verdi11 == "nei":
        print ("Håper du fikk svaret du trengte!")    
    
    
elif verdi10 == 3:
    spenning = 230*math.sqrt(3)

    verdi3 = input ("Skriv inn størrelse på sikring (I) oppgitt i ampere: ")
    strom = (float(verdi3))    #strøm i ampere (A)

    effekt = spenning*strom
    print (f"Effekt er {effekt:.0f} watt")
        
    # energi utregning
    
    verdi5 = input ("Skriv inn antall tid (t) oppgitt i timer: ")
    tid = (float(verdi5))    #tid i timer (t)
    
    energi = effekt*tid/1000
    print (f"Energi er {energi:.1f} kilowatt-timer (kWh)")