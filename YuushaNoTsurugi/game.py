import random
import time
import os
import sys

import db


level_data = db.level_data

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
        db.insert_player(name)
        clear()
        lvl_start(1, name)
    else:
        print("Coward.")
        sys.exit()

def lvl_start(lvl, current_player_name):
    enemy_name = level_data[lvl]["enemy_name"]
    enemy_hp = level_data[lvl]["enemy_hp"]
    enemy_strength = level_data[lvl]["enemy_strength"]
    player_hp = level_data[lvl]["player_hp"]
    player_strength = 23232 #level_data[lvl]["player_strength"]
    winner = None
    
    print(">> FIGHT START <<")
    time.sleep(0.7)
    print(f">> LEVEL {lvl} - YOUR HP: {player_hp} - STRENGTH {enemy_strength} <<")
    print(f">> GLADIATOR {enemy_name} - {enemy_hp} HP - STRENGTH {player_strength} <<")
    
    while player_hp > 0 and enemy_hp > 0:
        # Player's turn
        atk_prompt = input("""
        >> PRESS a TO ATTACK
        """).lower()
        atk_prompt = validate(atk_prompt, ["a"])  
        player_atk = random.randint(1, player_strength)
        print(f"YOU ATTACKED {enemy_name}")
        time.sleep(0.7)
        print(f"YOUR ATTACK DEALT {player_atk} DAMAGE. {enemy_name}'S HP WAS REDUCED FROM {enemy_hp} TO {enemy_hp-player_atk}\n")
        enemy_hp -= player_atk
        if enemy_hp <= 0:
            winner = "player"
            break
        time.sleep(1)
        
        # Enemy turn
        enemy_atk = random.randint(1, enemy_strength)
        print(f"{enemy_name} ATTACKED YOU")
        time.sleep(0.7)
        print(f"{enemy_name}'S ATTACK DEALT {enemy_atk} DAMAGE. YOUR HP WAS REDUCED FROM {player_hp} to {player_hp-enemy_atk}\n")        
        player_hp -= enemy_atk
        if player_hp <= 0:
            winner = "enemy"
            break
                
    if winner == "player":
        print(">> YOU WON! <<")
        if lvl == 10:
            print(">> CONGRATULATIONS. YOU ARE THE CHAMPION OF THE COLLOSSEUM! <<")
            db.update_score(current_player_name)
            sys.exit()
        db.update_score(current_player_name)
        print(f"Score: {db.get_score(current_player_name)}")
        print(f"NEXT LEVEL: {lvl+1} - STARTING IN 3 SECONDS")
        time.sleep(3)
        clear()
        lvl_start(lvl+1, current_player_name)
    else:
        print("YOU DIED.")
        print(f">> GAME OVER - SCORE {db.get_score(current_player_name)} <<")

def get_name():
    name = input(">> What's your name, gladiator? (3-12 characters, only letters or numbers): ")
    existing_names = db.get_existing_names()
    while not name.isalnum():
        name = input(">> Please only use letters or numbers in your name: ")
    while name in existing_names:
        name = input(">> Name already exists, please try another name: ")
    while len(name) < 3 or len(name) > 12:
        long_or_short = "short" if len(name) < 3 else "long"
        name = input(f">> Name too {long_or_short}. Please try another name. (3-12 characters): ")   
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