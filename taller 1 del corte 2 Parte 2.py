# Ejercicio 9
def cuenta_regresiva(n):
    print (n)
    if n == 0:
        return
    cuenta_regresiva(n-1)
numero = int((input("Escriba un numero: ")))
cuenta_regresiva(numero)
#Ejercicio 10
def suma_n(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n + suma_n(n - 1)
numero = int(input("Digite un numero entero positivo: "))
print("Resultado de la suma:", suma_n(numero))

#Ejercicio 11
def factorial(n):
    print("Entrando con n=", n)
    if n == 1:
        return 1
    return n * factorial(n-1)
print("el factorial es",)
#Ejercicio 12
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente -1)

b = float(input("Digite la base: "))
e = int(input("Digite el exponente: "))
resultado = potencia(b, e)
print("El resultado es: ", resultado)
#Ejercicio 13
def contar_digitos(n):
    return len(str(n))
codigo = int(input("Digite un código,ejemplo(53829): "))
cantidad = contar_digitos(codigo)
print("El número de dígitos es:", cantidad)