### Error Types ###

# SyntaxError
#print "¡Hola comunidad" #Error
print ("¡Hola comunidad!")

# NameError

# NameError: name 'language' is not defined
language = "Spanish" # Comentar para Error
print(language)

# IndexError
#IndexError: list index out of range
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[2])
#print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError
#ModuleNotFoundError: No module named 'maths'
import math

# AttributeError
#AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
#print(math.PI) #Descomentar para error
print(math.pi)

# KeyErorr
#KeyError: 'Apellidos'
my_dict = {"Nombre":"Camilo", "Apellido":"Rodriguez", "Edad": 20, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apellidos"]) # Descomentar para error
print(my_dict["Apellido"])

# TypeError
#TypeError: list indices must be integers or slices, not str
#print(my_list["0"]) # Descomentar para error
print(my_list[0])

# ImportError
#ImportError: cannot import name 'PI' from 'math' 
#from math import PI # Descomentar para error
from math import pi
print(pi)

# ValueError
#ValueError: invalid literal for int() with base 10: '10 años'
#my_int = int("10 años") # Descomentar para error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError

print(4/2)
#ZeroDivisionError: division by zero
#print(4/0) # Descomentar para error