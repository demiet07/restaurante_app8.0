class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        if not identificacion or not nombre or not correo:
            raise ValueError("Todos los campos del usuario son obligatorios.")

        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Usuario':
        try:
            return Usuario(
                identificacion=str(datos["identificacion"]),
                nombre=str(datos["nombre"]),
                correo=str(datos["correo"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida en el JSON de Usuario: {e}")