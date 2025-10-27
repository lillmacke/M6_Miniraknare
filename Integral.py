import sympy as sp 
import math



choice = input("Välj räknesätt x+y*/ samt derivera eller Integral: ")

if  choice =='Integral':
    x = sp.Symbol('x') #skapar en variabel som man kallar x
    nytt_uttryck = input("Ange ett uttryck som vi ska integrera: ") # En variabel som sparar det man skriver i denna input

    uttryck_1 = sp.sympify(nytt_uttryck) #Denna rad gör om input svaret till ett uttryck som passar sympy biblioteket
    fraga_2 = input("Ska man beräkna en bestämd integral? (ja eller nej):  ") # Denna variabel frågar om man ska ha en bestämd eller öppen integral

    if fraga_2.lower() =='ja': # Denna if sats gör att man väljer två värden på x och och beräknar integralen mellan dem på grafen 
        a = float(input("Bestäm nedre gränsen för x: "))
        b = float(input("Bestäm den övre gränsen för x: "))
        resultat = sp.integrate(uttryck_1, (x,a,b))
        print(f"Integalen av {uttryck_1} från {a} till {b} i grafen är: {resultat} ")
    else: #Detta händer om man svarar nej på fraga_2 variabeln. 
        resultat = sp.integrate(uttryck_1, x)
        print(f"Integralen av {uttryck_1} är: {resultat} + C (konstant) ")









