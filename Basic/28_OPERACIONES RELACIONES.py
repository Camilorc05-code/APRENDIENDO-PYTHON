print ("Introduce dos números a comparar: \n")

numero_uno = int(input("Introduce el primer número: "))

numero_dos = int(input("Introduce el segundo número: "))

print ("\n Los números a comparar son: ", numero_uno , "y", numero_dos, " \n")


if numero_uno < numero_dos :
    print ("Es menor...")

if numero_uno > numero_dos :
    print ("Es mayor...")

if numero_uno == numero_dos :
    print ("Es igual...")

if numero_uno != numero_dos :
    print ("Es diferente...")

if numero_uno <= numero_dos :
    print ("Es menor o igual...")

if numero_uno >= numero_dos :
    print ("Es mayor o igual...")

print ("Fin.")
