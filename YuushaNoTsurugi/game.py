import random
import time
import os
import sys

# TODO: add data for another 9 levels, move it to a separate file
# Possibly use dictionary comprehensions?
level_data = {
    1: {
        "name": "FLAMMA",
        "hp": 15,
        "strength": 5,
        "block_chance": 1
    }
}

score = 0
current_lvl = 0

def start():
    print(">> GAME STARTED <<\n")
    time.sleep(1.3)
    print(">> welcome to <<SHOURI NO TSURUGI>>, a turn-based gladiator game where you climb your way up in the legendary collosseum tournament, can you win and be crowned champion of the collosseum?\n")
    time.sleep(1)
    print(">> in this game, there are 10 levels, each level there is a gladiator you have to fight. If you win - by reducing your opponent's HP to 0 - you advance to the next level. Each level your sword's strength and your HP increase and the same for your opponents.\n")
    name = get_name()
    answer = input(f">> Gladiator {name}, are you ready? (y/n) ").lower()
    answer = validate(answer, ["y", "n"])
    if answer == "y":
        clear()
        start_time = time.time()
        lvl_start(1)
    else:
        print("Coward.")
        sys.exit()

# TODO: Add block for enemy, organize code, more fighting options, make it so the program doesn't print the attack log when one hp reaches 0.
def lvl_start(lvl):
    enemy_name = level_data[lvl]["name"]
    player_hp = 15
    enemy_hp = level_data[lvl]["hp"]
    blocked = False
    winner = None
    print(">> FIGHT START <<")
    time.sleep(1)
    print(f">> LEVEL {lvl} - YOUR HP: {player_hp} - STRENGTH 5 <<")
    print(f">> GLADIATOR {enemy_name} - {enemy_hp} HP - STRENGTH 5 <<")
   
    while player_hp > 0 and enemy_hp > 0:
        # Player's turn
        choice = input("""
        >> What will you do?
            > Attack (a)
            > Block (b) 
        """).lower()
        choice = validate(choice, ["a", "b"])  
        if choice == "a":
            player_atk = random.randint(1, 5)
            print(f"YOU ATTACKED {enemy_name}")
            time.sleep(1)
            if blocked:
                print(f"YOU TRIED TO ATTACK {enemy_name}, BUT {enemy_name} BLOCKS THE ATTACK!")
            else:
                print(f"YOUR ATTACK DEALT {player_atk} DAMAGE. {enemy_name}'S HP WAS REDUCED FROM {enemy_hp} TO {enemy_hp-player_atk}")
                print("======================================================")
                enemy_hp -= player_atk
                if enemy_hp <= 0:
                    winner = "player"
                    break
            time.sleep(1)
        else:
            
            block_chance = random.choices([True, False], [0.1, 0.9])           
        if blocked:
            print(f"{enemy_name} TRIED TO ATTACK, BUT YOU BLOCK THE ATTACK!")
            blocked = False
            print("======================================================")
        # Enemy's turn
        else:
            enemy_strength = level_data[lvl]["strength"]
            enemy_atk = random.randint(1, enemy_strength)
            print(f"{enemy_name} ATTACKED YOU")
            time.sleep(1)
            print(f"{enemy_name}'S ATTACK DEALT {enemy_atk} DAMAGE. YOUR HP WAS REDUCED FROM {player_hp} to {player_hp-enemy_atk}")
            print("======================================================")
            player_hp -= enemy_atk
            if player_hp <= 0:
                winner = "enemy"
                break
                
    if winner == "player":
        print("YOU WON!")
    else:
        print("YOU DIED.")
        print(">> GAME OVER <<")

def get_name():
    name = input(">> What's your name, gladiator? (3-12 characters) ")
    while len(name) < 3 or len(name) > 12:
        long_or_short = "short" if len(name) < 3 else "long"
        name = input(f">> Name too {long_or_short}. Please try a longer name. (3-12 characters)")
    confirm = input(f">> Is your name {name}? (y/n) ").lower()
    confirm = validate(confirm, ["y", "n"])
    while confirm == "n":
        name = input(f">> What's your name? ")
        confirm = input(f">> Is your name {name}? (y/n) ").lower()
        confirm = validate(confirm, ["y", "n"])     
    return name
    
def validate(usr_input, choices):
    while usr_input not in choices:
        usr_input = input(f"Please input a valid option. ({[choice for choice in choices]}) ").lower()
    return usr_input

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = system('clear')

start()
