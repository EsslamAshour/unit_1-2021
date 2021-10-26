"""
    File name: db.py
    Author: Esslam Ashour
    Date created: 26/9/2021
    Python Version: 3.9.6 
"""

import sqlite3 

conn = sqlite3.connect("player_data.db")
cursor = conn.cursor()
caesar_shift = 3

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    name TEXT NOT NULL,
    score INTEGER NOT NULL,
    time_played INTEGER NOT NULL 
)
""")

def encode(message:str, shift=caesar_shift):
    """
    Function to implement the caesar cipher.
    """
    encoded_message = ''
    for i in range(len(message)):
        letter = message[i]
        letter_code = ord(letter)
        shifted_code = letter_code + shift
        if (shifted_code > 122 and letter.islower()) or (shifted_code > 90 and letter.isupper()):
            shifted_code -= 26
        encoded_message += chr(shifted_code)
    return encoded_message

def decode(message: str, shift=caesar_shift):
    """
    Function to decrypt caesar cipher
    """
    decoded_message = ''
    for i in range(len(message)):
        letter = message[i]
        letter_code = ord(letter)
        shifted_code = letter_code - shift
        if (letter.islower() and shifted_code < 96) or (letter.isupper() and shifted_code < 65):
            shifted_code += 26
        decoded_message += chr(shifted_code)
    return decoded_message    

def insert_player(name: str):
    """
    Insert player name and initial score, time_played values (0, 0)
    """
    cursor.execute("INSERT INTO players VALUES (?, ?, ?)", (encode(name), 0, 0))
    conn.commit()

def update_score(name: str):
    """
    Increase score by one given name
    """
    cursor.execute("UPDATE players set score = score + 1 where name = ?", (encode(name),))
    conn.commit()

def update_time_played(name: int, time: float):
    """
    Update time_played given name
    """
    cursor.execute("UPDATE players set time_played = ? where name = ?", (time, encode(name)))

def get_score(name: str):
    """
    Get the score of a player given name
    """
    score = cursor.execute("SELECT score FROM players WHERE name = ?", (encode(name),)).fetchone()[0]
    return score

def get_existing_names():
    """
    Get all names stored in the database
    """
    names_list = []
    names_tuples = cursor.execute("SELECT name FROM players").fetchall()
    for tup in names_tuples:
        for name in tup:
            names_list.append(decode(name))
    return names_list

# Data for each level from 1 - 10
level_data = {
    1: {
        "enemy_name": "FLAMMA",
        "enemy_hp": 15,
        "player_hp": 15,
        "enemy_strength": 5,
        "player_strength": 213
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