import math 

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y 

print("Välj räknesätt: \n"
        "1. Addera \n"  
        "2. Subtrahera \n"
        "3. Multiplicera \n"
        "4. Dividera \n")

while True: 
    val = input("Välj 1/2/3/4: ")

    if val in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Första talet:" ))
            num2 = float(input("Andra talet: "))
        except ValueError:
            print("Fel input. Välj ett giltigt alternativ.")

        if val == "1":
            print(num1, "+", num2, "=", add(num1,num2))
         
        elif val == "2":
            print(num1, "-", num2, "=", sub(num1,num2))
        
        elif val == "3":
            print(num1, "*", num2, "=",  mult(num1,num2))
        
        elif val == "4":
            print(num1, "/", num2, "=", div(num1,num2))
        
        köra_igen = input("Nästa uträkning? (ja/nej): ")
        if köra_igen == "nej":
            break
    else:
        print("Fel input")
            