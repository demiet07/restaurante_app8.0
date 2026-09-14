class Usuario:
    """Representa a un usuario del sistema del restaurante."""

    def __init__(self, username: str, password: str, nombre: str, rol: str):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    def __str__(self) -> str:
        return f"{self.nombre} ({self.username}) - Rol: {self.rol}"