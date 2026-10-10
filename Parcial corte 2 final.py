#Parcial de Corte 2
#Sistema de ventas e inventario
catalogo = [
    ("P01", "Mouse", 45000, 10, "Perifericos"),
    ("P02", "Teclado", 80000, 8, "Perifericos"),
    ("P03", "Memoria USB", 35000, 15, "Almacenamiento"),
    ("P04", "Audifonos", 65000, 6, "Audio"),
    ("P05", "Webcam", 120000, 5, "Video")
]
#P se va a denominar al producto

def buscar_producto(lista_cat, cod_buscado):
    for p in range(len(lista_cat)):
        if lista_cat[p][0] == cod_buscado:
            return p
    return -1

#Punto 2
def calcular_descuento(subtotal_monto):
    if subtotal_monto < 100000:
        return 0.0
    elif subtotal_monto < 250000:
        return 0.05
    else:
        return 0.10

def sumar_ventas(lista_ventas, pos_idx):
    if pos_idx == len(lista_ventas):
        return 0
    return lista_ventas[pos_idx][6] + sumar_ventas(lista_ventas, pos_idx + 1)

ventas = []
clientes_atendidos = set()
productos_vendidos = set()

num_ventas = int(input("Cuántas ventas se quiere registrar: "))

for i in range(num_ventas):
    print(f"\n--- REGISTRO DE VENTA {i + 1} DE {num_ventas} ---")

    #Pedir nombre
    cliente = input("Digite su nombre: ").strip()
    while cliente == "":
        print("El nombre no puede estar vacio")
        cliente = input("Digite su nombre: ").strip()

    #Pedir el codigo
    posicion = -1
    while posicion == -1:
        codigo = input("Digite el codigo del producto para la venta, ej. P01: ").strip().upper()
        posicion = buscar_producto(catalogo, codigo)
        if posicion == -1:
            print("El codigo no existe en el catálogo. Intente de nuevo.")

    stock_disponible = catalogo[posicion][3]
    precio = catalogo[posicion][2]

    cantidad = 0
    while cantidad <= 0 or cantidad > stock_disponible:
        cantidad = int(input(f"Cantidad a comprar (Stock disponible {stock_disponible}): "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
        elif cantidad > stock_disponible:
            print("La cantidad supera el stock disponible.")

    subtotal = precio * cantidad

    porcentaje_desc = calcular_descuento(subtotal)
    monto_descuento = subtotal * porcentaje_desc 
    subtotal_con_descuento = subtotal - monto_descuento  
    iva = subtotal_con_descuento * 0.19
    total_final = subtotal_con_descuento + iva

    # Actualizar stock en el catálogo reemplazando la tupla
    prod = catalogo[posicion]
    nuevo_stock = stock_disponible - cantidad
    catalogo[posicion] = (prod[0], prod[1], prod[2], nuevo_stock, prod[4])

    # Punto 4: Guardar la venta como una tupla
    venta_actual = (cliente, codigo, cantidad, subtotal, monto_descuento, iva, total_final)
    ventas.append(venta_actual)

    # Punto 5: 
    clientes_atendidos.add(cliente)
    productos_vendidos.add(codigo)

# 1. Número de ventas
num_ventas_reg = len(ventas)

# 2. Total vendido mediante la función recursiva (inicia en la posición 0)
total_jornada = sumar_ventas(ventas, 0)

# 3. Promedio de venta
promedio_venta = total_jornada / num_ventas_reg if num_ventas_reg > 0 else 0

# 4. Cantidad de clientes diferentes
cant_clientes = len(clientes_atendidos)

# Operación de conjuntos para hallar los productos NO vendidos
# Primero obtenemos un conjunto con TODOS los códigos existentes en el catálogo
todos_los_codigos = set()
for prod in catalogo:
    todos_los_codigos.add(prod[0])

# La resta (-) entre conjuntos devuelve los que están en el catálogo pero no se vendieron
productos_no_vendidos = todos_los_codigos - productos_vendidos

# 7. Venta de mayor valor y cliente que la realizó
# Se busca la tupla cuyo total_final (posición 6) sea el mayor
venta_mayor = max(ventas, key=lambda v: v[6])
cliente_mayor = venta_mayor[0]
monto_mayor = venta_mayor[6]

# --- IMPRESIÓN DEL REPORTE FINAL ---
print("\n" + "="*40)
print("RESUMEN FINAL DE LA JORNADA")
print("="*40)
print(f"1. Número de ventas registradas: {num_ventas_reg}")
print(f"2. Total vendido (recursivo): ${total_jornada:,.2f}")
print(f"3. Promedio por venta: ${promedio_venta:,.2f}")
print(f"4. Cantidad de clientes diferentes: {cant_clientes}")
print(f"5. Productos vendidos: {productos_vendidos}")
print(f"6. Productos NO vendidos: {productos_no_vendidos}")
print(f"7. Mayor venta realizada: ${monto_mayor:,.2f} (Cliente: {cliente_mayor})")

# 8. Mostrar catálogo final con stock actualizado
print("\nCATÁLOGO FINAL ACTUALIZADO")
for prod in catalogo:
    print(f"Código: {prod[0]} | Producto: {prod[1]} | Precio: ${prod[2]} | Stock: {prod[3]} | Categoría: {prod[4]}")