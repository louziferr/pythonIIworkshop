
def get_lettermap():
    letter_map = dict()
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    len_alphabet = len(alphabet)
    for i in range(len_alphabet):
        old_letter = alphabet[i]
        new_letter = alphabet[(i+13)%len_alphabet]
        letter_map[old_letter] = new_letter
    return letter_map


def encrypt(message):
    lettermap = get_lettermap()
    message = message.lower()
    encrypted_message = ""
    for letter in message:
        if letter in lettermap:
            encrypted_message += lettermap[letter]
        else:
            encrypted_message += letter
    return encrypted_message


def decrypt(message):
    lettermap = get_lettermap()
    lettermap = {v: k for k, v in lettermap.items()}
    decrypted_message = ""
    for letter in message:
        if letter in lettermap:
            decrypted_message += lettermap[letter]
        else:
            decrypted_message += letter
    return decrypted_message