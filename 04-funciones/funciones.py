# 04 - Funciones
# Temas: def, parametros, retorno, valores default, *args

def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

def sumar(*numeros):
    return sum(numeros)

def es_par(n):
    return n % 2 == 0

def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

# Uso
print(saludar("Sergio"))
print(saludar("Sergio", "Buenas tardes"))
print(f"Suma: {sumar(1, 2, 3, 4, 5)}")
print(f"Es par 8: {es_par(8)}")
print(f"Es par 7: {es_par(7)}")

notas = [85, 90, 78, 92, 88]
print(f"Promedio: {calcular_promedio(notas):.2f}")
