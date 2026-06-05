# 07 - POO Basica
# Temas: clase, atributos, metodos, __init__, __str__

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - Q{self.precio:.2f} (stock: {self.stock})"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"Stock insuficiente. Disponible: {self.stock}")
        else:
            self.stock -= cantidad
            print(f"Venta exitosa. Stock restante: {self.stock}")

# Uso
p1 = Producto("Teclado", 250.00, 10)
p2 = Producto("Mouse", 150.00, 5)

print(p1)
print(p2)

p1.aplicar_descuento(10)
print(f"\nDespues de descuento: {p1}")

p2.vender(3)
p2.vender(5)
print(p2)
