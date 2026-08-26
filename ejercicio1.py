descuento = 0
valor_base = 0
edad = int(input("ingrese su edad: "))
sueldo_base = int(input("ingres su sueldo base: "))
if edad > 65:
    descuento = 0.2
elif edad >= 18 and edad <= 64:
    descuento = 0.05
else:
    descuento = 0
    if sueldo_base < 500000:
        descuento = descuento + 0.1
valor_final = valor_base - (valor_base * descuento)
print(f"el valor final = {valor_final}")