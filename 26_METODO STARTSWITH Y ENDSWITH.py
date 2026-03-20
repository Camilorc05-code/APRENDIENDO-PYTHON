#METODO STARTSWITH Y ENDSWITH

string = "Diana se peina sola"
resultado = 0
starts_with = "Ejemplos con startswith():"
ends_with = "Ejemplos con endswith():"

print(f"\n{starts_with.rjust(50, '=')}")

resultado = string.startswith("D")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado = string.startswith("Diana")
print(f"\n{string} comienza con la subcadena Diana: {resultado}")

resultado = string.startswith("a")
print(f"\n{string} comienza con la subcadena a: {resultado}")

resultado = string.startswith("se", 6)
print(f"\n{string} comienza con la subcadena se, desde la posición 6: {resultado}")

resultado = string.startswith("se", 6, 7)
print(f"\n{string} comienza con la subcadena se, desde la posición 6 hasta la 7: {resultado}")



print(f"\n{ends_with.rjust(50, '=')}")

resultado = string.endswith("A")
print(f"\n{string} termina con la subcadena A: {resultado}")

resultado = string.endswith("a")
print(f"\n{string} termina con la subcadena a: {resultado}")

resultado = string.endswith("sola")
print(f"\n{string} termina con la subcadena sola: {resultado}")

resultado = string.endswith("sola", 10)
print(f"\n{string} termina con la subcadena sola, desde la posición 10: {resultado}")

resultado = string.endswith("s", 9, 14)
print(f"\n{string} termina con la subcadena s, desde la posición 9 hasta la posición 14: {resultado}")
