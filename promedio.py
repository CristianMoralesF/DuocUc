nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio_presentacion_final = (nota1 * 0.3) + (nota2 * 0.4) + (nota3 * 0.3)
print(f"El promedio final es: {promedio_presentacion_final:.1f}")

nota_Examen = float(input("Ingrese la nota de examen : "))
promedio_Final = (nota_Examen * 0.4) + (promedio_presentacion_final * 0.6)
print(f"El promedio final es: {promedio_Final}")