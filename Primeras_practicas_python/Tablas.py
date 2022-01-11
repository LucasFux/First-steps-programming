def tablas(): 
    numero = int(input("¿La tabla de que numero deseas ver? "))
    for i in range(11):
        print(numero, "x", i, "=", i * numero)


def run():
    tablas()

if __name__ == "__main__":
    run()