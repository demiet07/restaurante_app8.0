import json
import os

class ArchivoServicio:
    """Encargado exclusivamente de la lectura de archivos locales en formato JSON."""

    @staticmethod
    def leer_json(ruta_archivo: str) -> list:
        if not os.path.exists(ruta_archivo):
            return []
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, IOError):
            return []