# 08 - SQLite Basico
# Temas: crear tabla, insertar, consultar, actualizar, eliminar

import sqlite3

DB = "agenda.db"

def conectar():
    return sqlite3.connect(DB)

def crear_tabla():
    with conectar() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre  TEXT NOT NULL,
                telefono TEXT
            )
        """)

def insertar(nombre, telefono):
    with conectar() as con:
        con.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    print(f"Insertado: {nombre}")

def listar():
    with conectar() as con:
        rows = con.execute("SELECT id, nombre, telefono FROM contactos").fetchall()
    print(f"\n{'ID':<4} {'Nombre':<20} {'Telefono'}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<4} {row[1]:<20} {row[2]}")

def actualizar(id, nuevo_telefono):
    with conectar() as con:
        con.execute("UPDATE contactos SET telefono = ? WHERE id = ?", (nuevo_telefono, id))
    print(f"Telefono actualizado.")

def eliminar(id):
    with conectar() as con:
        con.execute("DELETE FROM contactos WHERE id = ?", (id,))
    print(f"Contacto {id} eliminado.")

# Uso
crear_tabla()
insertar("Sergio", "1234-5678")
insertar("Ana", "8765-4321")
insertar("Luis", "5555-0000")
listar()
actualizar(1, "9999-0000")
listar()
eliminar(3)
listar()
