print ("Conjunción (and)")

conjuncion = int(input("Escribe un número mayor a 2 y menor a 5: "))

if conjuncion > 2 and conjuncion < 5 :
    print ("El número", conjuncion, "cumple con la condición.")

else :
    print ("El número", conjuncion, "NO cumple con la condición.")

print ("\n Disyunción (or)")

disyuncion = input("Para cumplir con la condición escribe 'si' o 'yes': ")
disyuncion = disyuncion.lower()

if disyuncion == "si" or disyuncion == "yes" :
    print ("La condición 'SI' se ha cumplido.")

else :
    print ("La condición 'NO' se ha cumplido.")

print ("\n Negación (not)")

negacion = int(input("Introduce un número igual a 5: "))

if not negacion == 5 :
    print ("\n El número es diferente a cinco y SI cumple la condición. \n")

else :
    print ("\n El número es igual a cinco y NO cumple la condicón. \n")

print ("Fin.")
