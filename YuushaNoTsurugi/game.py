import random
import time
import os
import sys

import db


level_data = db.level_data
name = None
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
        db.insert_player((name, 0))
        clear()
        lvl_start(1)
    else:
        print("Coward.")
        sys.exit()

def lvl_start(lvl):
    enemy_name = level_data[lvl]["enemy_name"]
    enemy_hp = level_data[lvl]["enemy_hp"]
    enemy_strength = 232323 #level_data[lvl]["enemy_strength"]
    player_hp = level_data[lvl]["player_hp"]
    player_strength = level_data[lvl]["player_strength"]
    winner = None
    start_time = time.time()
    
    print(">> FIGHT START <<")
    time.sleep(0.7)
    print(f">> LEVEL {lvl} - YOUR HP: {player_hp} - STRENGTH 5 <<")
    print(f">> GLADIATOR {enemy_name} - {enemy_hp} HP - STRENGTH 5 <<")
    
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
        end_time = time.time()
        play_time = start_time - end_time
        print(">> YOU WON! <<")
        if lvl == 10:
            print(">> CONGRATULATIONS. YOU ARE THE CHAMPION OF THE COLLOSSEUM! - TIME PLAYED: {play_time} <<")
            db.update_score(name)
            sys.exit()
        db.update_score(name)
        print(f"NEXT LEVEL: {lvl+1} - STARTING IN 3 SECONDS")
        time.sleep(3)
        clear()
        lvl_start(lvl+1)
    else:
        end_time = time.time()
        play_time = end_time - start_time
        print("YOU DIED.")
        print(f">> GAME OVER - SCORE {db.get_score(name)} - TIME PLAYED: {play_time}<<")

def get_name():
    name = input(">> What's your name, gladiator? (3-12 characters) ")
    existing_names = db.get_existing_names()
    while name in existing_names:
        name = input(">> Name already exists, please try another name: ")
    while len(name) < 3 or len(name) > 12:
        long_or_short = "short" if len(name) < 3 else "long"
        name = input(f">> Name too {long_or_short}. Please try another name. (3-12 characters)")
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
