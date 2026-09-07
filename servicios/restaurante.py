# -*- coding: utf-8 -*-
"""
Proyecto: restaurante_app (Semana 12 - Optimización de Rendimiento)
Autor: Damian Ortega
Asignatura: Programación Orientada a Objetos
"""

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self, ruta_productos="datos/productos.json", 
                 ruta_usuarios="datos/usuarios.json", 
                 ruta_ventas="datos/ventas.json"):
        self.autor = "Damian Ortega"
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

        # Colecciones Principales (listas obligatorias)
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

        # Estructuras Auxiliares / Índices en Memoria para Rendimiento
        self._index_productos: dict[str, Producto] = {}
        self._index_usuarios: dict[str, Usuario] = {}
        self._index_ventas_usuario: dict[str, list[Venta]] = {}
        self._codigos_registrados: set[str] = set()

        self.cargar_datos()

    def _reconstruir_indices(self):
        """Reconstruye los índices desde las listas principales tras leer JSON."""
        self._index_productos = {p.codigo: p for p in self.productos}
        self._index_usuarios = {u.identificacion: u for u in self.usuarios}
        self._codigos_registrados = {p.codigo for p in self.productos}

        self._index_ventas_usuario = {}
        for v in self.ventas:
            if v.id_usuario not in self._index_ventas_usuario:
                self._index_ventas_usuario[v.id_usuario] = []
            self._index_ventas_usuario[v.id_usuario].append(v)

    def cargar_datos(self):
        datos_p = ArchivoServicio.cargar_json(self.ruta_productos)
        self.productos = [Producto.desde_dict(d) for d in datos_p]

        datos_u = ArchivoServicio.cargar_json(self.ruta_usuarios)
        self.usuarios = [Usuario.desde_dict(d) for d in datos_u]

        datos_v = ArchivoServicio.cargar_json(self.ruta_ventas)
        self.ventas = [Venta.desde_dict(d) for d in datos_v]

        self._reconstruir_indices()

    def guardar_datos(self):
        ArchivoServicio.guardar_json(self.ruta_productos, [p.a_dict() for p in self.productos])
        ArchivoServicio.guardar_json(self.ruta_usuarios, [u.a_dict() for u in self.usuarios])
        ArchivoServicio.guardar_json(self.ruta_ventas, [v.a_dict() for v in self.ventas])

    # --- CONSULTAS OPTIMIZADAS ---
    def buscar_producto(self, codigo: str) -> Producto | None:
        return self._index_productos.get(codigo)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        return self._index_usuarios.get(identificacion)

    def obtener_ventas_usuario(self, identificacion: str) -> list[Venta]:
        return self._index_ventas_usuario.get(identificacion, [])

    # --- OPERACIONES CON SINCRONIZACIÓN DE ÍNDICES ---
    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        if codigo in self._codigos_registrados:
            return False
        
        nuevo_p = Producto(codigo, nombre, precio, stock)
        self.productos.append(nuevo_p)
        
        self._index_productos[codigo] = nuevo_p
        self._codigos_registrados.add(codigo)
        self.guardar_datos()
        return True

    def registrar_usuario(self, identificacion: str, nombre: str, email: str) -> bool:
        if identificacion in self._index_usuarios:
            return False
        
        nuevo_u = Usuario(identificacion, nombre, email)
        self.usuarios.append(nuevo_u)
        
        self._index_usuarios[identificacion] = nuevo_u
        self.guardar_datos()
        return True

    def registrar_venta(self, id_venta: str, id_usuario: str, codigo_producto: str, cantidad: int) -> tuple[bool, str]:
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            return False, "Error: Usuario no registrado."

        producto = self.buscar_producto(codigo_producto)
        if not producto:
            return False, "Error: Producto no registrado."

        if producto.stock < cantidad:
            return False, f"Error: Stock insuficiente. Stock actual: {producto.stock}"

        producto.stock -= cantidad
        total = producto.precio * cantidad

        nueva_venta = Venta(id_venta, id_usuario, codigo_producto, cantidad, total)
        self.ventas.append(nueva_venta)

        if id_usuario not in self._index_ventas_usuario:
            self._index_ventas_usuario[id_usuario] = []
        self._index_ventas_usuario[id_usuario].append(nueva_venta)

        self.guardar_datos()
        return True, f"Venta {id_venta} registrada exitosamente. Total: ${total:.2f}"