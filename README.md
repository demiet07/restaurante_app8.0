# Restaurante App - Semana 11

**Estudiante:** Damian Ortega   
**Asignatura:** Programación Orientada a Objetos  

## Descripción del Sistema
Evolución de `restaurante_app` que incorpora el registro de ventas mediante colecciones de objetos, control de stock y persistencia extendida a través de tres archivos JSON (`productos.json`, `usuarios.json` y `ventas.json`).

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md