# 📘 Agenda de Contactos - Gestión Inteligente con Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge&logo=sqlite)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Terminado-success?style=for-the-badge)

> Una aplicación de escritorio moderna y robusta para la gestión de contactos (ABM), diseñada con una arquitectura modular y principios de Programación Orientada a Objetos (POO).

---

## 🖼️ Vista Previa

![Interfaz de Usuario](agenda.png)


---

## 🚀 Descripción del Proyecto

Este sistema permite administrar una libreta de contactos personal de manera intuitiva y segura. A diferencia de scripts básicos, este proyecto implementa una **arquitectura de software profesional** que separa la lógica de negocio de la interfaz gráfica.

El objetivo principal es proveer una herramienta intuitiva para realizar operaciones CRUD (Alta, Baja y Modificación), garantizando la integridad de los datos mediante validaciones lógicas y SQL.

### ✨ Características Principales

* **Gestión Completa (CRUD):** Funcionalidades de agregar, leer, modificar y eliminar contactos de forma persistente.
* **Interfaz Moderna:** Uso de `customtkinter` para lograr una estética visual superior con bordes redondeados y temas integrados.
* **Validación Inteligente:**
    * Campos obligatorios protegidos.
    * **Prevención de duplicados:** El sistema verifica si un contacto ya existe (insensible a mayúsculas/minúsculas mediante `LOWER()` en SQL) antes de guardarlo.
* **Seguridad:** Implementación de consultas SQL parametrizadas para blindar la aplicación contra inyecciones SQL.
* **Arquitectura Escalable:** Diseño modular que facilita el mantenimiento y futuras expansiones.

---

## 🏗️ Arquitectura del Software

El proyecto sigue estrictamente el principio de **Separación de Responsabilidades**, dividiendo el código en capas lógicas:

### 1. Capa de Vista (`main.py`) 🖥️
* **Responsabilidad:** Es la "cara" de la aplicación. Gestiona la presentación visual y captura los eventos del usuario.
* **Detalle:** Actúa como controlador pero es completamente independiente de la lógica de datos. Nunca ejecuta SQL directamente.

### 2. Capa de Modelo (`modelo.py`) 🧠
* **Responsabilidad:** Es el "cerebro" y encapsula la lógica de negocio y el acceso a datos.
* **Componentes:**
    * **Clase `Contacto`:** Blueprint que define la estructura de datos de la entidad principal.
    * **Clase `AdministradorDB`:** Actúa como un DAO (Data Access Object), centralizando la conexión y todas las sentencias DDL y DML.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso en el proyecto |
| :--- | :--- |
| **Python** | Lenguaje principal del backend y frontend. |
| **SQLite3** | Motor de base de datos relacional ligero y eficiente. |
| **CustomTkinter** | Librería gráfica para interfaces modernas (wrapper de Tkinter). |
| **POO** | Paradigma utilizado para estructurar el código (Clases y Objetos). |

---

## 📂 Estructura del Proyecto

```text
📁 Agenda-Contactos
│
├── main.py           # Frontend: Interfaz Gráfica y Control de Eventos
├── modelo.py         # Backend: Lógica de Negocio y DAO
├── agenda.db         # Persistencia: Base de datos SQLite (Auto-generada)
└── Documentacion.pdf # Documentación técnica detallada del sistema
