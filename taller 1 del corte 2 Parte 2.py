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
    print("Entando con n=", n)
    if n == 1:
        return 1
    return n * factorial(n-1)

        