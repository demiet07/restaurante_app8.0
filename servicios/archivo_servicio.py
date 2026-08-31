import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    @staticmethod
    def _asegurar_directorio(ruta_archivo: str) -> None:
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

    @staticmethod
    def guardar_datos(ruta_archivo: str, coleccion: list) -> None:
        try:
            ArchivoServicio._asegurar_directorio(ruta_archivo)
            datos_dict = [obj.a_diccionario() for obj in coleccion]
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos_dict, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print(f"Error de permisos: No se puede escribir en el archivo {ruta_archivo}.")
        except Exception as e:
            print(f"Error inesperado al guardar datos en {ruta_archivo}: {e}")

    @staticmethod
    def cargar_productos(ruta_archivo: str) -> List[Producto]:
        productos = []
        if not os.path.exists(ruta_archivo):
            return productos
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    productos.append(Producto.desde_diccionario(item))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Advertencia: El archivo {ruta_archivo} contiene un JSON inválido. Se iniciará colección vacía.")
        except (KeyError, ValueError) as e:
            print(f"Error en la estructura de los datos de productos: {e}")
        except PermissionError:
            print(f"Error de permisos al leer {ruta_archivo}.")
        return productos

    @staticmethod
    def cargar_usuarios(ruta_archivo: str) -> List[Usuario]:
        usuarios = []
        if not os.path.exists(ruta_archivo):
            return usuarios
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    usuarios.append(Usuario.desde_diccionario(item))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Advertencia: El archivo {ruta_archivo} contiene un JSON inválido. Se iniciará colección vacía.")
        except (KeyError, ValueError) as e:
            print(f"Error en la estructura de los datos de usuarios: {e}")
        except PermissionError:
            print(f"Error de permisos al leer {ruta_archivo}.")
        return usuarios

    @staticmethod
    def cargar_ventas(ruta_archivo: str) -> List[Venta]:
        ventas = []
        if not os.path.exists(ruta_archivo):
            return ventas
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    ventas.append(Venta.desde_diccionario(item))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Advertencia: El archivo {ruta_archivo} contiene un JSON inválido. Se iniciará colección vacía.")
        except (KeyError, ValueError) as e:
            print(f"Error en la estructura de los datos de ventas: {e}")
        except PermissionError:
            print(f"Error de permisos al leer {ruta_archivo}.")
        return ventas