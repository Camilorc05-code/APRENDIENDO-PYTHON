print ("***************************************")
print ("* Sistema de control vacacional Rappi *")
print ("***************************************")

print ("Menú de opciones \n")

print ("Clave 1 para entrar al departamento de 'ATENCIÓN AL CLIENTE'.")

print ("Clave 2 para entrar al departamento de 'LOGISTICA'.")

print ("Clave 3 para entrar al departamento de 'GERENCIA'. \n")

clave = int(input("\n Ingrese la clave del departamento: "))

nombre = input("Ingrese el nombre del trabajador: ")

if clave == 1 :
    print ("Bienvenido al departamento de 'ATENCIÓN AL CLIENTE' \n")
    
    años = int(input("\n Ingrese los años que lleva en la empresa: "))

    if años == 1 :
        print ("Con 1 año de servicio, el trabajador", nombre, "recibe '6' dias de vacaciones.")

    elif años >= 2 and años <= 6 :
        print ("De 2 a 6 año de servicio, el trabajador", nombre, "recibe '14' dias de vacaciones.")

    elif años >= 7 :
        print ("A partir de 7 años de servicio, el trabajador", nombre, "recibe '20' dias de vacaciones.")

    else :
       print ("No ingreso un valor númerico.")

elif clave == 2 :
    print ("Bienvenido al departamento de 'LOGISTICA' \n")
    
    años = int(input("\n Ingrese los años que lleva en la empresa: "))

    if años == 1 :
        print ("Con 1 año de servicio, el trabajador", nombre, "recibe '7' dias de vacaciones.")

    elif años >= 2 and años <= 6 :
        print ("De 2 a 6 año de servicio, el trabajador", nombre, "recibe '15' dias de vacaciones.")

    elif años >= 7 :
        print ("A partir de 7 años de servicio, el trabajador", nombre, "recibe '22' dias de vacaciones.")

    else :
        print ("No ingreso un valor númerico.")
        
elif clave == 3 :
    print ("Bienvenido al departamento de 'GERENCIA' \n")
    
    años = int(input("\n Ingrese los años que lleva en la empresa: "))

    if años == 1 :
        print ("Con 1 año de servicio, el trabajador", nombre, "recibe '10' dias de vacaciones.")

    elif años >= 2 and años <= 6 :
        print ("De 2 a 6 año de servicio, el trabajador", nombre, "recibe '20' dias de vacaciones.")

    elif años >= 7 :
        print ("A partir de 7 años de servicio, el trabajador", nombre, "recibe '30' dias de vacaciones.")

    else :
        print ("No ingreso un valor númerico.")

else :
    print ("No es una opción valida.")

print ("Fin.")

