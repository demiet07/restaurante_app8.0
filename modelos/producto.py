class Producto:
    """Representa un producto o platillo disponible en el restaurante."""

    def __init__(self, id: int, nombre: str, precio: float, stock: int, categoria: str):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"