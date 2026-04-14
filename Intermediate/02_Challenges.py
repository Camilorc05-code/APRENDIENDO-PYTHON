### Challenges ###
""""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) 
los números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

print("EL FAMOSO 'FIZZ BUZZ' \n")

def fizzbuzz():
    for indice in range(1,101):
     if indice % 3 == 0 and indice % 5 == 0:
        print("fizzbuzz")
     elif indice % 3 == 0:
       print("fizz")
     elif indice % 5 == 0:
       print("buzz")
     else:
      print(indice)

fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
-Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
-NO hace falta comprobar que ambas palabras existan.
-Dos palabras exactamente iguales no son anagrama. 
"""
print("¿ES UN ANAGRAMA?\n")

def is_anagrama(word_one, word_two):
  if word_one.lower() == word_two.lower():
    return False
  return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagrama("Amor", "Roma"))

"""
Escribe un programa que imprima los 50 primeros números de la suseción 
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de número en
la que el siguiente siempre es la suma de los dos anteriores.
"""

def fibonacci():

  prev = 0
  next = 1

  for index in range(0, 11):
    print(prev)
    fib = prev + next
    prev = next
    next = fib

fibonacci()
  


