#Ejercicio16
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Los primeros 10 términos de la sucesión de Fibonacci son:")
for i in range(10):
    print(f"Término {i}: {fibonacci(i)}")
#Ejercico 17
def suma_tupla(tupla, indice):
    if indice >= len(tupla):
        return 0
    return tupla[indice] + suma_tupla(tupla, indice + 1)
numeros = (10, 11, 12, 13, 114)
resultado = suma_tupla(numeros, 0)
print(f"Tupla: {numeros}")
print(f"La suma de los elementos es: {resultado}")
#Ejercico 18
def contar_apariciones(tupla, valor, indice=0):
    if indice >= len(tupla):
        return 0

    es_igual = 1 if tupla[indice] == valor else 0
    return es_igual + contar_apariciones(tupla, valor, indice + 1)

datos = (4, 7, 2, 7, 9, 7, 1, 4, 7, 3)
print(f"Tupla de datos: {datos}")
valor_buscado = int(input("Ingrese el número que desea contar: "))
resultado_recursivo = contar_apariciones(datos, valor_buscado)
resultado_count = datos.count(valor_buscado)
print("\n--- Resultados ---")
print(f"Resultado con función recursiva: {resultado_recursivo}")
print(f"Resultado con método .count(): {resultado_count}")
if resultado_recursivo == resultado_count:
    print("✓ Ambos métodos coinciden correctamente.")
else:
    print("✗ Los resultados difieren.")
    
#Ejercicio 19
def buscar_estudiante(tupla, nombre_buscado, indice=0):
    if indice >= len(tupla):
        return -1

    if tupla[indice] == nombre_buscado:
        return indice

    return buscar_estudiante(tupla, nombre_buscado, indice + 1)


estudiantes = ("Omar", "Otto", "Julian", "Juan", "Valentina", "Mary")

print("Lista de estudiantes: ", estudiantes)

busqueda = input("Ingrese el nombre del estudiante a buscar: ")

posicion = buscar_estudiante(estudiantes, busqueda)

if posicion != -1:
    print(
        f"El estudiante '{busqueda}' se encuentra en la posición (índice) {posicion}."
    )
else:
    print(f"El estudiante '{busqueda}' no existe en la tupla.")
#Ejercicio 20
ventas = (
    ("Cuaderno", 3, 8500),
    ("Lapiz", 5, 1500),
    ("Regla", 2, 4000)
)

# Función recursiva para calcular el valor total vendido
def ctotal_ventas(ventas, indice=0):
    if indice >= len(ventas):
        return 0
    
    producto, cantidad, precio = ventas[indice]
    ingreso_a = cantidad * precio
    
    return ingreso_a + ctotal_ventas(ventas, indice + 1)

# Total ventas (mediante la función recursiva)
total_vendido = ctotal_ventas(ventas)

# Producto de mayor ingreso y unidades totales vendidas
producto_mayor_ingreso = ""
mayor_ingreso = 0
unidades_t = 0

for producto, cantidad, precio in ventas:
    ingreso_producto = cantidad * precio
    unidades_t += cantidad
    
    if ingreso_producto > mayor_ingreso:
        mayor_ingreso = ingreso_producto
        producto_mayor_ingreso = producto

promedio_i = total_vendido / len(ventas) if len(ventas) > 0 else 0

# Muestra de resultados 
print(" INFORME DE VENTAS DEL DÍA ")
print(f"1. Valor total vendido: ${total_vendido:,.2f}")
print(f"2. Producto de mayor ingreso: {producto_mayor_ingreso} (${mayor_ingreso:,.2f})")
print(f"3. Cantidad total de unidades vendidas: ", unidades_t)
print(f"4. Promedio de ingreso por producto: ", promedio_i)