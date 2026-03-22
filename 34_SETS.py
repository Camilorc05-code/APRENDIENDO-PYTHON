## SETS ##

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Camilo", "Rodriguez", 19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Felipe")

print(my_other_set) # Un set no es una estructura ordenada y no acepta valores repetidos

print("Camilo" in my_other_set)
print("Carlos" in my_other_set)

my_other_set.remove("Felipe")
print(my_other_set)

my_other_set.clear() #Borra datos de la variable
print(len(my_other_set))

del my_other_set #Borra toda la variable

my_set = {"Camilo", "Rodriguez", 19}
my_set = list(my_set)
print(type(my_set))

my_other_set = {"Camilo", "Rodriguez", 20}

my_new_set = my_set.union(my_other_set)
print(my_new_set)