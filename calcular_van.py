print("\t\t*** Calculo del VAN ***")
suma = 0
lista = []
inversion = int(input("Ingrese la inversión: ")) * -1
desc = (int(input("Ingrese la Taza de descuento: ")) / 100)
cantMeses = int(input("Ingrese la cantidad de meses: "))

for item in range(cantMeses):
    importe = int(input(f"Ingrese el importe del mes {item + 1}: "))
    cadena = (f" {importe} / (1 + {desc})^{item + 1} ")
    lista.append(cadena)
    if importe != 0: aux = importe/ (1 + desc)**(item + 1)
    else:aux = 0 
    suma += round(aux,2)
    
van = inversion + suma
formula = '+'.join(lista)
print(f"La formula completa es {inversion} + {formula}")
print(f"El van es {round(van,2)}")




    


