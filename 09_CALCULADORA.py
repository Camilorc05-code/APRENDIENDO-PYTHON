print ("Calculadora con una sola variable")

print ("********************")
print ("* Menú de opciones *")
print ("********************")

print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicación")
print ("4. División")
print ("5. División entera")
print ("6. Exponente")
print ("7. Modulo o resto \n")

numero = int(input("Introduce la opción deseada: "))

if numero == 1 :
        print ("Elegiste suma \n")

        numero = int(input("Introduce el primer número: "))
        numero += int(input("Introduce el segundo número: "))

        print ("El resultado de la suma es: ", numero)

elif numero == 2 :
    print ("Elegiste Resta \n")

    numero = int(input("Introduce el primer número: "))
    numero -= int(input("Introduce el segundo número: "))

    print ("El resultado de la resta es: ", numero)

elif numero == 3 :
    print ("Elegiste Multiplicación \n")

    numero = int(input("Introduce el primer número: "))
    numero *= int(input("Introduce el segundo número: "))

    print ("El resultado de la multiplicación es: ", numero)

elif numero == 4 :
    print ("Elegiste División \n")

    numero = int(input("Introduce el primer número: "))
    numero /= int(input("Introduce el segundo número: "))

    print ("El resultado de la división es: ", numero)

elif numero == 5 :
    print ("Elegiste División entera \n")

    numero = int(input("Introduce el primer número: "))
    numero //= int(input("Introduce el segundo número: "))

    print ("El resultado de la divesión entera es: ", numero)

elif numero == 6 :
    print ("Elegiste Exponente \n")
    
    numero = int(input("Introduce el primer número: "))
    numero **= int(input("Introduce el segundo número: "))

    print ("El resultado de la exponente es: ", numero)

elif numero == 7 :
    print ("Elegiste Modulo o resto \n")

    numero = int(input("Introduce el primer número: "))
    numero %= int(input("Introduce el segundo número: "))

    print ("El resultado del modulo o resto es: ", numero)

else :
    print ("No ingresaste una opción valida")

    
    
    
    
        




