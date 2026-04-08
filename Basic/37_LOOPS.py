### LOOPS ###

# WHILE

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else :  #Es opcional
    print("Mi condición es mayor o igual que 10")

while my_condition < 20 :

     my_condition += 1
     if my_condition == 15:
         print("Se detiene la ejecución")
         break
     print(my_condition)

# FOR

my_list = [35, 24, 12, 42, 54, 63, 14]

for element in my_list:
    print(element)

my_tupla = (35, 53, "Camilo", "Rodriguez")
for element in my_tupla:
    print(element)

my_set = {"Camilo", "Rodriguez", 19}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Camilo", "Apellido":"Rodriguez", "Edad":19, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario a finalizado")

print("La ejecución continua")
