#!/usr/bin/python3
import base

print("Let's do some number base conversion.")
print()

cont ="Y" 

while(cont == "Y"):
    from_base = ""
    while(not(from_base.isnumeric())):
        from_base = input("What number base are you converting from? ")

    to_base = ""
    while(not(to_base.isnumeric())):
        to_base = input("What number base are you converting to? ")

    thenumber = ""
    while(not(len(thenumber) > 0)):
        thenumber = input("What is the number to convert? ")

    print("The result is " + base.numconvert(from_base,to_base,thenumber))
    print()
    try:
        cont = input("Do you want to convert another number? ")[0].upper()
    except:
        cont = "N"
    print()
