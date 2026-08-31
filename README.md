# restaurante_app6.0 - Semana 11

**Estudiante:** Damian Ortega  
**Usuario GitHub:** demiet07  
**Asignatura:** Programación Orientada a Objetos  
**Proyecto:** Evolución del sistema `restaurante_app` con gestión de ventas, relaciones entre colecciones, control riguroso de inventario y persistencia basada en JSON.

---

## 1. Descripción Contextual y Objetivo del Sistema

La presente versión de **restaurante_app6.0** constituye una evolución arquitectónica con respecto a entregas anteriores. El objetivo central de esta iteración es implementar la operación de **Venta de Productos**, la cual relaciona directamente un objeto de tipo `Usuario` con un objeto de tipo `Producto` mediante la instanciación de una nueva entidad transaccional llamada `Venta`.

A diferencia de un sistema simple de inventario, la aplicación implementa reglas de negocio avanzadas para garantizar la consistencia de los datos:
* Impide la venta si el usuario o el producto no existen en el sistema.
* Impide transacciones con cantidades menores o iguales a cero.
* Verifica la disponibilidad de stock previo a la transacción y disminuye de forma atómica la cantidad de unidades en inventario.
* Realiza persistencia automática inmediata en archivos JSON tras cada modificación exitosa, permitiendo rehidratar completamente el estado del sistema tras un reinicio.

---

## 2. Arquitectura y Estructura del Proyecto

El proyecto respeta de forma estricta el patrón de diseño modular por capas, separando los datos, el dominio de negocio, los servicios de infraestructura y la interfaz de consola:

```text
restaurante_app6.0/
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