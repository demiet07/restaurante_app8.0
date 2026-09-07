class Venta:
    def __init__(self, id_venta: str, id_usuario: str, codigo_producto: str, cantidad: int, total: float):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.total = total

    def a_dict(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @staticmethod
    def desde_dict(datos: dict) -> "Venta":
        return Venta(
            datos["id_venta"],
            datos["id_usuario"],
            datos["codigo_producto"],
            datos["cantidad"],
            datos["total"]
        )