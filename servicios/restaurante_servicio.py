from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.ruta_productos = "datos/productos.json"
        self.ruta_usuarios = "datos/usuarios.json"
        self.productos = self.cargar_productos()
        self.usuarios = self.cargar_usuarios()

    def cargar_productos(self):
        datos = ArchivoServicio.leer_json(self.ruta_productos)
        return [Producto(**item) for item in datos] if datos else []

    def guardar_productos(self):
        datos = [p.a_diccionario() for p in self.productos]
        ArchivoServicio.escribir_json(self.ruta_productos, datos)

    def cargar_usuarios(self):
        datos = ArchivoServicio.leer_json(self.ruta_usuarios)
        return [Usuario(**item) for item in datos] if datos else []

    def validar_login(self, username, password):
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return True
        return False

    def obtener_usuarios(self):
        return self.usuarios

    def registrar_producto(self, id_prod, nombre, precio, stock):
        if not id_prod or not nombre or not precio or not stock:
            raise ValueError("Todos los campos del producto son obligatorios.")
        
        for p in self.productos:
            if p.id_prod == id_prod:
                raise ValueError("El ID del producto ya se encuentra registrado.")
                
        nuevo = Producto(id_prod, nombre, float(precio), int(stock))
        self.productos.append(nuevo)
        self.guardar_productos()

    def obtener_productos(self):
        return self.productos

    def actualizar_producto(self, id_prod, nombre, precio, stock):
        for p in self.productos:
            if p.id_prod == id_prod:
                p.nombre = nombre
                p.precio = float(precio)
                p.stock = int(stock)
                self.guardar_productos()
                return True
        raise ValueError("No se encontró un producto con ese ID para actualizar.")

    def eliminar_producto(self, id_prod):
        for p in self.productos:
            if p.id_prod == id_prod:
                self.productos.remove(p)
                self.guardar_productos()
                return True
        raise ValueError("No se encontró un producto con ese ID para eliminar.")