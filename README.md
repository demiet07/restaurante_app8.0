# Restaurante App - Semana 13 (Interfaz Gráfica con Tkinter)

Aplicación de gestión para un restaurante desarrollada en Python utilizando la biblioteca gráfica **Tkinter**, implementando una arquitectura modular basada en el proyecto docente de la Semana 13.

## Propósito
Esta versión marca la transición del proyecto desde la consola hacia una interfaz gráfica de usuario (GUI). Su objetivo principal es estructurar adecuadamente el software separando la lógica de negocio, las entidades, el acceso a archivos de datos locales y las vistas gráficas dentro de una única ventana de ejecución (`mainloop`).

## Estructura del Proyecto
restaurante_app/
├── datos/
│   ├── productos.json      # Almacenamiento local de los productos del restaurante
│   └── usuarios.json       # Almacenamiento local de los usuarios autorizados
├── modelos/
│   ├── __init__.py
│   ├── producto.py         # Entidad Producto
│   └── usuario.py          # Entidad Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py   # Lógica de lectura de archivos JSON
│   └── restaurante_servicio.py # Lógica de negocio, validación de acceso y consultas
├── ui/
│   ├── __init__.py
│   ├── login_view.py       # Pantalla gráfica de inicio de sesión
│   └── main_view.py        # Panel principal del sistema con pestañas/opciones
├── main.py                 # Punto de entrada y controlador general de vistas
└── README.md               # Documentación del proyecto

## Flujo de la Aplicación
1. **Inicio**: `main.py` inicializa la ventana principal de Tkinter y carga los servicios de datos.
2. **Autenticación**: Se presenta `LoginView`. El usuario ingresa sus credenciales, las cuales son validadas por `RestauranteServicio`.
3. **Panel Principal**: Tras un acceso correcto, se despliega `MainView` dentro de la misma ventana.
4. **Consulta de Datos**: Permite alternar la visualización entre productos y usuarios registrados cargados desde los archivos JSON. Las opciones avanzadas (como Ventas) se identifican visualmente como pendientes.
5. **Cierre de Sesión**: Permite retornar de manera segura a la pantalla de acceso sin cerrar la aplicación.

## Requisitos
- Python 3.x instalado.
- Biblioteca estándar `tkinter` (incluida por defecto en la mayoría de las distribuciones de Python).

## Instrucciones de Ejecución
1. Clone este repositorio o descargue los archivos manteniendo la estructura de carpetas indicada.
2. Abra una terminal en la carpeta raíz del proyecto (`restaurante_app/`).
3. Ejecute el archivo principal mediante el comando:
   ```bash
   python main.py