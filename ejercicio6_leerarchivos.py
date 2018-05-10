archivo = open("ejercicio6_ejemplo.txt")

contenido = archivo.readlines()

largo = len(contenido)
contador = 0
while contador < largo:
	elemento = contenido[contador].split()

	if elemento[0] == "nave":
		print("Cargando gráfico nave:", elemento[1])
	elif elemento[0] == "marcianito1":
		print("Cargando gráfico m1:", elemento[1])
	elif elemento[0] == "marcianito2":
		print("Cargando gráfico m2:", elemento[1])
	elif elemento[0] == "marcianito3":
		print("Cargando gráfico m3:", elemento[1])
	elif elemento[0] == "nodriza":
		print("Cargando gráfico nave nodriza:", elemento[1])

		



	contador = contador + 1


