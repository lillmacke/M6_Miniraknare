# Välj räknesätt:
# 1: Addition
# 2: Subtraktion
# 3: Division
# 4: Multiplikation

# Skriv första talet:
# Skriv andra talet:

#Summan/Differensen/Kvoten/Produkten är: 

import math 
num1 = float(input("Första heltalet: "))
num2 = float(input("Andra heltalet: "))

def addition(x,y):
    return x + y

def subraktion(x,y):
    return x - y

def multiplikation(x,y):
    return x * y

def division(x,y):
    return x / y 

print(num1, "+", num2, "=", addition(num1,num2))

def meny():