import random

print("Adivina el número")

numero = random.randint(1,100)
#print("numero:",numero)

contador = 0

seguir = True
while seguir:
    solucion = int(input("¿Qué número es?"))

    if numero == solucion:
        print("Has ganado!")
        seguir = False
    elif numero > solucion:
        print("Es mayor")
    elif numero < solucion:
        print("Es menor")
        
    if seguir:
        contador += 1
        if contador == 3:
            print("Paga para seguir jugando")
