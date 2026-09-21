import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Toplevel):
    def __init__(self, root, servicio):
        super().__init__(root)
        self.root = root
        self.servicio = servicio
        
        self.title("Restaurante App - Gestión Principal")
        self.geometry("900x650")
        
        self.crear_interfaz()
        self.actualizar_visor()

    def crear_interfaz(self):
        # 1. Contenedor de Navegación Superior
        barra_nav = ttk.Frame(self, padding=10)
        barra_nav.pack(side=tk.TOP, fill=tk.X)
        
        ttk.Button(barra_nav, text="Consultar Usuarios", command=self.ver_usuarios).pack(side=tk.LEFT, padx=5)
        ttk.Button(barra_nav, text="Actualizar Vista", command=self.actualizar_visor).pack(side=tk.LEFT, padx=5)

        # 2. Contenedor Principal (Divide la pantalla en dos secciones)
        contenedor_principal = ttk.Frame(self, padding=10)
        contenedor_principal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 3. Subcontenedor Izquierdo: Formulario y Acciones (LabelFrame)
        frame_form = ttk.LabelFrame(contenedor_principal, text="Gestión de Productos", padding=15)
        frame_form.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        ttk.Label(frame_form, text="ID Producto:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.txt_id = ttk.Entry(frame_form)
        self.txt_id.grid(row=0, column=1, sticky=tk.EW, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.txt_nombre = ttk.Entry(frame_form)
        self.txt_nombre.grid(row=1, column=1, sticky=tk.EW, pady=5)

        ttk.Label(frame_form, text="Precio:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.txt_precio = ttk.Entry(frame_form)
        self.txt_precio.grid(row=2, column=1, sticky=tk.EW, pady=5)

        ttk.Label(frame_form, text="Stock:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.txt_stock = ttk.Entry(frame_form)
        self.txt_stock.grid(row=3, column=1, sticky=tk.EW, pady=5)

        # Contenedor de Botones de Acción
        frame_botones = ttk.Frame(frame_form, padding=5)
        frame_botones.grid(row=4, column=0, columnspan=2, pady=15)

        ttk.Button(frame_botones, text="Registrar", command=self.accion_registrar).pack(side=tk.LEFT, padx=3)
        ttk.Button(frame_botones, text="Actualizar", command=self.accion_actualizar).pack(side=tk.LEFT, padx=3)
        ttk.Button(frame_botones, text="Eliminar", command=self.accion_eliminar).pack(side=tk.LEFT, padx=3)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).pack(side=tk.LEFT, padx=3)

        # 4. Subcontenedor Derecho: Visualización de Inventario (LabelFrame)
        frame_visor = ttk.LabelFrame(contenedor_principal, text="Inventario Actual", padding=15)
        frame_visor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.texto_visor = tk.Text(frame_visor, width=40, height=20, state=tk.DISABLED)
        self.texto_visor.pack(fill=tk.BOTH, expand=True)

    def actualizar_visor(self):
        self.texto_visor.config(state=tk.NORMAL)
        self.texto_visor.delete("1.0", tk.END)
        
        productos = self.servicio.obtener_productos()
        if not productos:
            self.texto_visor.insert(tk.END, "No hay productos registrados en el inventario.")
        else:
            for p in productos:
                info = f"ID: {p.id_prod} | {p.nombre} | ${p.precio:.2f} | Stock: {p.stock}\n"
                self.texto_visor.insert(tk.END, info)
                
        self.texto_visor.config(state=tk.DISABLED)

    def limpiar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_stock.delete(0, tk.END)

    def accion_registrar(self):
        try:
            self.servicio.registrar_producto(
                self.txt_id.get(),
                self.txt_nombre.get(),
                self.txt_precio.get(),
                self.txt_stock.get()
            )
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.actualizar_visor()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def accion_actualizar(self):
        try:
            self.servicio.actualizar_producto(
                self.txt_id.get(),
                self.txt_nombre.get(),
                self.txt_precio.get(),
                self.txt_stock.get()
            )
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.actualizar_visor()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def accion_eliminar(self):
        try:
            id_prod = self.txt_id.get()
            if not id_prod:
                raise ValueError("Debe ingresar el ID del producto que desea eliminar.")
            self.servicio.eliminar_producto(id_prod)
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.actualizar_visor()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ver_usuarios(self):
        usuarios = self.servicio.obtener_usuarios()
        listado = "\n".join([f"Usuario: {u.username} | Rol: {u.rol}" for u in usuarios])
        messagebox.showinfo("Usuarios Registrados", listado if listado else "No hay usuarios.")