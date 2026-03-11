import random

# Player stats
player = {
    "name": input("Enter your hero name: "),
    "health": 100,
    "attack": 20,
    "potions": 3
}

# Enemy list
enemies = [
    {"name": "Goblin", "health": 60, "attack": 12},
    {"name": "Skeleton", "health": 70, "attack": 13},
    {"name": "Orc", "health": 80, "attack": 15}
]

game_running=True
enemy = random.choice(enemies)

#Main game loop
print(f"\nWelcome {player['name']}! Your adventure begins...\n")
print(f"⚔️ A wild {enemy['name']} appears!")
print(f"Your goal: [Defeat the enemy or run away safely]")

while game_running and enemy["health"] > 0 and player["health"] > 0:
    print(f"\nYour Health: {player['health']}")
    print(f"{enemy['name']} Health: {enemy['health']}")
    
    print("What will you do?")
    print("1. Attack")
    print("2. Run Away")
    print("3. Use Potion")

    choice = input("Enter Your Choice (1/2/3): ")

    if choice == "1":
        damage = random.randint(10, player["attack"])
        enemy["health"] -= damage
        print(f"You dealt {damage} damage!")

    elif choice == "2":
        print("\n You ran away safely!")
        game_running=False
        break

    elif choice == "3":
        if player["potions"] > 0:
            heal = random.randint(10, 15)
            player["health"] += heal
            player["potions"] -= 1
            print(f"You healed {heal} HP. Potions left: {player['potions']}")
        else:
            print("No potions left!")

    else:
        print("Invalid choice!")
        continue

    if enemy["health"] > 0:
        enemy_damage = random.randint(10, enemy["attack"])
        player["health"] -= enemy_damage
        print(f"{enemy['name']} hit you for {enemy_damage} damage!")

if player["health"] > 0 and choice!="2":
    print(f"\n🎉 Congratulations!!! You defeated the {enemy['name']}!\n")
    print('*'*5,"You survived the RPG adventure!",'*'*5)
elif player["health"] > 0 and choice=="2" :
    print('*'*5,"🏆 You survived the RPG adventure!",'*'*5)
else:
    print("\n💀 You were defeated by the enemy...")
    print("Game Over. Try again!")

