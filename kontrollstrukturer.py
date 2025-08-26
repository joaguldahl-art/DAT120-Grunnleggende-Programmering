# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 08:42:24 2025

@author: joagu
"""
# bokstav karakter

prosent_str = input("Skriv inn prosentscore:")
prosent_int = int(prosent_str)

if prosent_int >= 90:
    print("A")
elif prosent_int >= 80:
    print("B")
elif prosent_int >= 60:
    print("C")
elif prosent_int >= 50:
    print ("D)")
elif prosent_int >= 40:
    print("E")
else:
    print ("F")
