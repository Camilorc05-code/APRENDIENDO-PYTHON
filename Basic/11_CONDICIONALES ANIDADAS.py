print ("=========")
print ("Conversor")
print ("========= \n")

print ("Menú de opciones \n")

print ("Presiona 1 para convertir de número a palabra.")

print ("Presiona 2 para convertir de palabra a número. \n")


menu = int(input("¿Cúal es tu opción deseada?: "))


if menu == 1 :
    print ("\n Conversor de número a palabra \n")
    menu_uno = int(input("¿Cual es el número que deseas convertir a palabra?: "))
                   
    if menu_uno == 1 :
                   print ("El número es 'UNO'")
                   
    elif menu_uno == 2 :
         print ("El número es 'DOS'")

    elif menu_uno == 3 :
         print ("El número es 'TRES'")

    elif menu_uno == 4 :
         print ("El número es 'CUATRO'")

    elif menu_uno == 5 :
         print ("El número es 'CINCO'")

    elif menu_uno == 6 :
         print ("El número es 'SEIS'")

    elif menu_uno == 7 :
         print ("El número es 'SIETE'")

    elif menu_uno == 8 :
         print ("El número es 'OCHO'")

    elif menu_uno == 9 :
         print ("El número es 'NUEVE'")

    else :
        print ("Este programa solo convierte hasta el número '9'")

elif menu == 2 :
    print ("Conversor de palabra a número")

    menu_dos = (input("¿Cual es el palabra que desea convertir a número?: "))
    menu_dos = menu_dos.lower()

    if menu_dos == "uno" :

        print ("El número es '1'")

    elif menu_dos == "dos" :
        print ("El número es '2'")

    elif menu_dos == "tres" :
        print ("El número es '3'")

    elif menu_dos == "cuatro" :
        print ("El número es '4'")

    elif menu_dos == "cinco" :
        print ("El número es '5'")

    elif menu_dos == "seis" :
        print ("El número es '6'")

    elif menu_dos == "siete" :
        print ("El número es '7'")
    elif menu_dos == "ocho" :
        print ("El número es '8'")

    elif menu_dos == "nueve" :
        print ("El número es '9'")

    else:
        print ("Este programa solo convierte hasta el número 'nueve'")
else:
    print("Opción no disponible.")


print ("Fin.")

        

    

     

    


        
        
                   



                 
