import random

hp_heroe = 100
hp_enemigo = 120
pociones = 3

hp_max_heroe = 100
hp_max_enemigo = 120

def generar_daño(minimo, maximo):
    return random.randint(minimo, maximo)

def barra_vida(hp, hp_max):
    longitud = 10
    llenos = int((hp / hp_max) * longitud)
    vacios = longitud - llenos
    return "[" + "♡" * llenos + "-" * vacios + "]"

def mostrar_estado():
    print("\n=== ESTADO ACTUAL ===")
    print(f"Héroe:   {barra_vida(hp_heroe, hp_max_heroe)} {hp_heroe} HP")
    print(f"Enemigo: {barra_vida(hp_enemigo, hp_max_enemigo)} {hp_enemigo} HP")

def turno_jugador():
    global hp_enemigo, hp_heroe, pociones

    print("\n1. Atacar\n2. Curar\n3. Habilidad Especial")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        daño = generar_daño(10, 25)
        if random.random() < 0.1:
            daño *= 2
            print("¡CRÍTICO!")
        hp_enemigo -= daño
        print(f"El Hereoe golpea por {daño}")

    elif opcion == "2":
        if pociones > 0:
            hp_heroe += 20
            hp_heroe = min(hp_heroe, hp_max_heroe)
            pociones -= 1
            print("Te curaste")
        else:
            print("Sin pociones")
            return False

    elif opcion == "3":
        if random.random() < 0.5:
            daño = generar_daño(30, 50)
            if random.random() < 0.1:
                daño *= 2
                print("¡CRÍTICO!")
            hp_enemigo -= daño
            print(f"Especial: {daño}")
        else:
            print("Fallaste")

    else:
        print("Opción inválida")
        return False

    return True

def turno_enemigo():
    global hp_heroe, hp_enemigo

    if hp_enemigo < 0.2 * hp_max_enemigo and random.random() < 0.5:
        hp_enemigo += 15
        hp_enemigo = min(hp_enemigo, hp_max_enemigo)
        print("El enemigo se cura")
        return

    daño = generar_daño(15, 20)
    if random.random() < 0.1:
        daño *= 2
        print("¡CRÍTICO enemigo!")
    hp_heroe -= daño
    print(f"Enemigo hace {daño}")

def verificar_ganador():
    if hp_heroe <= 0:
        print("Perdiste")
        return True
    elif hp_enemigo <= 0:
        print("Ganaste")
        return True
    return False

juego_activo = True

while juego_activo:
    mostrar_estado()

    if not turno_jugador():
        continue

    if verificar_ganador():
        break

    turno_enemigo()

    if verificar_ganador():
        break