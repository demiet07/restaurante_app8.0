# Restaurante App - Semana 14: Componentes y Contenedores

Aplicación de escritorio desarrollada en Python con Tkinter, manteniendo una arquitectura modular estricta, servicios de negocio y persistencia en archivos JSON.

## 🚀 Propósito de la Semana 14
Evolucionar la interfaz gráfica implementando de forma adecuada **componentes y contenedores** (`Frame`, `LabelFrame`) y gestores de geometría (`grid`, `pack`). Se mejoró la experiencia de usuario mediante formularios y áreas de visualización estructuradas.

## 📂 Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md