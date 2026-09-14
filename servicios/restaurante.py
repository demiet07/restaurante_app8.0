from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    """Proporciona las operaciones de negocio para la gestión de usuarios y productos."""

    def __init__(self, ruta_productos: str, ruta_usuarios: str):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.productos = []
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        # Cargar productos
        datos_prod = ArchivoServicio.leer_json(self.ruta_productos)
        self.productos = [
            Producto(
                id=p.get("id"),
                nombre=p.get("nombre"),
                precio=p.get("precio"),
                stock=p.get("stock"),
                categoria=p.get("categoria")
            ) for p in datos_prod
        ]

        # Cargar usuarios
        datos_user = ArchivoServicio.leer_json(self.ruta_usuarios)
        self.usuarios = [
            Usuario(
                username=u.get("username"),
                password=u.get("password"),
                nombre=u.get("nombre"),
                rol=u.get("rol")
            ) for u in datos_user
        ]

    def validar_acceso(self, username: str, password: str) -> Usuario | None:
        """Valida las credenciales del usuario simulando el acceso."""
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                return usuario
        return None

    def obtener_productos(self) -> list:
        return self.productos

    def obtener_usuarios(self) -> list:
        return self.usuarios