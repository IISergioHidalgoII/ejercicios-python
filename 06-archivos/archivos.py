# 06 - Archivos
# Temas: escribir, leer y agregar contenido a archivos de texto

ARCHIVO = "notas.txt"

# Escribir
with open(ARCHIVO, "w", encoding="utf-8") as f:
    f.write("Nota 1: Aprender Python\n")
    f.write("Nota 2: Practicar con proyectos\n")
    f.write("Nota 3: Subir al portafolio\n")

print("Archivo escrito.")

# Leer completo
print("\n=== Contenido del archivo ===")
with open(ARCHIVO, "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# Agregar linea
with open(ARCHIVO, "a", encoding="utf-8") as f:
    f.write("Nota 4: Seguir aprendiendo\n")

# Leer linea por linea
print("=== Linea por linea ===")
with open(ARCHIVO, "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, 1):
        print(f"  {i}: {linea.strip()}")
