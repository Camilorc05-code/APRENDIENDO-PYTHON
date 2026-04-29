### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7 : Lección Llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6 : Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
#if not(match == None): #Otra forma de comprobar el None
if match is not None:
  print(match)
  start, end = match.span()
  print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

# search 

search = re.search("lección", my_string, re.I)
print(search)

start, end = search.span()
print(my_string[start:end])

# findall 

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("lección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patterns

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d]"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

import re

email = "camilo@camilo.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"

print(re.match(pattern, email))      # Match object
print(re.search(pattern, email))     # Match object
print(re.findall(pattern, email))    # ['camilo@camilo.com']

email = "camilo@camilo.com.mx.es"
print(re.findall(pattern, email))