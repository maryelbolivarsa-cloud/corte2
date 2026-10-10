#Parte 1
import random

def crear_baraja():
    palos = ("Corazones", "Diamantes", "Treboles", "Picas")
    valores = ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
               "J", "Q", "K", "A")
    baraja = []
    for palo in palos:
        for valor in valores:
            baraja.append((valor, palo))
            random.shuffle(baraja)
            return baraja

def valor_carta(carta):
    """Devuelve el valor base de una carta. El As se calcula inicialmente como 11."""
    valor = carta[0]
    
    if valor in ("J", "Q", "K"):
        return 10
    if valor == "A":
        return 11
    return int(valor)

def calcular_puntos(mano):
    total = 0
    cantidad_ases = 0
    
    for carta in mano:
        total += valor_carta(carta)
        
        if carta[0] == "A":
            cantidad_ases += 1
    
    while total > 21 and cantidad_ases > 0:
        total -= 10
        cantidad_ases -= 1
        
    return total