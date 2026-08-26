estatura = int(input("ingrese su estatura: "))
edad = int(input("ingrese su edad: "))

if edad >= 15 and edad <= 18:
    if estatura > 180:
        print("beca completa")
    elif estatura >= 170 and estatura < 180:
        print("media beca")
    else:
        print("sin beneficios por ahora")
else:
    print("sin beneficios por ahora")