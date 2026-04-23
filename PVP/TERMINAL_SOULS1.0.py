import random

def generate_damage(minimum, maximum):
    damage = random.randint(minimum, maximum)

    if random.random() < 0.1:
        damage *= 2
        print("💥 Critical hit!")

    return damage


def show_status(hero_name, hp_h, enemy_name, hp_e):
    def health_bar(hp, max_hp):
        total = 10
        filled = int((hp / max_hp) * total)
        empty = total - filled
        return "[" + "#" * filled + "-" * empty + "]"

    print("\n=== STATUS ===")
    print(f"{hero_name}: {hp_h} HP {health_bar(hp_h, 100)}")
    print(f"{enemy_name}: {hp_e} HP {health_bar(hp_e, 120)}")
    print("==============\n")


def player_turn(hp_h, hp_e, potions):
    option = ""

    while option not in ["1", "2", "3"]:
        print("\nYour turn:")
        print("1. Attack")
        print("2. Heal (20 HP)")
        print("3. Special Ability")

        option = input("Choose an action: ")
        if option != "1" and option != "2" and option != 3:
            print("\nPlease enter a valid option")

        elif option == "2" and potions == 0:
            print("❌ You have no potions left.")
            option = ""  # force retry

    if option == "1":
        damage = generate_damage(10, 25)
        hp_e -= damage
        print(f"⚔️ You attack and deal {damage} damage!")

    elif option == "2":
        hp_h += 20
        potions -= 1
        print("🧪 You heal 20 HP!")

    elif option == "3":
        if random.random() < 0.5:
            damage = generate_damage(30, 50)
            hp_e -= damage
            print(f"🔥 Special ability successful! {damage} damage!")
        else:
            print("💨 The special ability failed!")

    return hp_h, hp_e, potions


def enemy_turn(hp_h, hp_e):
    print("Enemy's turn...")

    if hp_e <= 0.2 * 120 and random.random() < 0.5:
        hp_e += 15
        print("👾 The enemy heals 15 HP.")
    else:
        damage = generate_damage(15, 20)
        hp_h -= damage
        print(f"👾 The enemy attacks and deals {damage} damage.")

    return hp_h, hp_e


def check_winner(hp_h, hp_e):
    if hp_h <= 0:
        print("💀 You have been defeated...")
        return True
    elif hp_e <= 0:
        print("🏆 You defeated the enemy!")
        return True
    return False

def game():
    hero_name = "Hero"
    enemy_name = "Enemy"

    hp_h = 100
    hp_e = 120
    potions = 3

    print("⚔️ Welcome to Terminal Souls ⚔️")

    while hp_h > 0 and hp_e > 0:
        show_status(hero_name, hp_h, enemy_name, hp_e)

        hp_h, hp_e, potions = player_turn(hp_h, hp_e, potions)

        if check_winner(hp_h, hp_e):
            break

        hp_h, hp_e = enemy_turn(hp_h, hp_e)

        if check_winner(hp_h, hp_e):
            break

game()