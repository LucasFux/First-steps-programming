import random

def run():
    numero= random.randint(1,100)
    user=0
    while numero != user:
        user = int(input("Adivina el numero: "))
        if numero == user:
            print("ACERTASTE")
        elif numero < user:
            print("El numero es mas bajo")
        else:
            print("El numero es mas alto")



if __name__ == "__main__":
    run()