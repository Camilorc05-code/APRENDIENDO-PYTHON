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
"EJERCICIO FINOBACCI"
Escribe un programa que imprima los 50 primeros números de la suseción 
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de número en
la que el siguiente siempre es la suma de los dos anteriores.
"""
print("EJERCICIO FINOBACCI")
def fibonacci():

  prev = 0
  next = 1

  for index in range(0, 11):
    print(prev)
    fib = prev + next
    prev = next
    next = fib

fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
print("¿ES UN NÚMERO PRIMO?")

def es_primo():
    
    for number in range(1, 101):

      if number >= 2:

        es_divisible = False
      
        for index in range(2,number):
            if number % index == 0:
              es_divisible = True
              break

        if not es_divisible:      
           print(number)
    
es_primo()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje  que lo hagan de forma automatica.
- Si le pasamos "Hola mundo" nos retornaria "odnum aloH"
"""

def reverse(text):
  text_len = len(text) 
  reverse_text = ""
  for index in range(0, text_len):
    reverse_text += text[text_len - index -1]

  return reverse_text

print(reverse("Hola mundo"))





