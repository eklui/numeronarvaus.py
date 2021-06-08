from random import randint

arvaus = input("Arvaa numero nollan ja sadan väliltä: ")
numero = randint(0, 100)

while int(arvaus) < numero or int(arvaus) > numero:
    if int(arvaus) < numero:
        print("Numero on suurempi ")
        arvaus = input()
    else:
        print("Numero on pienempi")
        arvaus = input()

else:
    print("Voitit pelin")
