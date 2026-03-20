print ("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")

Matematicas_nota = float (input(nombre +  ", ¿Cual es tu calificación en matematicas?: "))
Quimica_nota = float (input(nombre +  ", ¿Cual es tu calificación en quimica?: "))
Biologia_nota = float (input(nombre +  ", ¿Cual es tu calificación en biologia?: "))

promedio = (Matematicas_nota + Quimica_nota + Biologia_nota) / 3

if promedio >= 6 :
    print ('Felicidades ' + nombre + ', "aprobaste" con un promedio de: ', promedio)
    print ('Felicidades ' + nombre + ', "aprobaste" con un promedio de: ', round (promedio,2))

else :
    print ('Lo sentimos ' + nombre + ', has "reprobado" con un promedio de: ', promedio)
    print ('Lo sentimos ' + nombre + ', has "reprobado" con un promedio de: ', round (promedio, 1))


print ("Fin.")
