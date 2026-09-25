frutas =["manzana", "pera" ,"uva"]
numeros=[10, 20, 30, 40]
mixta = ["Ana", 18, 4.5, True]
print(frutas)
print(numeros)
print(mixta)

estudiantes = ["Laura", "Carlos", "Diana", "Mateo",]

print(estudiantes[0])
print(estudiantes[1])
print(estudiantes[-1])

notas = [3.0, 4.2, 2.8]

notas.append(5.0) #Agrega al final
notas[0] = 3.5  #Modifica una posicion
notas.remove(2.8) #Elimina el valor 2.8
print(notas)

notas = [4.0, 3.5, 2.9, 5.0]

for nota in notas:
    print ("Nota:", nota)
    
notas = [4.0, 3.5, 2.9, 5.0]
suma=0
for nota in notas:
    suma = suma + nota
    
promedio = suma / len(notas)
print("Promedio:", promedio)

#SETS

numeros = {1, 2, 3, 3, 4, 4, 5}
print(numeros)

nombres = {"Ana", "Luis", "Ana", "Marta"}
print(nombres)

#Agregar y eliminar sets

usuarios ={"ana","luis", "marta"}

usuarios.add("Carlos")
usuarios.discard("luis")

print(usuarios)

ciudades = ["Bogota", "Cali", "Bogota", "Medellin"]
ciudades_unicas = set(ciudades)

print(ciudades)
print(ciudades_unicas)

#Operaciones entre sets
grupo_a = {"Ana", "Luis", "Marta"}
grupo_b = {"Luis", "Carlos", "Diana"}

print(grupo_a | grupo_b) #Union
print(grupo_a & grupo_b) # Interseccion
print(grupo_a - grupo_b) #diferencia

#Ejemplo
inscritos = {"Ana", "Luis", "Marta", "Carlos"}
asistieron = {"Ana", "Carlos"}

faltaron = inscritos - asistieron
print("Faltaron:", faltaron)

#Ejercicio 1 guiado

notas = []

for i in range(5):
    nota = float(input("Digite una nota: "))
    notas.append(nota)
    
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Mayor", max(notas))
print("Menor", min(notas))

#Ejercicio 1 guiado
codigos = []

for i in range(6):
    codigo = input("Digite codigo: ")
    codigos.append(codigo)
    
codigos_unicos = set(codigos)
print("Todos:", codigos)
print("Unicos", codigos_unicos)