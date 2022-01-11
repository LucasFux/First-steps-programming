#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es
# el día tiene un descuento del 60%. Escribir un programa que comience leyendo el 
# número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de 
# una barra de pan, el descuento que se le 
# hace por no ser fresca y el coste final total.

frase= "Hola esto es una prueba"
i=0
while i < len(frase):
    if str(frase[i]) == "s":
        i+=1
        continue
    print(frase[i])
    i+=1
    if str(frase[i]) == "r":
        break