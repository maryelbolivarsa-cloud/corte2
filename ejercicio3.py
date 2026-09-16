def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo = n % 10
        resto = n // 10
        return ultimo + suma_digitos(resto)
    
numero = int(input("Digite un numero entero: "))
print("Suma de digitos", suma_digitos(numero))