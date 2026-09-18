#Ejercicio guiado 1
notas = (4.0, 3.5, 5.0, 4.2)

suma = 0
for nota in notas:
    suma = suma + nota
    
promedio = suma / len(notas)
print("promedio:", promedio)
#Ejercicio guiado 2
temperaturas = (18, 22, 19, 25, 21)

mayor = temperaturas[0]
menor = temperaturas[0]

for temp in temperaturas:
    if temp> mayor:
        mayor =temp
    if temp < menor:
        menor = temp
        
print("Mayor:", mayor)
print("Menor:", menor)
#Ejercios
#Ejercicio1
nombres = ("Mary", "Maria", "Otto", "Julian", "Omar")
print(nombres [-1])
#Ejercicio2
numeros = (1, 3, 5, 20, 8, 100, 32)
suma=0
for numero in numeros:
    suma =+ numero
print("resultado:",suma)
#Ejercicio 3
notas = (4.0, 3.0, 5.0, 1.2)

suma = 0
for nota in notas:
    suma = suma + nota
    
promedio = suma / len(notas)

print("promedio:", promedio)
#Ejercico 4
print "Escriba una palabra"
input palabra
permitidas = ("hola", "buenas", "chao", "amor")
for perm in permitidas:
    if palabra != permitidas 