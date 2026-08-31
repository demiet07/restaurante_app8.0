from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    RUTA_PRODUCTOS = "datos/productos.json"
    RUTA_USUARIOS = "datos/usuarios.json"
    RUTA_VENTAS = "datos/ventas.json"

    def __init__(self):
        self._productos: List[Producto] = ArchivoServicio.cargar_productos(self.RUTA_PRODUCTOS)
        self._usuarios: List[Usuario] = ArchivoServicio.cargar_usuarios(self.RUTA_USUARIOS)
        self._ventas: List[Venta] = ArchivoServicio.cargar_ventas(self.RUTA_VENTAS)

    # --- BÚSQUEDAS ---
    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for prod in self._productos:
            if prod.codigo == codigo:
                return prod
        return None

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usr in self._usuarios:
            if usr.identificacion == identificacion:
                return usr
        return None

    # --- REGISTROS ---
    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        if self.buscar_producto(codigo) is not None:
            print("El producto con este código ya existe.")
            return False
        nuevo_producto = Producto(codigo, nombre, precio, stock)
        self._productos.append(nuevo_producto)
        ArchivoServicio.guardar_datos(self.RUTA_PRODUCTOS, self._productos)
        return True

    def registrar_usuario(self, identificacion: str, nombre: str, correo: str) -> bool:
        if self.buscar_usuario(identificacion) is not None:
            print("El usuario con esta identificación ya existe.")
            return False
        nuevo_usuario = Usuario(identificacion, nombre, correo)
        self._usuarios.append(nuevo_usuario)
        ArchivoServicio.guardar_datos(self.RUTA_USUARIOS, self._usuarios)
        return True

    # --- OPERACIÓN DE VENTA ---
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None:
            print("Error: El usuario especificado no existe.")
            return False

        if producto is None:
            print("Error: El producto especificado no existe.")
            return False

        if cantidad <= 0:
            print("Error: La cantidad solicitada debe ser mayor a cero.")
            return False

        if producto.stock < cantidad:
            print(f"Error: Stock insuficiente. Stock disponible: {producto.stock}")
            return False

        # Registrar la venta y actualizar stock
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)

        # Persistir cambios
        ArchivoServicio.guardar_datos(self.RUTA_VENTAS, self._ventas)
        ArchivoServicio.guardar_datos(self.RUTA_PRODUCTOS, self._productos)
        return True

    # --- CONSULTAS ---
    def consultar_ventas_usuario(self, identificacion_usuario: str) -> List[dict]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if not usuario:
            print("Error: Usuario no encontrado.")
            return []

        ventas_usuario = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                producto = self.buscar_producto(venta.producto_codigo)
                nombre_prod = producto.nombre if producto else "Producto no disponible"
                ventas_usuario.append({
                    "producto_codigo": venta.producto_codigo,
                    "producto_nombre": nombre_prod,
                    "cantidad": venta.cantidad
                })
        return ventas_usuario

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self._usuarios