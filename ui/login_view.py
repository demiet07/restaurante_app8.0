import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    """Pantalla gráfica de acceso simulado."""

    def __init__(self, parent, controlador, restaurante_servicio):
        super().__init__(parent, bg="#f5f5f5")
        self.controlador = controlador
        self.restaurante_servicio = restaurante_servicio
        self.crear_widgets()

    def crear_widgets(self):
        # Contenedor central
        frame_centro = tk.Frame(self, bg="#ffffff", padx=30, pady=30, relief="raised", borderwidth=1)
        frame_centro.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_centro, text="Restaurante App", font=("Arial", 18, "bold"), bg="#ffffff", fg="#333333").pack(pady=(0, 20))

        tk.Label(frame_centro, text="Usuario:", font=("Arial", 10), bg="#ffffff", anchor="w").pack(fill="x")
        self.entry_usuario = tk.Entry(frame_centro, font=("Arial", 11), width=25)
        self.entry_usuario.pack(pady=(0, 10))

        tk.Label(frame_centro, text="Contraseña:", font=("Arial", 10), bg="#ffffff", anchor="w").pack(fill="x")
        self.entry_password = tk.Entry(frame_centro, font=("Arial", 11), width=25, show="*")
        self.entry_password.pack(pady=(0, 20))

        btn_ingresar = tk.Button(frame_centro, text="Ingresar", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=20, command=self.intentar_login)
        btn_ingresar.pack()

    def intentar_login(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Campos vacíos", "Por favor, ingrese usuario y contraseña.")
            return

        usuario_valido = self.restaurante_servicio.validar_acceso(usuario, password)
        if usuario_valido:
            self.entry_usuario.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.controlador.mostrar_main_view(usuario_valido)
        else:
            messagebox.showerror("Acceso denegado", "Credenciales incorrectas. Intente nuevamente.")
            self.entry_password.delete(0, tk.END)