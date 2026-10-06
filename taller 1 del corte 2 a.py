#Taller 1 del corte dos
#Ejercicio 1
lenguajes = ("pseudocodigo", "thony", "paython", "R", "JavaScript",)
print(lenguajes [-1])
print(lenguajes [1])
print(len(lenguajes))
# Ejercicio 2
edades = (23, 31, 18, 19, 24, 35, 35, 45, 20, 20)
for edad in edades:
    if edad >= 18:
        print("Mayor:", edad)
    if edad < 18:
        print("Menor:", edad)
#Ejercicio 3
numeros = (2, 3, 4, 2, 6, 7, 8, 10, 13, 12)
Suma = sum(numeros)
print("Total de suma:",Suma)
Maximo = max(numeros)
print("el numero maximo es:", Maximo)
Minimo = min(numeros)
print("el numero minimo es:", Minimo)
promedio = Suma/10
print("El prmedio es:", promedio)

#Ejercicio 4
print("Escriba una palabra")
palabra = input()
tupla_c = ()
lista_caracteres = []
contador_a = 0

for caracter in palabra:
    print(caracter)
    lista_caracteres.append(caracter)
    if caracter == "a" or caracter == "A":
        contador_a += 1

       
print("Tupla de caracteres:", tupla_c)
print("La letra 'a' aparece", contador_a, "veces.")

#Ejercicio 5
semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

print ("Escriba un numero del 1 al 7")
numero = int(input())

if numero >= 1 and numero <= 7:
    print("El dia de la semana es:", semana[numero - 1])
else:
    print("Error: El número debe estar entre 1 y 7")
     
print("El dia de la semana es", )
#Ejercio 6
nombre = input(("Ingrese su nombre "))
edad = input(("Digite su edad "))
programa = input(("Ingrese su programa acasemico "))
semestre = input(("Ingrese el semestre en el que esta "))
promedio = float(input("Ingrese su promedio "))
estudiante = (nombre, edad, programa, semestre, promedio)
nom, e, prog, sem, prom = estudiante
print(f"""
FICHA DEL ESTUDIANTE
Nombre: {nom}
Edad: {e}, años
Programa: {prog}
Semestre: {sem}
Promedio: {prom}
""")
#Ejercicio 7