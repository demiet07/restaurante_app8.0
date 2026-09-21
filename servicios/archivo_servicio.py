import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta):
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except Exception:
            return []

    @staticmethod
    def escribir_json(ruta, datos):
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al escribir el archivo: {e}")