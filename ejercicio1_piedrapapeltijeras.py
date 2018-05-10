import random

print("¡Piedra, papel o tijeras!")

contador = 3
while contador > 0: 
    opcion = input("Introduce tu opcion: ")

    print("Tu opción es:",opcion)

    oponente = random.randint(1,3)

    if oponente == 1:
        opcion_oponente = "piedra"
    elif oponente == 2:
        opcion_oponente = "tijeras"
    else:
        opcion_oponente = "papel"
        
    print(opcion,opcion_oponente)


    if opcion == opcion_oponente:
        print("Has empatado!")
    elif opcion == "piedra":
        if opcion_oponente == "tijeras":
            print("Has ganado!")        
        elif opcion_oponente == "papel":
            print("Has perdido!")   
    elif opcion == "tijeras":
        if opcion_oponente == "papel":
            print("Has ganado!")
        elif opcion_oponente == "piedra":
            print("Has perdido!")
    elif opcion == "papel":
        if opcion_oponente == "piedra":
            print("Has ganado!")
        elif opcion_oponente == "tijeras":
            print("Has perdido!")


    #contador = contador - 1
    contador -= 1
    
    
    print("Quedan",contador,"intentos")
    
print("Fin del juego")

        








