# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# oving DAT120 
# oppg h

# Beregning av elektrisk effekt og energi
# 1 - Beregne effekten (P) til elektrisk effekt
# 2 - Beregne energiforbruket (E) over tid

# 1 - Be brukeren skrive inn spenning (V), strøm (A) og tid (t)
# 2 - Beregn effekten og energiforbruket
# 3 - Skriv ut resultatene med forklarende tekst.


verdi1 = input("Skriv inn spenning i volt: ")
spenning = float(verdi1)

verdi2 = input("Skriv inn antall strøm i ampere: ")
strom = float(verdi2)

verdi3 = input("Skriv inn antall timer energiforbruket skal beregnes over: ")
tid = float(verdi3)

effekt = spenning*strom

energiforbruk = effekt*tid/1000

print (f"Effekten er {effekt:.0f} watt.")
print (f"Energiforbruket er {energiforbruk:.1f} kilowatt-timer (kWh).")







