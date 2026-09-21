import tkinter as tk
from tkinter import ttk, messagebox
from ui.main_view import MainView

class LoginView:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Restaurante App - Login")
        self.ventana.geometry("350x250")
        self.ventana.resizable(False, False)
        
        self.crear_widgets()

    def crear_widgets(self):
        frame = ttk.LabelFrame(self.ventana, text="Acceso al Sistema", padding=20)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Usuario:").pack(anchor=tk.W, pady=2)
        self.txt_usuario = ttk.Entry(frame, width=30)
        self.txt_usuario.pack(pady=5)

        ttk.Label(frame, text="Contraseña:").pack(anchor=tk.W, pady=2)
        self.txt_pass = ttk.Entry(frame, width=30, show="*")
        self.txt_pass.pack(pady=5)

        btn_login = ttk.Button(frame, text="Ingresar", command=self.verificar_credenciales)
        btn_login.pack(pady=15)

    def verificar_credenciales(self):
        user = self.txt_usuario.get()
        pwd = self.txt_pass.get()
        
        if self.servicio.validar_login(user, pwd):
            messagebox.showinfo("Éxito", "Acceso concedido.")
            self.ventana.destroy()
            MainView(self.root, self.servicio)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")