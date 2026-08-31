from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n--- SISTEMA DE RESTAURANTE ---")
    print("1. Registrar Producto")
    print("2. Registrar Usuario")
    print("3. Vender Producto")
    print("4. Consultar Ventas de un Usuario")
    print("5. Listar Productos")
    print("6. Listar Usuarios")
    print("7. Salir")

def main():
    servicio = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                codigo = input("Código del producto: ").strip()
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio del producto: "))
                stock = int(input("Stock inicial: "))
                if servicio.registrar_producto(codigo, nombre, precio, stock):
                    print("Producto registrado exitosamente.")
            except ValueError as e:
                print(f"Error de formato o entrada inválida: {e}")

        elif opcion == "2":
            try:
                identificacion = input("Identificación del usuario: ").strip()
                nombre = input("Nombre del usuario: ").strip()
                correo = input("Correo electrónico: ").strip()
                if servicio.registrar_usuario(identificacion, nombre, correo):
                    print("Usuario registrado exitosamente.")
            except ValueError as e:
                print(f"Error en datos de entrada: {e}")

        elif opcion == "3":
            try:
                identificacion = input("Identificación del usuario: ").strip()
                codigo = input("Código del producto: ").strip()
                cantidad = int(input("Cantidad a comprar: "))
                if servicio.vender_producto(codigo, identificacion, cantidad):
                    print("Venta registrada con éxito.")
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")

        elif opcion == "4":
            identificacion = input("Identificación del usuario a consultar: ").strip()
            ventas = servicio.consultar_ventas_usuario(identificacion)
            if ventas:
                print(f"\n--- Ventas asociadas al Usuario {identificacion} ---")
                for v in ventas:
                    print(f"Producto: [{v['producto_codigo']}] {v['producto_nombre']} | Cantidad: {v['cantidad']}")
            else:
                print("No se encontraron ventas para este usuario o el usuario no existe.")

        elif opcion == "5":
            productos = servicio.obtener_productos()
            print("\n--- Lista de Productos ---")
            if not productos:
                print("No hay productos registrados.")
            for p in productos:
                print(f"Código: {p.codigo} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "6":
            usuarios = servicio.obtener_usuarios()
            print("\n--- Lista de Usuarios ---")
            if not usuarios:
                print("No hay usuarios registrados.")
            for u in usuarios:
                print(f"ID: {u.identificacion} | Nombre: {u.nombre} | Correo: {u.correo}")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()