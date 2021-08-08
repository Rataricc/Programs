from random import randrange
import time
#---------------------------------------------------------------Presentacion y Menu Principal--------------------------------------------------------------------------------
print("")
print("                                            *********************************************************")
print("                                            *Bienvenidos  Ok  donde puedes encontrar 3 programas    *")
print("                                            *       De utilidad para salvar nuestro planeta.        *")
print("                                            *         O bien para hacer tus porpios calculos        *")
print("                                            *********************************************************")
print("")

time.sleep(2)

print("¡IMPORTANTE!: SI USTED ESTA AQUI ES POR QUE ANTERIORMENTE RECIBIO EN EMAIL CON UNA CONTRASEÑA\nYA ESTABLECIDA POR NOSTROS.")

time.sleep(4)

print("")

print("A continuacion le pediremos que ingrese algunos datos asi quedan en nuestros registros.")

time.sleep(1.5)

print("")

nombre = input("Ingrese por favor su nombre: ")

print("")

apellido = input("Ingrese su apellido: ")

print("")

while True:
	try: 
		edad = int(input("Digite su edad por favor: "))
		print("")
		break
	except ValueError: 
		print("")
		print("Debe Ingresar solo numeros, intente nuevamente")
		print("")

print("")


print("Hola", nombre, apellido, "su edad es de", edad, "años. Bienvenido,\nacontinuacion le pediremos que ingrese la contraseña ya establecida.")

time.sleep(1.5)

print("")

print("Consta de 4 intentos para escribir la contraseña correctamente.\nSI sobrepasa la cantidad de intentos su cuenta sera bloqueada." + 
	"Y tendra que comunicarse nuevamente con nostros. Gobierno de la Ciudad.com;")

time.sleep(1.5)

print("")

#          Aca ya empieza el ingreso de la contraseña ya establecida y validada. 

CONTRA = "362436" # variable constante. NO tocar. contraseña establecida. por si me olvido. 

intentos = 0  # contador.

while intentos < 5:  # Bucle while de repeticion. controla la cantidad de intentos que puede hacer el usuario... en este caso 4 intentos. 
	pin = input("Ingrese por favor la contraseña: ")                                                             # despues del 5to intento sale cuenta bloqueda.
	if pin == CONTRA: 
		print("")
		print(nombre,"su contraseña es correcta, puede ingresar")
		print("")
		print("Aguarde unos segundos por favor.")
		time.sleep(4)
		print("")
		menu = None   # variable Menu.
		while menu is None: 
			menu = input("¿Desea ver el menu?.\nEscriba (si); si desea ver el menu.\nDe caso contrario escriba (no) y el programa finaliza.\n" +
				"Ingrese la opcion correspondinete de acuerdo a lo que usted desea: ")
			print("")
			if menu.lower() == "si": 
				for i in ["Menu: ", "1 - Campaña de recoleccion de colillas de cigarrillos.", "2 - Programa de Trancito para saber cuantos vehiculos- ",
				"tiraron basura en la via publica y quienes son los que van a tener multas.", "3 - Calculadora interactiva.", "4 - Juego de Multiplicaciones."]: # Recorre los elementos de la lsita.
                                                                                                                             # Mostrandolo por pantalla a medida; 
                                                                                                                             # que corre el programa.
					time.sleep(0.5)
					print(i)
				time.sleep(0.5)
				print("")
				while True: 
					try: 
						Ingresarrr = int(input("Ingrese el numero correpondiente para que realice el programa que desea: ")) # Variable Ingresarrr puesta asi aproposito. 
						break                                                                                                # No olvidarme de no corregir.
					except ValueError:
						print("") 
						print("Dato invalido, solo deben ser numeros, por favor intentelo nuevamente")
						print("")
#----------------------------------------------------------------------------Programa Recoleccion de colillas----------------------------------------------------------------
				if Ingresarrr == 1:
					print("")
					print("                       **********************************************************")
					print("                       *     Campaña de recoleccion de colillas de cigarrillos  *")
					print("                       *VAMOS A SEGUIR ADELANTE QUE PODEMOS SALVAR NUESTRO MUNDO*")
					print("                       **********************************************************")
					print("")
					while True: 
						try: 
							personas = int(input("Ingrese por favor cuantas personas son las que recolectaron colillas: "))  #
							break                                                                                            #
						except ValueError:                                                                                   # No se por que no use un bucle for; 
							print("")                                                                                        # para trabajar con el primer numero que indica-
							print("Dato invalido, por favor que sean numeros unicamente, intentelo de nuevo")                # el usuario.    REVISAR LUEGO....... 
							print("")                                           											 # 	      TEMA A DISCUTIR CONMIGO MISMO. jajaja 
					print("")

					coli = 1     # hace como un acumulador y contador a la ves.
					             #                                                    NO TOCAR. por si me olvido jajaja.
					total = 0    # Para hacer la operacion luego.                                

					print("Tiene que ingresar brevemente cuantas colillas recolecto cada persona")
					print("")
					time.sleep(1)
					print("Deben ingresar sus nombres o su nombre si es usted solo nuevamente.\nEspero unos segundos por favor.")
					time.sleep(3)
					print("")
					print("Para terminar de ingresar los datos por favor apriete (ENTER), despues el cero (0) y nuevamente (ENTER)")
					time.sleep(1)
					print("")
					while coli != 0:  # Distinto a cero (0). 
						nombre = input("Ingrese su nombre: ")
						time.sleep(1.5)
						print("")
						while True:  # No se por que no utilizo funciones para validar. tema a discutir. valido con excepciones. pero solo con numeros.
							try: 
								coli = int(input("Ingrese cuantas colillas de cigarrillo recolecto: "))
								break
							except ValueError:
								print("") 
								print("Dato incorrecto, deben ser numeros, por favor intentelo nuevamente.")
								print("")
						if coli > 0: 
							if coli > 100: 
								print("")
								print(nombre,"junto mas de 100 colillas.")     # 
							elif coli < 100:                                   #
								print("")                                      #
								print(nombre,"junto menos de 100 colillas.")   #         Posible bug... 
							elif coli > 200:                                   #
								print("")                                      #         tendria que revisar luego. 
								print(nombre,"junto mas de 200 colillas.")     #
							elif coli > 200:                                   #
								print("")                                      #
								print(nombre,"junto menos de 200 colillas.")   #
							total = total + coli     # o puede ser: (total += coli). / Operacion.
							print("")
							print(nombre,"usted junto", coli,"colillas de cigarrillos.")
							print("")
						else: 
							print("")
							print("Usted apreto el cero (0), finaliza la suma de las colillas.")
							print("")
							print("La suma total de todas las colillas recolectadas es de: ",total)
							print("")
							print("Fin del Programa, siga/sigan por favor juntando colillas para salvar nuestro planeta.")
					print("")
					menu = None
#--------------------------------------------------------------------------------Programa del Trancito--------------------------------------------------------------------- 
				elif Ingresarrr == 2:
					print("") 
					time.sleep(3)
					print("              ======================================================================================")
					print("              = Programa de Trancito para saber cuantos vehiculos tiraron basura en la via publica =")
					print("              =                   y quienes son los que van a tener multas                         =")
					print("              ======================================================================================")
					print("")
					while True: 
						try: 
							cantidad_vehiculos = int(input("Ingrese por favor la cantidad de vehiculos que se observaron: "))
							break
						except ValueError: 
							print("")
							print("Dato incorrecto.Solo tienen que ser numeros.\nIntentelo nuevamente por favor.")
							print("")
					print("")

					for x in range(cantidad_vehiculos):  # Aca utilizo for despues de varios dias pensando como lo podia utilizar. 
						while True:                      # espero que quede bien. revisar luego. 
							try: 
								vtb = int(input("Ingrese por favor la cantidad de vehiculos que han tirado basura: ")) # vtb = Cantidad de Vehiculos que han tirado basura.
								break
							except ValueError:
								print("") 
								print("Dato invalido, deben ser numeros solamente.\nPor favor intentelo nuevamente.")
								print("")
						cantidad_vehiculos = cantidad_vehiculos - vtb # o puede ser = (cantidad_vehiculos -= vtb).
						if vtb == "": 
							print("")
							print("1 - Los vehiculos que tiraron basura en la via publica son:", vtb)
							print("")
						else: 
							print("")
							print("0 - Los vehiculos que NO tiraron basura son:", cantidad_vehiculos)
							print("")
							print('Apriete "SI" si desea ver el numero de autos que han sido multados.\nEn caso contrario apriete "NO"',
								'o culquier otra tecla')
							print("")
							y = input("¿Quiere saber cuentas vehiculos han sido multados por tirar basura en la via publica?: ")
							if y.lower() == "si": 
								print("")
								print("Los vehiculos multados son:", vtb)
								print("")
							print("")
							print("El/Los vehiculo/s sin multas son/es:", cantidad_vehiculos)
							print("") 
							print("Fin del programa. Hasta pronto")
							break # Para cortar el bucle y no siga preguntando. 
					print("")
					menu = None
#--------------------------------------------------------------------Programa calculadora Interactiva---------------------------------------------------------------------
				elif Ingresarrr == 3: 
					print("")
					print("                                 ******************************************")
					print("                                 *BIENVENIDOS A LA CALCULADORA INTERACTIVA*")
					print("                                 ******************************************")
					print("")
					menuuu = None # Puse menuuu aproposito para evitar tener un margen de error con el primer menu ya antes definido.
					while menuuu is None: 
						print("") 
						time.sleep(3)                                                                                            
						menuuu = input("¿Desea ver el Menu de la calculadora?.\nEscriba (si) si es que desea ver el menu.\n"
							"Escriba (no) si desea que el programa finalice.\nIngrese la opcion correspodiente de acuerdo a lo que usted desea: ")
						time.sleep(0.5)
						print("") 
						if menuuu.lower() == "si":                                                                                                   
							for b in ["Menu: ", "1 - Sumar.", "2 - Restar.", "3 - Multiplicar.", "4 - Dividir.", "5 - Modulo.",                     
							"6 - Potenciar.", "7 - Salir."]:  # Lo mismo que el anterir menu, bucle for para recorrer la lista.                    


								time.sleep(0.5) # con un margen de 0.5 segundos, uno abajo del otro se va ir mostrando.  
								print(b)        # Imprimo por pantalla la lista. 
							time.sleep(0.5)     # lo mismo aca. 
							print("")
							while True: 
								try: 
									elegir = int(input("Ingrese el numero correpondiente para hacer la operacion que desee hacer: "))
									break
								except ValueError: 
									print("")
									print("\nOpcion incorrecta.\nIntetelo nuevamente.")
									print("")
#**************************************************************************Bloque de Suma********************************************************************************
							if elegir == 1: 
								while True:                                                                                    #
									try:                      																   #
										print("")                                                                              # Valido con las excepciones.
										num1 = float(input("Ingrese el primer numero: "))                                      # creo las variables num1 y num2.
										print("")                                                                              # para despues alojarlas en una variables-
										time.sleep(0.5)                                                                        # resul / resultado en criollo.
										num2 = float(input("Ingrese el segundo numero: "))                                     # no tenia ganas de escribir la palabra - 
										print("")                                                                              # completa. 
										break                                                                                  # paja.
									except ValueError:                                                                         #
										print("")                                                                              #
										print("Debe Ingresar solo numeros, intente nuevamente")                                #
										print("")                                                                              #
								resul = num1 + num2                                                                            #
								print("")                                                                                      # Imprimo el resultado mas adelante.
								print("El resltado de la suma es", resul)                                                      # 
								print("")
								c = input("¿Desea seguir sumando?.\nEscriba (si) si desea seguir sumando\nEn caso contrario" +     #
									"escriba (no)\n")                                                                              #
								print("")                                                                                          # Puse como variable "c" para no tener -
								while c.lower() == "si":                                                                           # margen de error. 
									while True:                                                                                    # 
										try:                   
											print("")                                                                              # error despues, por que ya use otras - 
											num1 = float(input("Ingrese el primer numero: "))                                      # letras. 
											print("")                                                                              # podria haber usado las mismas letras - 
											time.sleep(0.5)                                                                        # ahora que me pongo pensar bien. 
											num2 = float(input("Ingrese el segundo numero: "))                                     # bueno. por lo menos funciona.
											print("")                                                                              #
											break                                                                                  # Para inicializar.
										except ValueError:                                                                         #
											print("")                                                                              # Aca repeti codigo cosa que se que es
											print("Debe ingresar solo numeros, intentelo de nuevamente")                           # una mala practica.
											print("")                                                                              # 
									resul = num1 + num2                                                                            # Hubiera creado antes una variable - 
									print("")                                                                                      # repetir. 
									print("El resultado de la suma es", resul)                                                     #
									print("")                                                                                      #  Pero el codigo funciona bien - 
									c = input("¿Desea seguir sumando?.\nEscriba (si) si desea seguir sumando\nEn caso contrario" + # asi que no lo toco. 
										"escriba (no)\n")
									print("")
								else: 
									c.lower() == "no"
									print("")
									print("ha elegido la opcion (no), vuelve al menu de la calculadora.")
									print("")
									menuuu = None
									                #--------------A partir de aca para abajo es toda la misma resolucion y sintaxis, no cambia nada.-----------
									                
#******************************************************************************Bloque de Resta******************************************************************************
							elif elegir == 2:
								while True: 
									try: 
										print("")
										num1 = float(input("Ingrese el primer numero: "))
										print("")
										time.sleep(0.5)
										num2 = float(input("Ingrese el segundo numero: "))
										print("")
										break
									except ValueError: 
										print("")
										print("Debe ingresar solo numeros, intentelo de nuevamente.")
										print("")
								resul = num1 - num2
								print("")
								print("El resultado de la resta es", resul)
								print("")
								c = input("¿Desea seguir Restando?.\nEscriba (si) si desea seguir restando\nEn caso contrario" + 
									"escriba (no)\n") 
								print("")
								while c.lower() == "si":
									while True: 
										try: 
											print("")
											num1 = float(input("Ingrese el primer numero: ")) 
											print("")
											time.sleep(0.5)
											num2 = float(input("Ingresa el segundo numero: "))
											print("")
											break 
										except ValueError: 
											print("")
											print("Debe ingresar solo numeros, intentelo de nuevamente.")
											print("")
									resul = num1 - num2 
									print("")
									print("El resultado de la resta es:", resul)
									print("")
									c = input("¿Desea seguir Restando?.\nEscriba (si) si desea seguir restando\nEn caso contrario" + 
										"escriba (no)\n")
									print("")
								else: 
									c.lower() == "no"
									print("")
									print("ha elegido la opcion (no), vuelve al menu de la calculadora.")
									print("")
									menuuu = None
#****************************************************************************Bloque de Multiplicacion*************************************************************************
							elif elegir == 3: 
								while True: 
									try: 
										print("")
										num1 = float(input("Ingrese el primer numero: "))
										print("")
										time.sleep(0.5)
										num2 = float(input("Ingrese el segundo numero: "))
										print("")
										break
									except ValueError: 
										print("")
										print("Debe ingresar solo numeros, intentelo nuevamente.")
										print("")
								resul = num1 * num2
								print("")
								print("El resultado de la multiplicacion es", resul)
								print("")
								c = input("¿Desea seguir Multiplicando?.\nEscriba (si) si desea seguir multiplicando\nEn caso contrario" + 
									"escriba (no)\n")
								print("")
								while c.lower() == "si": 
									while True: 
										try: 
											print("")
											num1 = float(input("Ingrese el primer numero: "))
											print("")
											time.sleep(0.5)
											num2 = float(input("Ingrese el segundo numero: "))
											print("")
											break
										except ValueError: 
											print("")
											print("Debe ingresar solo numeros, intentelo nuevamente.")
											print("")
									resul = num1 * num2
									print("")
									print("El resultado de la multiplicacion es:", resul)
									print("")
									c = input("¿Desea seguir Multiplicando?\nEscriba (si) si desea seguir multiplicando\nEn caso contrario" + 
										"escriba (no)\n")
									print("")
								else: 
									c.lower() == "no"
									print("")
									print("ha elegido la opcion (no), vuelve al menu de la calculadora.")
									print("")
									menuuu = None
#*******************************************************************************Bloque de Division****************************************************************************
							elif elegir == 4: 
								while True: 
									try: 
										print("")
										num1 = float(input("Ingrese el primer numero: "))
										print("")
										time.sleep(0.5)
										num2 = float(input("Ingrese el segundo numero: "))
										print("") 
										break
									except ValueError: 
										print("")
										print("Debe ingresar solo numeros, intentelo nuevamente.")
										print("")
								resul = num1 / num2
								print("")
								print("El resultado de la Division es", resul)
								print("")
								c = input("¿Desea seguir Dividiendo?\nEscriba (si) si desea seguir dividiendo\nEn caso contrario" + 
									"escriba (no)\n")
								print("")
								while c.lower() == "si": 
									while True: 
										try:
											print("")
											num1 = float(input("Ingrese el primer numero: "))
											print("")
											time.sleep(0.5) 
											num2 = float(input("Ingrese el segundo numero: "))
											print("")
											break
										except ValueError: 
											print("")
											print("Debe ingresar solo numeros, intentelo nuevamente.")
											print("")
									resul = num1 / num2
									print("")
									print("El resultado de la division es", resul)
									print("")
									c = input("¿Desea seguir Dividiendo?\nEscriba (si) si desea seguir dividiendo\nEn caso contrario" + 
										"escriba (no)\n")
									print("")
								else: 
									c.lower() == "no"
									print("")
									print("ha elegido la opcion (no), vuelve al menu de la calculadora.")
									print("")
									menuuu = None
#************************************************************************Bloque de Modulo*************************************************************************************
							elif elegir == 5: 
								while True: 
									try: 
										print("")
										num1 = float(input("Ingrese el primer numero: "))
										print("")
										time.sleep(0.5)
										num2 = float(input("Ingrese el segundo numero: "))
										print("")
										break
									except ValueError: 
										print("")
										print("Debe ingresar solo numeros, intentelo nuevamente.")
										print("")
								resul = num1 % num2
								print("")
								print("El resultado del modulo es", resul)
								print("")
								c = input("¿Desea seguir Modulando\nEscriba (si) si desea seguir modulando\nEn caso contrario" + 
									"escriba (no)\n")
								print("")
								while c.lower() == "si":
									while True: 
										try: 
											print("")
											num1 = float(input("Ingrese el primer numero: "))
											print("")
											time.sleep(0.5)
											num2 = float(input("Ingrese el segundo numero: "))
											print("")
											break
										except ValueError: 
											print("")
											print("Debe ingresar solo numeros, intentelo nuevamente.")
											print("")
									resul = num1 % num2 
									print("")
									print("El resultado del modulo es", resul)
									print("")
									c = input("¿Desea seguir Modulando\nEscriba (si) si desea seguir modulando\nEn caso contrario" + 
										"escriba (no)\n")
									print("")
								else: 
									c.lower() == "no"
									print("")
									print("ha elegido la opcion (no), vuelve al menu de la calculadora.")
									print("")
									menuuu = None
#**************************************************************************Bloque de Potencia*********************************************************************************
							elif elegir == 6: 
								while True: 
									try: 
										print("")
										num1 = int(input("Ingrese el primer numero: "))
										print("")
										time.sleep(0.5)
										num2 = int(input("Ingrese el segundo numero: "))
										print("")
										break
									except ValueError: 
										print("")
										print("Debe ingresar solo numeros, intentelo nuevamente.")
										print("")
								resul = num1 ** num2
								print("")
								print("El resultado de la potencia es:", resul)
								print("")
								c = input("¿Desea seguir Potenciando?.\nEscriba (si) si desea seguir potenciando.\nEn caso contrario" + 
									"escriba (no)\n")
								print("")
								while c.lower() == "si": 
									while True: 
										try: 
											print("")
											num1 = int(input("Ingrese el primer numero: "))
											print("")
											time.sleep(0.5)
											num2 = int(input("Ingrese el segundo numero: "))
											print("")
											break
										except ValueError: 
											print("")
											print("Debe ingresar solo numeros, intentelo nuevamente.")
											print("")
									resul = num1 ** num2
									print("")
									print("El resultado de la potencia es:", resul)
									print("")
									c = input("¿Desea seguir Potenciando?.\nEscriba (si) si desea seguir potenciando.\nEn caso contrario" + 
										"escriba (no)\n")
								else: 
									c.lower() == "no"
									print("")
									print("ha elegido la opcion (no), vuelve al menu de la calculadora.")
									print("")
									menuuu = None
							else: 
								elegir == 7 
								print("")
								print("Usted decidio salir de la calculadora.\nVuelve al menu principal.")
								print("")
								menu = None
#***********************************************************************Parte del Menu de la calculadora*********************************************************************
						elif menuuu.lower() == "no": 
							print("")
							print("finalizo el programa.")
							menu = None
							break
						else:
							print("")
							print("La opcion que eligio no es valida.\nIntentelo nuevamente.")
							time.sleep(0.5)
							menuuu = None     # Va al menu de la calculadora nuevamente. y podra elegir como correponda. 
#-------------------------------------------------------------------------Juego de Multiplicaciones-------------------------------------------------
				elif Ingresarrr == 4: 
					repetir = None
					while repetir is None:

						print("")

						print("***************************************")
						print("*Bienvenido al Juego de multiplicacion*")
						print("***************************************")

						print("A continuacion le solicitaremos que ingrese los datos para calcular la multiplicacion")

						print("")

						cantidad_multiplicaciones = int(input("Ingrese por favor el numero de multiplicaciones a realizar: "))

						print("")

						numero_aciertos = 0

						for j in range(0,cantidad_multiplicaciones): 
							multiplicador = randrange(2,10)
							multiplicando = randrange(2,10)

							resultado_multiplicacion = multiplicador * multiplicando

							resultado = int(input("Ingrese por favor el resultado de {} x {}:\n".format(multiplicador,multiplicando)))

							desvio = (abs(resultado_multiplicacion - resultado) / resultado_multiplicacion)

							if desvio == 0: 
								numero_aciertos += 1
							elif desvio <= 10: 
								numero_aciertos += 0.66
							elif desvio > 10 and desvio <= 30: 
								numero_aciertos += 0.33

						nota = (numero_aciertos / cantidad_multiplicaciones) * 100

						print(f"La nota obtenida es: {nota}")

						if nota >= 90:
							print("¡Felicidades!, ha obtenido unos de los puntajes mas altos")

						repetir = input("¿Quiere volver a jugar?: ")

						if repetir.lower() == "si": 
							repetir = None
						else: 
							repetir.lower() == "no" 
							print("")
							print("Salio del juego, vuelve al menu principal.\nGracias por jugar.")
							menu = None 
#------------------------------------------------------------------------Parte del Menu Principal de la App-------------------------------------------------------------------
			elif menu.lower() == "no":
				print("")
				print("Finalizo la Aplicacion.")
				break
			else: 
				print("")
				print("La opcion que eligio no es la correcta.\nIntentelo nuevamente.")
				time.sleep(0.5)
				menu = None
		break
	else: 
		print(nombre,"su contraseña es incorrecta, intentelo nuevamente por favor.")

		intentos = intentos + 1
		print("")
		print("Intentos fallidos",intentos)
		print("")
else: 
	print(nombre,"su cuenta ha sido bloqueada.") 