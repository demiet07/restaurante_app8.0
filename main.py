# -*- coding: utf-8 -*-
"""
Proyecto: restaurante_app (Semana 12 - Optimización de Rendimiento)
Autor: Damian Ortega
Asignatura: Programación Orientada a Objetos
"""

from servicios.restaurante import Restaurante

def mostrar_encabezado():
    print("=" * 60)
    print(" RESTAURANTE APP - OPTIMIZACIÓN DE RENDIMIENTO (SEMANA 12) ")
    print(" Desarrollado por: Damian Ortega")
    print("=" * 60)

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar nuevo producto")
    print("2. Registrar nuevo usuario")
    print("3. Registrar una venta")
    print("4. Buscar producto por código")
    print("5. Buscar usuario por identificación")
    print("6. Consultar historial de ventas de un usuario")
    print("7. Listar todos los datos")
    print("8. Salir")

def main():
    mostrar_encabezado()
    app = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-8): ").strip()

        if opcion == "1":
            print("\n--- REGISTRO DE PRODUCTO ---")
            cod = input("Código del producto: ").strip().upper()
            nom = input("Nombre del producto: ").strip()
            try:
                pre = float(input("Precio ($): "))
                stk = int(input("Stock inicial: "))
                if app.registrar_producto(cod, nom, pre, stk):
                    print(f"✔ Producto '{nom}' [{cod}] registrado exitosamente.")
                else:
                    print(f"❌ Error: El código '{cod}' ya existe.")
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos.")

        elif opcion == "2":
            print("\n--- REGISTRO DE USUARIO ---")
            uid = input("Identificación / Cédula: ").strip()
            nom = input("Nombre completo: ").strip()
            em = input("Correo electrónico: ").strip()
            if app.registrar_usuario(uid, nom, em):
                print(f"✔ Usuario '{nom}' registrado exitosamente.")
            else:
                print(f"❌ Error: La identificación '{uid}' ya está registrada.")

        elif opcion == "3":
            print("\n--- REGISTRO DE VENTA ---")
            vid = input("ID de la Venta: ").strip().upper()
            uid = input("Identificación del Usuario: ").strip()
            cod = input("Código del Producto: ").strip().upper()
            try:
                cant = int(input("Cantidad a comprar: "))
                exito, mensaje = app.registrar_venta(vid, uid, cod, cant)
                print(f"{'✔' if exito else '❌'} {mensaje}")
            except ValueError:
                print("❌ Error: La cantidad debe ser un entero.")

        elif opcion == "4":
            print("\n--- BÚSQUEDA DIRECTA DE PRODUCTO ---")
            cod = input("Ingrese código: ").strip().upper()
            p = app.buscar_producto(cod)
            if p:
                print(f"\n- Código: {p.codigo}\n- Nombre: {p.nombre}\n- Precio: ${p.precio:.2f}\n- Stock: {p.stock}")
            else:
                print(f"❌ Producto '{cod}' no encontrado.")

        elif opcion == "5":
            print("\n--- BÚSQUEDA DIRECTA DE USUARIO ---")
            uid = input("Ingrese identificación: ").strip()
            u = app.buscar_usuario(uid)
            if u:
                print(f"\n- ID: {u.identificacion}\n- Nombre: {u.nombre}\n- Email: {u.email}")
            else:
                print(f"❌ Usuario '{uid}' no encontrado.")

        elif opcion == "6":
            print("\n--- HISTORIAL DE VENTAS POR USUARIO ---")
            uid = input("Ingrese identificación: ").strip()
            ventas = app.obtener_ventas_usuario(uid)
            if ventas:
                print(f"\nVentas del usuario {uid}:")
                for v in ventas:
                    print(f"  • Venta #{v.id_venta} | Producto: {v.codigo_producto} | Cantidad: {v.cantidad} | Total: ${v.total:.2f}")
            else:
                print(f"ℹ No se registran ventas para '{uid}'.")

        elif opcion == "7":
            print("\n--- VISTA GENERAL DEL SISTEMA ---")
            print(f"\n📦 PRODUCTOS ({len(app.productos)}):")
            for p in app.productos:
                print(f"  - [{p.codigo}] {p.nombre} | ${p.precio:.2f} | Stock: {p.stock}")
            print(f"\n👤 USUARIOS ({len(app.usuarios)}):")
            for u in app.usuarios:
                print(f"  - [{u.identificacion}] {u.nombre} ({u.email})")
            print(f"\n🧾 HISTORIAL DE VENTAS ({len(app.ventas)}):")
            for v in app.ventas:
                print(f"  - Venta {v.id_venta} | Cliente: {v.id_usuario} | Prod: {v.codigo_producto} | Total: ${v.total:.2f}")

        elif opcion == "8":
            print("\nGuardando y saliendo... ¡Gracias por usar la app de Damian Ortega!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()