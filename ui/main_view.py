import tkinter as tk
from tkinter import messagebox

class MainView(tk.Frame):
    """Panel principal del restaurante con pestañas para productos, usuarios y opciones pendientes."""

    def __init__(self, parent, controlador, restaurante_servicio, usuario_actual):
        super().__init__(parent, bg="#f0f0f0")
        self.controlador = controlador
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.crear_widgets()

    def crear_widgets(self):
        # Barra superior con bienvenida y botón de cerrar sesión
        top_frame = tk.Frame(self, bg="#333333", padx=15, pady=10)
        top_frame.pack(side="top", fill="x")

        lbl_bienvenida = tk.Label(top_frame, text=f"Bienvenido: {self.usuario_actual.nombre} ({self.usuario_actual.rol})", font=("Arial", 11, "bold"), bg="#333333", fg="white")
        lbl_bienvenida.pack(side="left")

        btn_logout = tk.Button(top_frame, text="Cerrar Sesión", font=("Arial", 9), bg="#d9534f", fg="white", command=self.controlador.cerrar_sesion)
        btn_logout.pack(side="right")

        # Contenedor de opciones con Listbox y vistas tabulares básicas
        content_frame = tk.Frame(self, bg="#f0f0f0", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Panel izquierdo de navegación o selección de vistas
        menu_frame = tk.Frame(content_frame, bg="#e0e0e0", padx=10, pady=10, width=200)
        menu_frame.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(menu_frame, text="Opciones", font=("Arial", 11, "bold"), bg="#e0e0e0").pack(pady=(0, 10))

        btn_ver_productos = tk.Button(menu_frame, text="Productos", font=("Arial", 10), width=18, command=self.mostrar_productos)
        btn_ver_productos.pack(pady=5)

        btn_ver_usuarios = tk.Button(menu_frame, text="Usuarios", font=("Arial", 10), width=18, command=self.mostrar_usuarios)
        btn_ver_usuarios.pack(pady=5)

        btn_ventas = tk.Button(menu_frame, text="Ventas (Pendiente)", font=("Arial", 10), width=18, state="disabled", fg="gray")
        btn_ventas.pack(pady=5)

        # Panel derecho para mostrar el contenido dinámico
        self.display_frame = tk.Frame(content_frame, bg="white", padx=15, pady=15, relief="solid", borderwidth=1)
        self.display_frame.pack(side="right", fill="both", expand=True)

        self.lbl_titulo_seccion = tk.Label(self.display_frame, text="Seleccione una opción del menú", font=("Arial", 13, "bold"), bg="white", fg="#333333")
        self.lbl_titulo_seccion.pack(anchor="w", pady=(0, 10))

        # Listbox con barra de desplazamiento para mostrar registros
        list_container = tk.Frame(self.display_frame, bg="white")
        list_container.pack(fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(list_container)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(list_container, font=("Consolas", 10), yscrollcommand=self.scrollbar.set, width=60, height=15)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        # Mostrar productos por defecto al iniciar la vista principal
        self.mostrar_productos()

    def mostrar_productos(self):
        self.lbl_titulo_seccion.config(text="Productos Registrados en el Restaurante")
        self.listbox.delete(0, tk.END)
        productos = self.restaurante_servicio.obtener_productos()
        for p in productos:
            texto = f"ID: {p.id} | {p.nombre:<25} | Precio: ${p.precio:>6.2f} | Stock: {p.stock:>3} | Cat: {p.categoria}"
            self.listbox.insert(tk.END, texto)

    def mostrar_usuarios(self):
        self.lbl_titulo_seccion.config(text="Usuarios Registrados en el Sistema")
        self.listbox.delete(0, tk.END)
        usuarios = self.restaurante_servicio.obtener_usuarios()
        for u in usuarios:
            texto = f"Usuario: {u.username:<12} | Nombre: {u.nombre:<20} | Rol: {u.rol}"
            self.listbox.insert(tk.END, texto)