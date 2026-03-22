⚔️ THE PVP - Turn-Based Battle Game

📌 Overview

THE PVP is a simple turn-based battle game developed in Python.
The player controls a hero who fights against an enemy controlled by basic artificial intelligence.

The goal is simple: defeat the enemy before your health reaches zero.

---

🎮 How the Game Works

The game runs in the console and is based on turns:

1. The player chooses an action.
2. The action is executed.
3. The enemy takes its turn automatically.
4. The process repeats until someone wins.

---

🧩 Player Actions

During each turn, the player can choose:

⚔️ Attack

- Deals random damage between 10 and 25 HP.

⚱️ Cure

- Restores 20 HP.
- Consumes 1 potion.
- Limited number of potions available.

☄️ Special Ability

- Has a 50% chance to activate.
- If successful: deals 30 to 50 damage.
- If it fails: nothing happens.

---

🤖 Enemy Behavior (AI)

The enemy acts automatically:

- Normally attacks dealing 15–20 damage.
- If its health drops below 20%, it has a chance to:
  - Heal 15 HP instead of attacking.

---

❤️ Health System

Both the hero and the enemy have:

- A numeric HP value
- A visual life bar like this:

[♡♡♡♡♡-----]

This helps the player easily understand the current state of the battle.

---

🔁 Game Flow

1. Main menu is displayed:
   - Start Game
   - Exit
2. Player starts a battle
3. Game enters a loop:
   - Show status
   - Player turn
   - Check winner
   - Enemy turn
   - Check winner again
4. Game ends when:
   - Hero HP = 0 → You lose
   - Enemy HP = 0 → You win

---

🧠 Functions Explained

"damage_generated(minimum, maximum)"

Generates a random damage value between two numbers.

---

"life_bar(hp, hp_max)"

Creates a visual representation of health using symbols.

---

"show_status(...)"

Displays:

- Hero health
- Enemy health
- Remaining potions

---

"hero_turn(...)"

Handles:

- Player input
- Action selection
- Damage or healing logic

---

"enemy_turn(...)"

Controls enemy decisions:

- Attack
- Heal (if low HP)

---

"winner_verfication(...)"

Checks if:

- The player lost
- The player won
  If so, the game ends.

---

🛠️ Technologies Used

- Python
- Standard libraries:
  - "random" → for randomness
  - "time" → for delays

---

🎯 Learning Objectives

This project helps practice:

- Functions
- Conditionals ("if", "elif", "else")
- Loops ("while")
- User input handling
- Game logic design

---

▶️ How to Run

1. Make sure you have Python installed
2. Run the file:

python your_file_name.py

---
