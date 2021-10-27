def encode(message:str, shift: int):
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

print(encode("abcz", 1))
