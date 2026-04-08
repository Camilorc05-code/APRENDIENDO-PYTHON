print ("***************************************************************************")
print ("* Programa para determinar ¿Cuál es el número más grande de tres números? *")
print ("*************************************************************************** \n")

numero_uno = int(input("Introduce el primer número: "))
numero_dos = int(input("Introduce el segundo número: "))
numero_tres = int(input("Introduce el tercer número: "))

if numero_uno > numero_dos and numero_uno > numero_tres :
    print ("El número", numero_uno, "es el más grande de los tres.")

elif numero_dos > numero_uno and numero_dos > numero_tres :
    print ("El número", numero_dos, "es el más grande de los tres.")

elif numero_tres > numero_dos and numero_tres > numero_uno :
    print ("El número", numero_tres, "es el más grande de los tres.")

else :
    print ("Debes ingresar un valor númerico")

print ("Fin.")
