### EXEPCIONES ###

number_one = 5 
number_two = 1
number_two = "1"

# try except

try:
   print(number_one + number_two)
   print("No se ha producido un error")
except:
   #Se ejecuta si se preduce una exepción
   print("Se ha producido un error")

# try except else

try:
   print(number_one + number_two)
   print("No se ha producido un error")
except:
   print("Se ha producido un error")
else: #Opcional
   #Se ejecuta si no se produce una exepción
   print("La ejecución continúa correctamente")
finally: #Opcional
   #Se ejecuta siempre
   print("La ejecución continua")

#Exepciones por tipo

try:
   print(number_one + number_two)
   print("No se ha producido un error")
except ValueError:
   print("Se ha producido un ValueError")
except TypeError:
   print("Se ha producido un TypeError")

# Captura de la información de la exepción 

try:
   print(number_one + number_two)
   print("No se ha producido un error")
except ValueError as error:
   print(error)
except Exception as error:
   print(error)