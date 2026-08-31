class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Producto':
        try:
            return Producto(
                codigo=str(datos["codigo"]),
                nombre=str(datos["nombre"]),
                precio=float(datos["precio"]),
                stock=int(datos["stock"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave requerida en el JSON de Producto: {e}")