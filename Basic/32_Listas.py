#Listas
my_list = list()
my_other_list = []

my_list = [35, 32, 20, 11, 15]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Camilo"]

print(type(my_other_list))

print(my_other_list[1])

a, b, c, = my_other_list
print(c)

print(my_other_list, my_list)

my_other_list.append("Colombia")

my_other_list.insert(1, "Azul")

print(my_other_list)

my_other_list.remove("Azul")

print(my_other_list)