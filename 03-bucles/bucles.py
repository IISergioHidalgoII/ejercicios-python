# 03 - Bucles
# Temas: for, while, break, continue, range

print("=== For con range ===")
for i in range(1, 6):
    print(f"  Iteracion {i}")

print("\n=== While con condicion ===")
contador = 0
while contador < 3:
    print(f"  Contador: {contador}")
    contador += 1

print("\n=== For con break y continue ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numeros:
    if n % 2 == 0:
        continue        # saltar pares
    if n > 7:
        break           # detener en mayores a 7
    print(f"  Impar: {n}")

print("\n=== Acumulador ===")
total = sum(range(1, 101))
print(f"  Suma del 1 al 100: {total}")
