import random
import time
import os
import sys

def start():
    answer = input("Start game? (y/n) ").lower()
    validate(answer, ["y", "n"])
    if answer == "y":
        print("                                >> GAME STARTED <<                                ")
        time.sleep(1.3)
        print(">> welcome to <<SHOURI NO TSURUGI>>, a turn-based gladiator game where you climb your ways up in the tournament, can you win and be crowned champion of the collosseum?")
        print(">> in this game, there are 20 levels, each level there is a gladiator you have to fight. If you win - by reducing your opponent's HP to 0 - you advance to the next level. Each level your sword's strength and your HP increase and the same for your opponents.")
        start = True
    else:
        print(">> game closed")
        sys.exit()

    if start == True:    
        # Get name
        name = input(">> What's your name, gladiator? ")
        confirm = input(f">> Is your name {name}? (y/n) ").lower()
        validate(confirm, ["y", "n"])
        while confirm == "n":
            name = input(f">> What's your name? ")
            confirm = input(f">> Is your name {name}? (y/n) ").lower()
            validate(confirm, ["y", "n"])
        answer = input(f">> Gladiator {name}, are you ready? (y/n) ").lower()
        validate(answer, ["y", "n"])
        if answer == "y":
            clear()
            lvl_one()
        else:
            print("Coward.")

# This function will later be generalized for all levels. For now this is a test version.
# TODO: Add block for enemy, organize code, more fighting options, make it so the program doesn't print the attack log when one hp reaches 0.
def lvl_one():
    player_hp = 15
    flamma_hp = 15
    blocked = False
    print(">> FIGHT START <<")
    time.sleep(1)
    print(f">> LEVEL ONE - YOUR HP: {player_hp} - STRENGTH 5 <<")
    print(f">> GLADIATOR FLAMMA - {flamma_hp} HP - STRENGTH 5 <<")
   
    while player_hp > 0 and flamma_hp > 0:
        # Player's turn
        atk_block = input("""
        >> What will you do?
            > Attack (a)
            > Block (b) 
        """).lower()
        validate(atk_block, ["a", "b"])  
        if atk_block == "a":
            player_atk = random.randint(1, 5)
            print("YOU ATTACKED FLAMMA")
            time.sleep(1)
            print(f"YOUR ATTACK DEALT {player_atk} DAMAGE. FLAMMA'S HP WAS REDUCED FROM {flamma_hp} TO {flamma_hp-player_atk}")
            print("======================================================")
            flamma_hp -= player_atk
            time.sleep(1)
        else:
            block_chance = random.randint(0, 10)
            if block_chance <= 3:
                blocked = True            
        
        if blocked:
            print("FLAMMA TRIED TO ATTACK, BUT YOU BLOCK THE ATTACK!")
            blocked = False
            print("======================================================")
        
        # Enemy's turn
        else:
            flamma_atk = random.randint(1, 5)
            print("FLAMMA ATTACKED YOU")
            time.sleep(1)
            print(f"FLAMMA'S ATTACK DEALT {flamma_atk} DAMAGE. YOUR HP WAS REDUCED FROM {player_hp} to {player_hp-flamma_atk}")
            print("======================================================")
            player_hp -= flamma_atk
    
    if player_hp <= 0:
        print("YOU DIED.")
    else:
        print("YOU WON!")
            
    
def validate(usr_input, choices):
    while usr_input not in choices:
        usr_input = input(f"Please input a valid option. ({[choice for choice in choices]}) ").lower()

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = system('clear')

start()