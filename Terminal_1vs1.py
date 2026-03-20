import random

# FUNCIONES
# ======================

def damage_generated(minimum, maximum):
    return random.randint(minimum, maximum)


def player_turn(hp_hero, hp_enemy, pociones):

    opcion_valida = False

    while opcion_valida == False:

        print("\n1. Atacar")
        print("2. Curar")
        print("3. Habilidad especial")

        opcion = input("Elige: ")

        if opcion == "1":
            daño = damage_generated(10, 25)
            hp_enemy -= daño
            print("Hiciste", daño, "de daño")
            opcion_valida = True

        elif opcion == "2":
            if pociones > 0:
                hp_hero += 20
                pociones -= 1
                print("Te curaste 20 HP")
                opcion_valida = True
            else:
                print("No tienes pociones, intenta otra opción")

        elif opcion == "3":
            if random.random() < 0.5:
                daño = damage_generated(30, 50)
                hp_enemy -= daño
                print("Habilidad especial:", daño)
            else:
                print("Fallaste la habilidad")
            opcion_valida = True

        else:
            print("Opción inválida")

    return hp_hero, hp_enemy, pociones


def turno_enemigo(hp_jugador):
    daño = damage_generated(15, 20)
    hp_jugador -= daño
    print("El enemigo te hace", daño, "de daño")
    return hp_jugador


# MENÚ PRINCIPAL
# ======================

programa_activo = False

while programa_activo == False:

    print("\n=== THE PVP ===")
    print("1. Jugar")
    print("2. Salir")

    opcion_menu = input("Elige una opción: ")

    # OPCIÓN: JUGAR
    # ======================
    if opcion_menu == "1":

        # VARIABLES DEL JUEGO
        hp_jugador = 100
        hp_enemigo = 120
        pociones = 3

        print("\n¡Let the Battle Begin!")

        # BUCLE DEL JUEGO
        # ======================

        while hp_jugador > 0 and hp_enemigo > 0:

            print("\n--- NEW SHIFT ---")
            print("Tu vida:", hp_jugador)
            print("Vida enemigo:", hp_enemigo)
            print("Pociones:", pociones)

            hp_jugador, hp_enemigo, pociones = player_turn(
                hp_jugador, hp_enemigo, pociones
            )

            if hp_enemigo > 0:
                hp_jugador = turno_enemigo(hp_jugador)

        # RESULTADO
        if hp_jugador > 0:
            print("¡Ganaste!")
        else:
            print("Perdiste...")

    # OPCIÓN: SALIR
    # ======================
    elif opcion_menu == "2":
        print("Saliendo del juego...")
        programa_activo = True

    # OPCIÓN INVÁLIDA
    # ======================
    else:
        print("Opción inválida, intenta otra vez")
