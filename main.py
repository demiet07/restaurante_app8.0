import os
import tkinter as tk
from servicios.restaurante import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:
    """Controlador principal que gestiona la ventana única de Tkinter y el cambio de vistas."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("750x500")
        self.root.minsize(700, 450)

        # Definir rutas de los archivos JSON de datos locales
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_productos = os.path.join(base_dir, "datos", "productos.json")
        ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")

        # Inicializar los servicios de negocio
        self.restaurante_servicio = RestauranteServicio(ruta_productos, ruta_usuarios)

        # Contenedor principal de vistas
        self.vista_actual = None
        self.mostrar_login_view()

    def limpiar_ventana(self):
        """Elimina cualquier vista activa anterior para mantener una única ventana."""
        if self.vista_actual is not None:
            self.vista_actual.destroy()

    def mostrar_login_view(self):
        self.limpiar_ventana()
        self.vista_actual = LoginView(self.root, self, self.restaurante_servicio)
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_main_view(self, usuario_actual):
        self.limpiar_ventana()
        self.vista_actual = MainView(self.root, self, self.restaurante_servicio, usuario_actual)
        self.vista_actual.pack(fill="both", expand=True)

    def cerrar_sesion(self):
        self.mostrar_login_view()

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()