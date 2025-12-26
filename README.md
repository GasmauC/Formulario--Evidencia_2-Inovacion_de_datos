# 📘 Agenda de Contactos - Gestión Inteligente con Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge&logo=sqlite)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Terminado-success?style=for-the-badge)

> Una aplicación de escritorio moderna y robusta para la gestión de contactos (ABM), diseñada con una arquitectura modular y principios de Programación Orientada a Objetos (POO).

---

## 🖼️ Vista Previa

![Interfaz de Usuario](screenshot.png)
*(Asegúrate de incluir una captura de pantalla de tu aplicación aquí para mostrar la interfaz Dark Mode)*

---

## 🚀 Descripción del Proyecto

Este sistema permite administrar una libreta de contactos personal de manera intuitiva y segura. [cite_start]A diferencia de scripts básicos, este proyecto implementa una **arquitectura de software profesional** que separa la lógica de negocio de la interfaz gráfica[cite: 8].

[cite_start]El objetivo principal fue crear una herramienta escalable que garantice la persistencia de datos mediante **SQLite** y ofrezca una experiencia de usuario agradable gracias a **CustomTkinter**[cite: 5].

### ✨ Características Principales

* **CRUD Completo:** Alta, Baja, Modificación y Consulta de contactos.
* [cite_start]**Interfaz Moderna:** Diseño "Dark Mode" con bordes redondeados y estética profesional[cite: 44].
* **Validación de Datos:**
    * Verificación de campos obligatorios.
    * [cite_start]**Prevención de duplicados:** El sistema detecta si un contacto (nombre + apellido) ya existe antes de guardar[cite: 37].
* [cite_start]**Seguridad:** Uso de consultas SQL parametrizadas para evitar inyecciones SQL.
* [cite_start]**Persistencia:** Los datos se guardan automáticamente en `agenda.db`[cite: 59].

---

## 🏗️ Arquitectura del Software

[cite_start]El proyecto sigue el principio de **Separación de Responsabilidades**, dividiendo el código en dos capas lógicas[cite: 7, 8]:

### 1. Capa de Vista (`main.py`) 🖥️
* **Función:** Es la "cara" de la aplicación. Maneja la interacción con el usuario y dibuja la interfaz gráfica.
* [cite_start]**Detalle:** Actúa como controlador, capturando eventos y comunicándose con el modelo, pero **nunca ejecuta SQL directamente**[cite: 47].

### 2. Capa de Modelo (`modelo.py`) 🧠
* **Función:** Es el "cerebro". Contiene la lógica de negocio y el acceso a datos (DAO).
* **Componentes:**
    * [cite_start]`Clase Contacto`: Representa la entidad principal (blueprint)[cite: 20].
    * [cite_start]`Clase AdministradorDB`: Centraliza la conexión y las operaciones SQL (INSERT, UPDATE, DELETE, SELECT)[cite: 26].

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso en el proyecto |
| :--- | :--- |
| **Python** | Lenguaje principal del backend y frontend. |
| **SQLite3** | Motor de base de datos relacional ligero y eficiente. |
| **CustomTkinter** | Librería para interfaces gráficas modernas (wrapper de Tkinter). |
| **POO** | Paradigma usado para modelar `Contactos` y el `AdministradorDB`. |

---

## 📂 Estructura del Proyecto

```text
📁 Agenda-Contactos
│
├── main.py          # Interfaz Gráfica y Control de Eventos (Frontend)
├── modelo.py        # Lógica de Negocio y Conexión a Base de Datos (Backend)
├── agenda.db        # Archivo de Base de Datos (Se genera automáticamente)
├── Documentacion.pdf # Documentación técnica detallada
└── README.md        # Este archivo
