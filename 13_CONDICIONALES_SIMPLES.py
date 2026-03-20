print ("Sistema para calcular el promedio de un alumno")


nombre = input("Para comenzar, ¿cual es tu nombre?: ")

Matematicas_nota = int (input(nombre +  "¿Cual es tu calificación en matematicas?: "))
Quimica_nota = int (input(nombre +  "¿Cual es tu calificación en quimica?: "))
Biologia_nota = int (input(nombre +  "¿Cual es tu calificación en biologia?: "))

num_uno = 3

resultado = Matematicas_nota + Quimica_nota + Biologia_nota
resultado_1 = resultado / 3

if resultado_1 >= 6 :
    print("Felicidades" + nombre + "aprobaste""con un promedio de: "+ str(resultado_1))

print("Fin.")
