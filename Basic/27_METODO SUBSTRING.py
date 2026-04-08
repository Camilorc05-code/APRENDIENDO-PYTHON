#METODO SUBSTRING

string = "0123456789"
substring = ""

print(f"Cadena principal: {string}")

substring = string[0]
print(f"\nsubcadena con indice en la posición [0] es: {substring}")

substring = string[5]
print(f"\nsubcadena con indice en la posición [5] es: {substring}")

substring = string[0:3]
print(f"\nsubcadena con indice en la posición [0:3] es: {substring}")

substring = string[1:6:2]
print(f"\nsubcadena con indice en la posición [1:6:2] es: {substring}")

substring = string[5:]
print(f"\nsubcadena con indice en la posición [5:] es: {substring}")

substring = string[3:]
print(f"\nsubcadena con indice en la posición [3:] es: {substring}")
