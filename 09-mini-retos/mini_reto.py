# 09 - Mini Reto
# Reto: sistema de calificaciones que combina funciones, listas, diccionarios y archivos
# Permite registrar alumnos con notas, calcular promedios y guardar el reporte en un .txt

import os

ARCHIVO = "reporte.txt"

def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

def obtener_estado(promedio):
    if promedio >= 90:
        return "Excelente"
    elif promedio >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

def registrar_alumno(alumnos):
    nombre = input("Nombre del alumno: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    try:
        notas = []
        for i in range(1, 4):
            nota = float(input(f"  Nota {i} (0-100): "))
            notas.append(max(0, min(100, nota)))
        alumnos[nombre] = notas
        print(f"Alumno '{nombre}' registrado.")
    except ValueError:
        print("Nota invalida.")

def mostrar_reporte(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    print(f"\n{'Alumno':<20} {'Promedio':<10} {'Estado'}")
    print("-" * 40)
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        estado = obtener_estado(promedio)
        print(f"{nombre:<20} {promedio:<10.2f} {estado}")

def guardar_reporte(alumnos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("=== Reporte de Calificaciones ===\n\n")
        for nombre, notas in alumnos.items():
            promedio = calcular_promedio(notas)
            estado = obtener_estado(promedio)
            f.write(f"{nombre}: promedio {promedio:.2f} - {estado}\n")
    print(f"Reporte guardado en '{ARCHIVO}'.")

def mostrar_menu():
    print("\n===== Sistema de Calificaciones =====")
    print("1. Registrar alumno")
    print("2. Ver reporte")
    print("3. Guardar reporte en archivo")
    print("4. Salir")
    print("=====================================")

def main():
    alumnos = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "1":
            registrar_alumno(alumnos)
        elif opcion == "2":
            mostrar_reporte(alumnos)
        elif opcion == "3":
            guardar_reporte(alumnos)
        elif opcion == "4":
            print("Bye!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
