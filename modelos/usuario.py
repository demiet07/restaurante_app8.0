class Usuario:
    def __init__(self, id=None, id_usuario=None, username="", nombre="", rol="", password="", **kwargs):
        self.id_usuario = id_usuario if id_usuario is not None else id
        # Mapea automáticamente username o nombre para evitar conflictos
        self.username = username if username else nombre
        self.nombre = nombre if nombre else username
        self.rol = rol
        self.password = password

    def a_diccionario(self):
        return {
            "id_usuario": self.id_usuario,
            "username": self.username,
            "nombre": self.nombre,
            "rol": self.rol,
            "password": self.password
        }