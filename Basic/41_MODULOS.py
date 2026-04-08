### MODULOS ###

import Basic.my_module as my_module
#from 38_FUNCIONES import sum_two_values #Python no lo reconoce por que tiene un número "38" en el nombre

my_module.suma(5, 3, 1)
my_module.printValue("Hola Python!")

from Basic.my_module import suma, printValue

suma(5, 6, 1)
printValue("Hola Python!")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)