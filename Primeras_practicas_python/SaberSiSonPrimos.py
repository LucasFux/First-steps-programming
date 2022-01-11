#Programa para imprimir los numeros primo


''' def run():
    lista = []
    for i in range(101):
        for i2 in range(2,i):
            if ii2 == 0:
                continue

    print(lista) '''
def es_primo(num):
    contador=0
    for i in range(num):
        if i == 1 or i==0:
            continue
        elif num % i == 0:
            contador+=1
    if contador == 0:
        return True
    else:
        return False



def saber_primo():
    numero=int(input("Numero: "))
    if es_primo(numero):
        print(numero, "es primo")
    else:
        print(numero, "no es primo")

def imprimir_primos():
    lista = []
    for i in range(101):
        if es_primo(i):
            lista.append(i)
        else:
            continue
    print(lista)


if __name__ == "__main__":
    imprimir_primos()
    saber_primo()