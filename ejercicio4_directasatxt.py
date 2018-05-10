#!/usr/bin/python


import random
import sys
import os

personaje = {}


def TheEnd ():
	print(personaje["nombre"],"encontró la Directasa.")
	print("Se reunen Pazos, Caliebre y Enoc alrededor del hallazgo.")
	print("Lo miran y le pegan una patada. Se la suda muy fuerte.")
	print("DEBERÁS CONVENCER A ESTOS TRES PARA QUE SIGAN CON LA DIRECTASA EN...")
	print("THE QUEST FOR DIRECTASA, LA NOVELA VISUAL")
	print("Liga con Pazos, Caliebre y Enoc <3")

	
def Molyneux ():
	vida = 50
	fuerza = 20
	
	ganar = False
	
	print("Hola! Soy Moli... Muli... Mo... El tito Peter!")
	print("Me vas a permitir matarte...")
	print("¡Tiene",vida,"puntos de vida!")
	while vida > 0:
		print("")
		accion = input("atacar o escapar: ")
		if accion == "atacar":
			vida = vida - personaje["fuerza"]
			if vida <= 0:
				print("Ganaste!!!!")
				print("Tu premio es 2 monedas")
				personaje["dinero"] += 2
				
				return True
			else:
				print("A Peter le quedan",vida,"puntos de vida")
				print("La Peter ataca!!!!")
				if personaje["dinero"] <= 0:
					personaje["vida"] -= fuerza
					if personaje["vida"] <= 0:
						print("GAME OVER")
						sys.exit()
				else:
					personaje["dinero"] -= fuerza
			printEstado()
		else:
			print("Escapaste")
			return False
			
	return false


def FINALBOSS ():
	if Molyneux():
		TheEnd()




def printEstado ():
	print("Vida:",personaje["vida"],"Dinero:",personaje["dinero"],"Fuerza:",personaje["fuerza"])



def lootbox (vida, fuerza):
	print("¡Una Lootbox salvaje apareció!")
	print("¡Tiene",vida,"puntos de vida!")
	while vida > 0:
		print("")
		accion = input("atacar o escapar: ")
		if accion == "atacar":
			vida = vida - personaje["fuerza"]
			if vida <= 0:
				print("Ganaste!!!!")
				print("Tu premio es 2 monedas")
				personaje["dinero"] += 2
			else:
				print("A la Lootboox le quedan",vida,"puntos de vida")
				print("La Lootbox ataca!!!!")
				if personaje["dinero"] <= 0:
					personaje["vida"] -= fuerza
					if personaje["vida"] <= 0:
						print("GAME OVER")
						sys.exit()
				else:
					personaje["dinero"] -= fuerza
					
					
				
			printEstado()
		else:
			print("Escapaste")
			return




def creaLootbox ():
	loot = random.randint(1,5)
	if loot % 2 == 0:
		loot_vida = random.randint(1,20)
		loot_fuerza = random.randint(1,4)
		lootbox(loot_vida,loot_fuerza)



cofre4 = True
def room4 ():
	print("ROOM 4")
	creaLootbox()
	
	if cofre4:
		print("¡Hay un cofre! también hay una puerta que pone")
		print("Molineux te espera en en norte")
		opcion = input("¿abrir cofre, ir norte o sur? ")
	else:
		print("Molineux te espera en en norte")
		opcion = input("¿ir norte o sur? ")
		
	if opcion == "abrir" and cofre4:
		monedas = random.randint(2,6)
		print("Abres el cofre y consigues...",monedas,"monedas!")
		personaje["dinero"] += monedas
		cofre4 = False
		opcion = input("¿norte o sur? ")
		if opcion == "norte":
			FINALBOSS()
		else:
			room2()
	elif opcion == "norte":
		FINALBOSS()
	else:
		room2()

			



def room3 ():
	print("ROOM 3")
	print("Esta habitación está vacía")
	direc = input("¿oeste? ")
	if direc == "oeste":
		room1()


		
def room2 ():
	print("ROOM 2")
	creaLootbox()
	direc = input("¿Este o norte? ")
	if direc == "norte":
		room4()
	elif direc == "este":
		room1()
	
	

def room1 ():
	#ESTE OESTE
	print("En la habitación no hay nada, pero hay dos puertas:")
	print("Una en el oeste y la otra al este")
	direc = input("¿oeste, este o sur?")
	if direc == "oeste":
		room2()
	elif direc == "este":
		room3()
	else:
		entrada()
	

def entrada ():
	print("Has entrado")
	print("Hay una puerta al norte")
	print("Al sur vuelves a la salida")
	
	
	
	direc = input("¿norte o sur?")
	if direc == "norte":
		room1()
	else:
		print("COBARDE GALLINA CAPITÁN DE LAS SARDINAS")



#os.system('cls')
print("The Quest for Directasa, The Videojocco")
print("=======================================")
print("")
print("LA DIRECTASA LA ROBÓ UN MONO MAGO.")
print("La ha escondido en el fondo de una mazmorra.")
print("¿Quién quieres ser?")
opcion = input("pazos, caliebre o enoc: ")

if opcion == "pazos":
	personaje["nombre"] = "Pazos64"
	personaje["vida"] = 5
	personaje["dinero"] = 10
	personaje["fuerza"] = 10
elif opcion == "caliebre":
	personaje["nombre"] = "Caliebre"
	personaje["vida"] = 5
	personaje["dinero"] = 15
	personaje["fuerza"] = 5
elif opcion == "enoc":
	personaje["nombre"] = "Enoc"
	personaje["vida"] = 5
	personaje["dinero"] = 5
	personaje["fuerza"] = 15

print("¿Quieres entrar en la mazmorra",personaje["nombre"],"?")

respuesta = input("(si/no) ")

if respuesta == "si":
	entrada()
else:
	print("COBARDE GALLINA CAPITÁN DE LAS SARDINAS")


#personaje = {"nombre":"Pazos", "vidas":5, "fuerza":10, "dinero":10}

#print(personaje["vidas"])
