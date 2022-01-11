import random


def generate_password():
    CAPITAL_LETTERS =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    LOWERCASE =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SIMBOLS = ['*', '+', '-', '/', '@', '_', '?', '!', ',',';', '.', '>', '<', '~', '°', '^', '&', '$', '#']
    CHARACTERS = CAPITAL_LETTERS + LOWERCASE + NUMS + SIMBOLS
    password = []
    for i in range(15):
        random_character = random.choice(CHARACTERS)
        password.append(random_character)
    password=''.join(password)
    return password






def run():
    password= generate_password()
    print("La nueva contraseña es: ", password)


if __name__ == "__main__":
    run()