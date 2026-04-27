### File Handling ###

import os

# .txt file
txt_file = open("Intermediate/my_file.txt", "w+") # Leer y Escribir
txt_file.write("Mi nombre es Camilo\nMi apellido es Rodriguez\n35 años\nY mi lenguaje preferido es Python")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Java")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermediate/my_file.txt")

# ,json file

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "Name":"Camilo", 
    "Surname":"Rodriguez", 
    "age":19, 
    "langauges":["Python", "Swift", "Java"],
    "website":"https://camilo.rc"}

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load (open("Intermediate/my_file.json"))
print(json_dict)

print(type(json_dict))
print(json_dict["Name"])

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Camilo", "Rodriguez", 20, "Python", "https://camilo.rc"])
csv_writer.writerow(["Felipe", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xslx file
# import xlrd # Debe instalarse el módulo

# .xml file

import xml