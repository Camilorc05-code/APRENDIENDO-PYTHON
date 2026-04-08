### FUNCIONES ###

def my_funcion ():
    print("Esto es una función")

my_funcion ()
my_funcion ()
my_funcion ()

def sum_two_values (primer_numero, segundo_numero):
    print("Resultado de suma: ", primer_numero + segundo_numero)

sum_two_values (4, 6)
sum_two_values (1.4, 3.4)
sum_two_values ("5", "7")

def sum_two_values_with_return (primer_numero, segundo_numero):
    return primer_numero + segundo_numero

my_result = sum_two_values_with_return (10, 5)
print("Resultado suma con return: ", my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Rodriguez", name = "Camilo")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Camilo", "Rodriguez")
print_name_with_default("Camilo", "Rodriguez", "Alias")

def print_texts (*text):
    print(text)

print_texts("Hola", "¿Como estas?", "¿Bien y tu?")

def print_texts_for (*texts):
    for text in texts:
        print(text.upper())

print_texts_for("Hola", "¿Como estas?", "¿Bien y tu?")