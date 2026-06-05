# 02 - Condicionales
# Temas: if, elif, else con caso real

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad no valida.")
elif edad < 13:
    print("Eres un nino.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")

# Operador ternario
acceso = "permitido" if edad >= 18 else "denegado"
print(f"Acceso: {acceso}")
