import sympy as sp 
import math



choice = input("Välj räknesätt x+y*/ eller derivata: ")

if  choice =='derivata':
    x = sp.Symbol('x') #skapar en variavl som man kallar x
    nytt_uttryck = input("Ange ett uttryck som vi ska derivera ")

    uttryck_1 = sp.sympify(nytt_uttryck) #detta gör om texten till ett sympy uttryck
    derivator = sp.diff(uttryck_1, x) #driverar uttrycket man skriver i input


    print(f"derivatan av denna uttryck blir: {derivator}")



