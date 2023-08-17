import tkinter as tk
from tkinter import Button, Frame, Label, PhotoImage, ttk
from tkinter.font import Font

# Función para manejar los botones numéricos y operadores


def boton_presionado(valor):
    # Obtener el texto actual y eliminar espacios
    texto_actual = pantalla.get("1.0", tk.END).strip()
    if valor == "=":
        try:
            resultado = eval(texto_actual)
            actualizar_pantalla(resultado)
        except:
            actualizar_pantalla("Error")
    elif valor == "C":
        actualizar_pantalla("0")
    elif valor == ".":
        if "." not in texto_actual:
            pantalla.insert(tk.END, valor)
    else:
        if texto_actual == "0":
            # Eliminar el cero inicial si se presiona otro número
            pantalla.delete("1.0", tk.END)
        pantalla.insert(tk.END, valor)

# Función para actualizar la pantalla de la calculadora


def actualizar_pantalla(valor):
    pantalla.delete("1.0", tk.END)
    pantalla.insert("1.0", valor)


# Crear la ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("400x550")  # Tamaño fijo de la ventana
root.config(bg="#FCFFE7", padx=15, pady=15)  # Color de fondo

# Crear la calculadora con relieve
frame_calculadora = Frame(root, relief="raised", borderwidth=5)
frame_calculadora.grid(row=0, column=0, padx=10, pady=10)
frame_calculadora.config(width="400", height="500", bg="#2B3467")
frame_calculadora.pack()

# Crear la pantalla con fondo personalizado
pantalla = tk.Text(frame_calculadora, height=1,
                   state=tk.NORMAL, font=("Roboto", 25))
pantalla.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Configurar color de cursor y fondo
pantalla.config(bg="#FCFFE7", insertbackground="#2B3467")
pantalla.insert("1.0", "0")  # Insertar cero inicial

# Aplicar etiqueta a todo el texto
pantalla.tag_add("blue", "1.0", "end")

# Crear los botones en una estructura de lista
boton_valores = [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("0", ".", "C", "/"),
    ("=",)
]

# Crear los botones en un bucle
for fila, valores in enumerate(boton_valores):
    for columna, valor in enumerate(valores):
        boton = Button(frame_calculadora, width=5, height=2,
                       text=valor, command=lambda v=valor: boton_presionado(v),
                       font=("Roboto", 15), fg="#2B3467", bg="#FCFFE7",
                       borderwidth=2, relief="ridge", activebackground="#FCFFE7", )
        boton.grid(row=fila + 2, column=columna, sticky="ns", padx=5, pady=5,)

# Hacer que las celdas de la calculadora se expandan
for i in range(6):
    frame_calculadora.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame_calculadora.grid_columnconfigure(i, weight=1)

foto = PhotoImage(
    file="C:\\Users\\josel\\Desktop\\Python\\calculadora\\img\\Logo.png")
imagenLabel = Label(root, image=foto, background="#FCFFE7", borderwidth=50)
imagenLabel.pack()

# Iniciar el bucle de la aplicación
root.mainloop()
