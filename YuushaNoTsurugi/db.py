import sqlite3 

conn = sqlite3.connect("player_data.db")
cursor = conn.cursor()
caesar_shift = 3

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    name TEXT,
    score INTEGER DEFAULT 0,
    time_played INTEGER NOT NULL DEFAULT 0 
)
""")


def insert_player(name):
    cursor.execute("INSERT INTO players VALUES (?, ?, ?)", (encode(name), 1213, 0))
    conn.commit()

def update_score(name):
    cursor.execute("UPDATE players set score = score + 1 where name = ?", (encode(name),))
    conn.commit()

def get_score(name):
    score = cursor.execute("SELECT score FROM players WHERE name = ?", (decode(name),)).fetchone()
    return score

def get_existing_names():
    names_list = []
    names_tuples = cursor.execute("SELECT name FROM players").fetchall()
    for tup in names_tuples:
        for name in tup:
            names_list.append(decode(name))
    return names_list

def encode(message, shift=caesar_shift):
    encoded_message = ''
    for i in range(len(message)):
        letter = message[i]
        letter_code = ord(letter)
        shifted_code = letter_code + shift
        if (shifted_code > 122 and letter.islower()) or (shifted_code > 90 and letter.isupper()):
            shifted_code -= 26
        encoded_message += chr(shifted_code)
    return encoded_message

def decode(message, shift=caesar_shift):
    decoded_message = ''
    for i in range(len(message)):
        letter = message[i]
        letter_code = ord(letter)
        shifted_code = letter_code - shift
        if (letter.islower() and shifted_code < 96) or (letter.isupper() and shifted_code < 65):
            shifted_code += 26
        decoded_message += chr(shifted_code)
    return decoded_message    

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