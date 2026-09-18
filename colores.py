colores = ("rojo", "azul", "verde")

lista_colores = list(colores)
lista_colores[0] = "amarillo"
colores = tuple(lista_colores)

print(colores)