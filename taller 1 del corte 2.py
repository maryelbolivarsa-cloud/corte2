#Taller 1 del corte dos
#Ejercicio 1
lenguajes = ("pseudocodigo", "thony", "paython", "R", "JavaScript",)
print(lenguajes [-1])
print(lenguajes [1])
print(len(lenguajes))
#Ejercicio 2
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
palabras = input()
for palabra in palabras:
    print(palabra)
 
