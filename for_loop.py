# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:39:04 2025

@author: joagu
"""
"""
# for - løkke
# for hver verdi i range (6) utfør blokka

for teller in range (6):
    print(teller)
# Skriver ut 0 til og med 5.

print()

# Parametere: start, slutt, steg
for verdi in range (3, 12, 2):
    print(verdi)
# fra og med 3 til men ikke med 12. 

# Teller nedover ved negativ steglengde, fra og med 10, til og med 0.
for verdi in range (10, 0, -1):
    print(verdi)

"""

"""
# brukes når man vet hvor mange ganger løkka skal kjøres.
tall_str = input("Skriv inn et positvt heltall: ")
tall_int = int(tall_str) 
akkumulator = 1
for verdi in range (1, tall_int+1):
    akkumulator = akkumulator * verdi
print(akkumulator)
"""

