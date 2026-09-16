"la recursion es cuando una funcion se llama asi misma"
"del problema general salen dos"
def factorial(n):
    print("Entrando con n=", n)
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))