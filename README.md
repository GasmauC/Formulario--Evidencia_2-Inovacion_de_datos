# 📒 Agenda de Contactos - CRUD con Python y CustomTkinter

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![GUI](https://img.shields.io/badge/CustomTkinter-UI-green?style=for-the-badge)

> **Aplicación de escritorio para la gestión eficiente de contactos, implementando principios de POO y Arquitectura en Capas.**

---

## 📖 Descripción del Proyecto

Este proyecto es una aplicación de escritorio desarrollada en **Python** que permite gestionar una libreta de contactos personal. [cite_start]El objetivo principal fue crear una herramienta intuitiva que realice operaciones **ABM** (Alta, Baja y Modificación) con persistencia de datos[cite: 1094, 1096].

[cite_start]A diferencia de scripts básicos, este sistema implementa una arquitectura robusta separando la lógica de negocio de la interfaz gráfica, y utiliza **CustomTkinter** para ofrecer una experiencia de usuario moderna con modo oscuro nativo[cite: 1095].

---

## ✨ Características Principales

* [cite_start]**CRUD Completo:** Funcionalidades para Crear, Leer, Actualizar y Eliminar contactos de forma sencilla[cite: 1096].
* [cite_start]**Interfaz Moderna:** Uso de la librería `customtkinter` para widgets estilizados y soporte de temas (Dark Mode)[cite: 1134].
* [cite_start]**Persistencia de Datos:** Almacenamiento permanente en base de datos **SQLite** (`agenda.db`), asegurando que la información no se pierda al cerrar la app[cite: 1147].
* **Validaciones Inteligentes:**
    * [cite_start]Prevención de contactos duplicados (insensible a mayúsculas/minúsculas)[cite: 1127].
    * Control de campos obligatorios antes de guardar.
* [cite_start]**Seguridad:** Uso de consultas SQL parametrizadas para prevenir inyección de código[cite: 1128].

---

## 🏗️ Arquitectura del Software

[cite_start]El proyecto sigue el principio de **Separación de Responsabilidades**, dividiendo el código en dos capas lógicas[cite: 1098]:

### 1. Capa de Modelo (`modelo.py`)
Actúa como el "cerebro" de la aplicación. Contiene:
* [cite_start]**Clase `Contacto`:** Representación orientada a objetos de la entidad (blueprint)[cite: 1109].
* **Clase `AdministradorDB`:** Funciona como un **DAO (Data Access Object)**. [cite_start]Es la única clase que interactúa con SQL, encargándose de conectar, crear tablas y ejecutar sentencias DDL/DML[cite: 1115, 1116].

### 2. Capa de Vista (`main.py`)
Es la "cara" de la aplicación. Se encarga de:
* Dibujar la interfaz gráfica (Ventana, Botones, Entradas).
* Capturar eventos del usuario.
* [cite_start]Comunicarse con el Modelo para solicitar operaciones, sin conocer detalles de la base de datos[cite: 1101, 1137].

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.
* **Interfaz Gráfica:** `customtkinter` (Wrapper moderno de Tkinter).
* **Base de Datos:** `sqlite3` (Motor nativo de Python).
* **Paradigma:** Programación Orientada a Objetos (POO).

---

## 🚀 Instrucciones de Ejecución

Sigue estos pasos para probar el proyecto en tu máquina local:

### 1. Prerrequisitos
Asegúrate de tener Python instalado. Además, necesitarás instalar la librería gráfica externa:

```bash
pip install customtkinter
