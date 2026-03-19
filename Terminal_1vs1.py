
#1. IMPORTAR LIBRERIAS
#2. CREAR VARIABLES (ESTADO DEL JUEGO)
#3. CREAR FUNCIONES
#4. CREAR EL BUCLE PRINCIPAL
#5. EJECUTAR EL JUEGO


import random

print("---------------------")
print("WELCOME TO THE RUMBLE")
print("---------------------")


hp_hero= 100
hp_enemy= 120
pociones= 3
hp_max_hero= 100
hp_max_enemy= 120

def generate_damage( minimum, maximum ):
    return random.randint(minimum,maximum)
