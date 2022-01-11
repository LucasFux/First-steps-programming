print("PROGRAMA PARA SABER SI UN NUMERO ES PAR O NO \n")

numero = int(input("Que numero elegiste? "))
resultado = numero % 2
if resultado == 0:
    print("El numero", numero, "es par")
else:
    print("El numero", numero, "es impar")
print(resultado)
print("Final del programa")
