class Producto:
    def __init__(self, id=None, id_prod=None, nombre="", precio=0.0, stock=0, categoria=None, **kwargs):
        self.id_prod = id_prod if id_prod is not None else id
        self.nombre = nombre
        self.precio = float(precio) if precio is not None else 0.0
        self.stock = int(stock) if stock is not None else 0
        self.categoria = categoria

    def a_diccionario(self):
        return {
            "id_prod": self.id_prod,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria
        }