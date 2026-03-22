import random
import time

# FUNCTIONS
# =============

def damage_generated(minimum, maximum):
    return random.randint(minimum, maximum)


def life_bar(hp, hp_max):
    length = 10
    full = int((hp / hp_max) * length)
    empty = length - full
    return "[" + "♡" * full + "-" * empty + "]"


def show_status(hp_hero, hp_enemy, hp_max_hero, hp_max_enemy, potions):
    print("\n===⛩︎ STATE ⛩︎===")
    print(f"Hero:   {life_bar(hp_hero, hp_max_hero)} {hp_hero} HP")
    print(f"Enemigo: {life_bar(hp_enemy, hp_max_enemy)} {hp_enemy} HP")
    print(f"Pociones: {potions} ")


def hero_turn(hp_hero, hp_enemy, potions):

    valid_option = False

    while not valid_option:

        print("\n1.Attack")
        print("2.Cure")
        print("3.Special ability")

        option = input("Which one do you want to choose: ")

        if option == "1":
            damage = damage_generated(10, 25)
            hp_enemy -= damage
            print(f"⚔︎ Your hit inflicted {damage} points of damage ⚔︎")
            valid_option = True

        elif option == "2":
            if potions > 0:
                hp_hero += 20
                potions -= 1
                print("⚱︎ You healed 20 HP")
                valid_option = True
            else:
                print("✖︎ You've run out of potions ✖︎")

        elif option == "3":
            if random.random() < 0.5:
                damage = damage_generated(30, 50)
                hp_enemy -= damage
                print(f"☄︎ The special ability was activated, you inflicted {damage} points of damage ☄︎")
            else:
                print("⤵︎ Special ability activation failed")
            valid_option = True

        else:
            print("✖︎ Invalid option, please try again ✖︎")

    return hp_hero, hp_enemy, potions


def enemy_turn(hp_hero, hp_enemy, hp_max_enemy):

    
    if hp_enemy < 0.2 * hp_max_enemy:
        if random.random() < 0.5:
            hp_enemy += 15
            print("⚱︎ The enemy healed for 15 HP")
            return hp_hero, hp_enemy

    damage = damage_generated(15, 20)
    hp_hero -= damage
    print(f"☢︎ The enemy inflicted {damage} points of damage on you ☢︎")

    return hp_hero, hp_enemy


def winner_verfication(hp_hero, hp_enemy):
    if hp_hero <= 0:
        print("\n☠︎You lost...☠︎")
        exit()
        return True
    elif hp_enemy <= 0:
        print("\n♚ You won! ♚")
        exit()
        return True
    return False



# MAIN MENU
# =============

active_program = True

while active_program:

    print("\n==⚔︎ THE PVP ⚔︎==")
    print("1.Start Playing☑")
    print("2.Exit the Game☒")

    menu_option = input("choose an option: ")

    if menu_option == "1":

        hp_hero = 100
        hp_enemy = 120
        potions = 3
        hp_max_hero = 100
        hp_max_enemy = 120

        print("\n✴︎ ¡Let the battle begin! ✴︎")

        while hp_hero > 0 and hp_enemy > 0:

            show_status(
                hp_hero, hp_enemy, hp_max_hero, hp_max_enemy, potions
            )

            hp_hero, hp_enemy, potions = hero_turn(
                hp_hero, hp_enemy, potions
            )

            winner_verfication(hp_hero, hp_enemy)

            if hp_enemy > 0:
                 hp_hero, hp_enemy = enemy_turn(
                 hp_hero , hp_enemy , hp_max_enemy
                 )
                 winner_verfication(hp_hero, hp_enemy)
                 
                 
               

    elif menu_option == "2":
        print("Leaving...⏱︎")
        time.sleep(1.5)
        active_program = False

    else:
        print("✖︎ Invalid option, please try again ✖︎")