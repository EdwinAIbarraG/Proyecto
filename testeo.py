import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()

# Crear un widget Canvas
canvas = tk.Canvas(ventana)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear un widget Scrollbar horizontal
scrollbar = ttk.Scrollbar(ventana, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configurar la vinculación entre el canvas y la scrollbar
canvas.configure(xscrollcommand=scrollbar.set)

# Crear un frame dentro del canvas para agregar contenido
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Agregar contenido al frame (ejemplo: etiquetas de texto)
for i in range(50):
    label = tk.Label(frame, text=f"Etiqueta {i}")
    label.pack()

# Configurar la función de desplazamiento del canvas
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_canvas_configure)

# Configurar la función de desplazamiento al utilizar la scrollbar
def on_scrollbar_scroll(*args):
    canvas.xview(*args)

scrollbar.config(command=on_scrollbar_scroll)

# Iniciar el bucle de eventos
ventana.mainloop()