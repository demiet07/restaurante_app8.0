import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal raíz

    servicio = RestauranteServicio()
    LoginView(root, servicio)

    root.mainloop()

if __name__ == "__main__":
    main()