def validate(usr_input: str, choices: list):
    """
    Validate any input from the user given the valid choices and prompt the user to input again if invalid.
    """
    while usr_input not in choices:
        usr_input = input(f"Please input a valid option. ({[choice for choice in choices]}) ").lower()
    return usr_input

validate(usr_input="a", choices=["b", "c"])