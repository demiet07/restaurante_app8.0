class Usuario:
    def __init__(self, identificacion: str, nombre: str, email: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.email = email

    def a_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "email": self.email
        }

    @staticmethod
    def desde_dict(datos: dict) -> "Usuario":
        return Usuario(datos["identificacion"], datos["nombre"], datos["email"])