# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:18:56 2025

@author: joagu
"""
"""
# testing av while løkke

#tekst = input("Skriv inn ei linje. Avslutt med tom linje: ")
#resultat = ""
#while tekst != "":
   # resultat = resultat + tekst
 #  resultat += tekst +"\n"
 # tekst = input("Skriv inn ei linje. Avslutt med tom linje: ")
#print(resultat) 
    
"""

# ønsker å lese inn et positivt heltall.
# la brukeren prøve på nytt hvis tallet er negatict
"""
program = 1
while program == 1:
    tall_str = input("Skriv inn et positvt heltall: ")
    tall_int = int(tall_str) 
    if tall_int > 0:
        print(tall_int," er et heltall!")
        program = 0
        
    else:
        print("Prøv p") 
        """
    
tall_str = input("Skriv inn et positvt heltall: ")
tall_int = int(tall_str) 
while tall_int < 0:
    print("Tallet kan ikke være negativt. Prøv på nytt.")
    tall_str = input("skriv inn et positivt heltall")
    tall_int = int(tall_str)
print(f"Tallet ble: {tall_int}")
