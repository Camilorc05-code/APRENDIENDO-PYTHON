## DICCIONARIOS ##

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Camilo", "Apellido":"Rodriguez", "Edad":19, 1:"Python"}
my_dict = {
    "Nombre":"Camilo", 
    "Apellido":"Rodriguez", 
    "Edad":19, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.72
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Felipe"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle 12"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Camilo" in my_dict)
print("Nombre" in my_dict)
print("Camili" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, ("Camilo", "Rodriguez"))
print((my_new_dict))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
