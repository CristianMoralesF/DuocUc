# numero de la suerte con validacion
import random
inferior = int(input("Ingrese un limite inferior: "))
superior = int(input("Ingrese un limite superior: "))

if inferior > superior :
    inferior,superior = superior,inferior
    print("Se han invertido los valores para poder jugar ")

numero_suerte = random.randint(inferior,superior)
print(numero_suerte)

intento = int(input(f"Tienes un intento, adivina el numero de la suerte entre {inferior} y {superior}: "))
if intento == numero_suerte:
    print("Felicidades has acertado!! ")
else:
    print(f"No acertaste :C, el numero de la suerte era : {numero_suerte}.")