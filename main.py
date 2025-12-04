import customtkinter
from tkinter import messagebox, Listbox, END

from modelo import Contacto, AdministradorDB

# --- CONFIGURACIÓN DE LA APARIENCIA ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# --- LÓGICA DE LA APLICACIÓN ---
db_manager = AdministradorDB("agenda.db")
contactos_en_lista = []
selected_contact_id = None

def guardar_contacto_nuevo():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    if nombre and email:
        db_manager.agregar_contacto(nombre, apellido, telefono, email)
        messagebox.showinfo("Éxito", "Contacto guardado.")
        actualizar_lista()
        limpiar_campos(borrar_id=True)
    else:
        messagebox.showwarning("Campos vacíos", "El nombre y el email son obligatorios.")

def modificar_contacto_seleccionado():
    if selected_contact_id is None:
        messagebox.showwarning("Sin selección", "Selecciona un contacto para modificar.")
        return
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    if nombre and email:
        db_manager.modificar_contacto(selected_contact_id, nombre, apellido, telefono, email)
        messagebox.showinfo("Éxito", "Contacto modificado.")
        actualizar_lista()
        limpiar_campos(borrar_id=True)
    else:
        messagebox.showwarning("Campos vacíos", "El nombre y el email son obligatorios.")

def eliminar_contacto_seleccionado():
    if selected_contact_id is None:
        messagebox.showwarning("Sin selección", "Selecciona un contacto para eliminar.")
        return
    if messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este contacto?"):
        db_manager.eliminar_contacto(selected_contact_id)
        messagebox.showinfo("Éxito", "Contacto eliminado.")
        actualizar_lista()
        limpiar_campos(borrar_id=True)

def on_contact_select(event):
    global selected_contact_id
    selected_indices = lista_contactos.curselection()
    if not selected_indices:
        return
    indice = selected_indices[0]
    if indice < len(contactos_en_lista):
        contacto_obj = contactos_en_lista[indice]
        selected_contact_id = contacto_obj.id
        limpiar_campos(borrar_id=False)
        entry_nombre.insert(0, contacto_obj.nombre)
        entry_apellido.insert(0, contacto_obj.apellido)
        entry_telefono.insert(0, contacto_obj.telefono)
        entry_email.insert(0, contacto_obj.email)
        
def guardar_contacto_nuevo():
    """Obtiene datos de los campos, verifica si existe y guarda un nuevo contacto."""
    nombre = entry_nombre.get().strip().title()
    apellido = entry_apellido.get().strip().title()
    telefono = entry_telefono.get().strip()
    email = entry_email.get().strip()

    if not (nombre and apellido and email):
        messagebox.showwarning("Campos vacíos", "El nombre, apellido y email son obligatorios.")
        return

    # VERIFICACIÓN !!!
    # preguntamos  si el contacto ya existe
    if db_manager.existe_contacto(nombre, apellido):
        # Si existe, mostramos una advertencia y la función termina
        messagebox.showwarning("Contacto Duplicado", f"El contacto '{nombre} {apellido}' ya se encuentra en la agenda.")
        return 
    # FIN DE LA  VERIFICACIÓN 

    # Si llegamos hasta aca significa que el contacto no estaba duplicado
    # Por lo tanto, procedemos a guardarlo como antes.
    db_manager.agregar_contacto(nombre, apellido, telefono, email)
    messagebox.showinfo("Éxito", "Contacto guardado correctamente.")
    actualizar_lista()
    limpiar_campos(borrar_id=True)

def actualizar_lista():
    global contactos_en_lista
    lista_contactos.delete(0, END)
    contactos_en_lista = db_manager.consultar_contactos()
    for contacto in contactos_en_lista:
        lista_contactos.insert(END, f"{contacto.nombre} {contacto.apellido}")

def limpiar_campos(borrar_id=True):
    global selected_contact_id
    if borrar_id:
        selected_contact_id = None
        lista_contactos.selection_clear(0, END)
    entry_nombre.delete(0, END)
    entry_apellido.delete(0, END)
    entry_telefono.delete(0, END)
    entry_email.delete(0, END)

def limpiar_todo():
    limpiar_campos(borrar_id=True)
    lista_contactos.delete(0, END)

# --- INTERFAZ GRÁFICA ---
ventana = customtkinter.CTk()
ventana.title("Agenda de Contactos")
ventana.geometry("680x550") # <-- Ajusté el ancho inicial

# --- FRAME FORMULARIO ---
frame_formulario = customtkinter.CTkFrame(ventana, corner_radius=10)
frame_formulario.pack(padx=10, pady=10, fill="x", expand=False)
frame_formulario.grid_columnconfigure(1, weight=1)

labels_text = ["Nombre:", "Apellido:", "Teléfono:", "Email:"]
entries = {}
for i, text in enumerate(labels_text):
    label = customtkinter.CTkLabel(frame_formulario, text=text)
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
    entry = customtkinter.CTkEntry(frame_formulario)
    entry.grid(row=i, column=1, padx=10, pady=10, sticky="ew")
    entries[text] = entry

entry_nombre = entries["Nombre:"]
entry_apellido = entries["Apellido:"]
entry_telefono = entries["Teléfono:"]
entry_email = entries["Email:"]

# --- FRAME BOTONES ---
frame_botones = customtkinter.CTkFrame(ventana, fg_color="transparent")
frame_botones.pack(padx=10, pady=5, fill="x", expand=False)
# Configura las 5 columnas para que tengan el mismo peso y se distribuyan equitativamente
frame_botones.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)


boton_guardar = customtkinter.CTkButton(frame_botones, text="Guardar Nuevo", command=guardar_contacto_nuevo)
boton_guardar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

boton_modificar = customtkinter.CTkButton(frame_botones, text="Modificar", command=modificar_contacto_seleccionado)
boton_modificar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

boton_eliminar = customtkinter.CTkButton(frame_botones, text="Eliminar", command=eliminar_contacto_seleccionado)
boton_eliminar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

boton_limpiar = customtkinter.CTkButton(frame_botones, text="Limpiar", command=limpiar_todo)
boton_limpiar.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

boton_listar = customtkinter.CTkButton(frame_botones, text="Listar / Actualizar", command=actualizar_lista)
boton_listar.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

# --- FRAME LISTA ---
frame_lista = customtkinter.CTkFrame(ventana, corner_radius=10)
frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

lista_contactos = Listbox(frame_lista, selectbackground="#1F6AA5", selectforeground="white", background="#2B2B2B", foreground="white", borderwidth=0, highlightthickness=0, font=("Calibri", 12))
lista_contactos.pack(side="left", fill="both", expand=True, padx=5, pady=5)
lista_contactos.bind('<<ListboxSelect>>', on_contact_select)

scrollbar = customtkinter.CTkScrollbar(frame_lista, command=lista_contactos.yview)
scrollbar.pack(side="right", fill="y")
lista_contactos.config(yscrollcommand=scrollbar.set)

# --- INICIAR APP ---
ventana.mainloop()

if __name__ == "__main__":

    
    # cerramos la conexión cuando terminamos
    db_manager.cerrar_conexion()        