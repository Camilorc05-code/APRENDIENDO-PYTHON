## Tuples - No cambian sus valores ni se pueden añadir despues como la lista ## 

my_tuple= tuple()
my_other_tuple = (40, 2.00, "Hola")

my_tuple = (35, 1.77, "Camilo", "Rodriguez")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.index("Camilo"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:5])

#Pasar Tupla a Lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Felipe"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))

my_tuple = tuple(my_tuple)
print(type(my_tuple))

