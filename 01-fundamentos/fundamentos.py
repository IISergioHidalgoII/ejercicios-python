# 01 - Fundamentos
# Temas: variables, tipos de datos, input y print

nombre = "Sergio"
edad = 22
altura = 1.75
activo = True

print("=== Datos basicos ===")
print(f"Nombre:  {nombre}")
print(f"Edad:    {edad}")
print(f"Altura:  {altura} m")
print(f"Activo:  {activo}")
print(f"Tipo de 'edad': {type(edad)}")
print(f"Tipo de 'altura': {type(altura)}")

print("\n=== Entrada de usuario ===")
usuario = input("Como te llamas? ").strip()
print(f"Hola, {usuario}! Bienvenido a Python.")
