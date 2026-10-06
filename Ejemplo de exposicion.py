#Exposicion
canciones = ["Al Taller del Maestro",
           "Inextinguible",
           "Dios Imparable",
           "En Sintonía",
           "¿Dónde Estabas Tú?",
           "El Rancho",
           "Más de lo que Soñé",
           "Tu Poeta",
           "Espíritu Santo",
           "Tu Amor Me Conquistó",
           "Las Alas de la Mariposa",
           "El Sabor de la Vida",
           "Sueño de Morir",
           "La Oveja Trasquilada",
           "Se Despierta Mi Corazón",
           "Dios Imparable",
           "Fiesta",
           "Siguiendo Tus Pasos",
           "Tu Presencia",
           "Me Robaste el Corazón"]
#Índices en listas
print(canciones[0]) # Al Taller del Maestro
print(canciones[4]) # ¿Dónde Estabas Tú?
print(canciones[-1]) # Me Robaste el Corazón
#Agregar, modificar y eliminar en listas
canciones.append("Dios esta Aqui") # agrega al final
canciones[0] = "Milagro de Amor" # modifica una posicion
canciones.remove("La Oveja Trasquilada") # elimina la canción por su nombre
 
print(canciones)
# Recorrer la lista
print(" MI PLAYLIST ")
for cancion in canciones:
    print("Reproduciendo:", cancion)