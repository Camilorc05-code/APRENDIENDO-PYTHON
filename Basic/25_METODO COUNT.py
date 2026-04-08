#METODO COUNT

string = "mi mamá me mima"
contador = 0

print(string.center(40, "="))

contador = string.count("m")
print(f"\nLa letra m se encontro {contador} veces en la cadena: {string}")

contador = string.count("mamá")
print(f"\nLa letra mamá se encontro {contador} veces en la cadena: {string}")

contador = string.count("m", 13)
print(f"\nLa letra m se encontro {contador} veces, desde la posición 13 en la cadena: {string}")

contador = string.count("m", 100, 100)
print(f"\nLa letra m se encontro {contador} veces, desde la posición 100 hasta la posición 100 en la cadena: {string}")
