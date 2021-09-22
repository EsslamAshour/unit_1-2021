inv = []
def start():
    print("--------------------------------------------GAME START--------------------------------------------")
    print("""
    It's the year 2329. 200 years ago, a great plague turned more than 90% of the earth's population into undead beasts known as the Fujimi. You're one of the very few survivors who are struggling to find shelter, food and water while protecting themselves from Fujimi. But they are not the only enemy, as most humans have abandoned their morals and beliefs and would do anything to survive, and that includes killing other humans. Wild animals - known as the Yajuu - were not affected by this plague.
    """)
    
    tutorial_q = input("Would you like to view the tutorial before starting? (y/n)")
    validate(tutorial_q, ["y", "n"])
    if tutorial_q == "y":
        tutorial()
    
    # Getting name from user
    name = input("What's your name? ")
    confirm = input(f"Is your name {name}? (y/n) ")
    validate(confirm, ["y", "n"])
    while confirm == "n":
        name = input(f"What's your name? ")
        confirm = input(f"Is your name {name}? (y/n) ")
        validate(confirm, ["y", "n"])
    

def tutorial():
    print(""""
    Welcome to Sekai no Owari, a turn-based post-apocalyptic game. In this game, you're a human trying to survive as long as possible, avoiding getting eaten by the undead, killed by humans or wild animals.
    This game uses a choice system where, for example, you choose which place to go to, or how to deal with an enemy. There are different places like abandoned houses, shops, etc. When entering a place you risk the chance of encountering an enemy in exchange of possibly finding useful items like weapons, food or water. When you encounter an enemy you can choose to run or fight, running will not always result in you safely escaping away. Fights are turn-based, you use your weapons - or your body if you have none - to fight the enemy until their HP (Health Points) becomes 0, if your HP becomes 0 you die. You can consume food after fights to recover your HP.
    """)
    print("===========================================================================================") 

def test_room():
    print("You wake up in the abandonded house you decided to stay at last night, the sun is just starting to rise.")
    choose_action()

def choose_action(next_place=None):
    print("What will you do?")
    action = input((""""
    - Move (m)
    - Open inventory (i)
    """)).lower()
    validate(action, ["m", "i"])
    if action == "m":
        next_place()
    else:
        inventory()
        pass

def inventory():
    print("------------------INVENTORY------------------")
    for item in inv:
        print(f"- {item} ")
        




def validate(usr_input, choices):
    while usr_input not in choices:
        usr_input = input(f"Please input a valid option. ({[choice for choice in choices]}) ").lower()


start()