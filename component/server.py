import asyncio
import websockets
import sqlite3
import json

# --------------------------------
# Inicializar la base de datos
# --------------------------------
def init_db():
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            direccion TEXT,
            mensaje TEXT
        )
    """)
    conn.commit()
    conn.close()

# --------------------------------
# Guardar datos en la DB
# --------------------------------
def guardar_datos(nombre, edad, direccion, mensaje):
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datos (nombre, edad, direccion, mensaje)
        VALUES (?, ?, ?, ?)
    """, (nombre, edad, direccion, mensaje))
    conn.commit()
    conn.close()

# --------------------------------
# Servidor WebSocket
# --------------------------------
async def handler(websocket):
    async for raw_data in websocket:
        try:
            data = json.loads(raw_data)

            nombre = data.get("nombre")
            edad = data.get("edad")
            direccion = data.get("direccion")
            mensaje = data.get("mensaje")

            guardar_datos(nombre, edad, direccion, mensaje)

            response = f"Datos guardados: {nombre}, {edad}, {direccion}, {mensaje}"
            await websocket.send(response)

        except Exception as e:
            await websocket.send("Error procesando datos: " + str(e))

async def main():
    init_db()
    async with websockets.serve(handler, "0.0.0.0", 8000):
        print("Servidor WebSocket escuchando en ws://0.0.0.0:8000")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
