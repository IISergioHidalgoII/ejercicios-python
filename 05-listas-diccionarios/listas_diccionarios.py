# 05 - Listas y Diccionarios
# Temas: operaciones con listas, dicts, comprension de listas

# --- Listas ---
frutas = ["manzana", "pera", "uva"]
frutas.append("mango")
frutas.remove("pera")
print(f"Frutas: {frutas}")
print(f"Primera: {frutas[0]}, Ultima: {frutas[-1]}")

# Comprension de lista
cuadrados = [x ** 2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# --- Diccionarios ---
persona = {"nombre": "Sergio", "edad": 22, "ciudad": "GT"}
persona["correo"] = "sergio@correo.com"
persona.pop("ciudad")

print(f"\nPersona: {persona}")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# Dict por comprension
cuadrados_dict = {x: x ** 2 for x in range(1, 6)}
print(f"\nCuadrados dict: {cuadrados_dict}")
