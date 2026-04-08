### CLASES ###

class MyPerson: 
    pass

print(MyPerson)
print(MyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" #Propiedad publica
        self.__name = name #Propiedad privada

    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} esta caminando")
       

my_person = Person("Camilo", "Rodriguez")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Camilo", "Rodriguez", "RC_05")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Felipe es inteligente"
print(my_other_person.full_name)

my_other_person.full_name = 2342
print(my_other_person.full_name)



