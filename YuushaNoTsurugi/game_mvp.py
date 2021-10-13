import random
import time
import os
import sys

level_data = {
    1: {
        "enemy_name": "FLAMMA",
        "enemy_hp": 15,
        "player_hp": 15,
        "enemy_strength": 5,
        "player_strength": 5
    },
    2: {
        "enemy_name": "SPICULUS",
        "enemy_hp": 20,
        "player_hp": 20,
        "enemy_strength": 8,
        "player_strength": 9
    },
    3: {
        "enemy_name": "TETRAITES",
        "enemy_hp": 25,
        "player_hp": 23,
        "enemy_strength": 10,
        "player_strength": 11
    },
    4: {
        "enemy_name": "CARPOPHORUS",
        "enemy_hp": 30,
        "player_hp": 25,
        "enemy_strength": 11,
        "player_strength": 13
    },
    5: {
        "enemy_name": "PRISCUS",
        "enemy_hp": 35,
        "player_hp": 32,
        "enemy_strength": 14,
        "player_strength": 15
    },
    6: {
        "enemy_name": "VERUS",
        "enemy_hp": 40,
        "player_hp": 40,
        "enemy_strength": 19,
        "player_strength": 16
    },
    7: {
        "enemy_name": "ATTILIUS",
        "enemy_hp": 45,
        "player_hp": 42,
        "enemy_strength": 20,
        "player_strength": 18
    },
    8: {
        "enemy_name": "THRAEX",
        "enemy_hp": 50,
        "player_hp": 45,
        "enemy_strength": 23,
        "player_strength": 20
    },
    9: {
        "enemy_name": "MYRMILLO",
        "enemy_hp": 60,
        "player_hp": 48,
        "enemy_strength": 25,
        "player_strength": 23
    },
    10: {
        "enemy_name": "SPARTACUS",
        "enemy_hp": 80,
        "player_hp": 55,
        "enemy_strength": 30,
        "player_strength": 25
    }
}

def start():
    print(">> GAME STARTED <<\n")
    time.sleep(1.3)
    print(">> welcome to <<SHOURI NO TSURUGI>>, a turn-based gladiator game where you climb your way up in the legendary collosseum tournament, can you win and be crowned champion of the collosseum?\n")
    time.sleep(1)
    print(">> in this game, there are 10 levels, each level there is a gladiator you have to fight. If you win - by reducing your opponent's HP to 0 - you advance to the next level. Each level your sword's strength and your HP increase and the same for your opponents.\n")
    name = get_name()
    global current_player_name
    current_player_name = name
    answer = input(f">> Gladiator {name}, are you ready? (y/n) ").lower()
    answer = validate(answer, ["y", "n"])
    if answer == "y":
        clear()
        lvl_start(1)
    else:
        print("Coward.")
        sys.exit()

def lvl_start(lvl):
    enemy_name = level_data[lvl]["enemy_name"]
    enemy_hp = level_data[lvl]["enemy_hp"]
    enemy_strength = level_data[lvl]["enemy_strength"]
    player_hp = level_data[lvl]["player_hp"]
    player_strength = level_data[lvl]["player_strength"]
    winner = None
    start_time = time.time()
    
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
        lvl += 1
        print(">> YOU WON! <<")
        if lvl == 11:
            print(f">> CONGRATULATIONS. YOU ARE THE CHAMPION OF THE COLLOSSEUM! <<")
            sys.exit()
        print(f"Score: {lvl-1}")
        print(f"NEXT LEVEL: {lvl} - STARTING IN 3 SECONDS")
        time.sleep(3)
        clear()
        lvl_start(lvl)
    else:
        end_time = time.time()
        print("YOU DIED.")
        print(f">> GAME OVER - SCORE {lvl}<<")

def get_name():
    uname = input(">> What's your name, gladiator? (3-12 characters, only letters or numbers): ")
    while not uname.isalnum():
        uname = input(">> Please only use letters or numbers in your name: ")
    while len(uname) < 3 or len(uname) > 12:
        long_or_short = "short" if len(uname) < 3 else "long"
        uname = input(f">> Name too {long_or_short}. Please try another name. (3-12 characters): ")   
    return uname
    
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
