import sqlite3

def conectar():
    return sqlite3.connect("ibex.db")

def criar_tabelas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()