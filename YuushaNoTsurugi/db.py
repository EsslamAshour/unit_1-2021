import sqlite3 

conn = sqlite3.connect("player_data.db")
cursor = conn.cursor()

def insert_player(data):
    cursor.execute("INSERT INTO players VALUES (?, ?)", data)
    conn.commit()

def update_score(name):
    cursor.execute("UPDATE players set score = score + 1 where name = ?", (name,))
    conn.commit()

def get_score(name):
    score = cursor.execute("SELECT score FROM players WHERE name = ?", (name,)).fetchone()
    return score

def get_existing_names():
    names_list = []
    names_tuples = cursor.execute("SELECT name FROM players").fetchall()
    for tup in names_tuples:
        for name in tup:
            names_list.append(name)
    return names_list


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