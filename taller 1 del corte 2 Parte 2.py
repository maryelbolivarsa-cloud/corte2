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
def contar(n):
    return len(str(n))
codigo = int(input("Digite un código,ejemplo(53829): "))
cantidad = contar(codigo)
print("El número de dígitos es:", cantidad)
#Ejercico 14
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
    #Ejercicio 15
    def inver_cadena(cadena):
        if len(cadena) <= 1:
            return cadena
        return cadena[-1] + inver_cadena(cadena[:-1])
    text = input("Ingrese una palabra: ")
    resultado2 = inver_cadena(text)
    print(f"Resultado: ", resultado2)
    