import tkinter as tk

# Crear la ventana principal
ventana1 = tk.Tk()
ventana1.title("Ventana 1")

# Crear una segunda ventana
ventana2 = tk.Toplevel(ventana1)
ventana2.title("Ventana 2")

# Crear una tercera ventana
ventana3 = tk.Toplevel(ventana1)
ventana3.title("Ventana 3")

# Función para llevar una ventana al frente
def bring_to_front(window):
    window.lift()

# Botones para llevar las ventanas al frente
button1 = tk.Button(ventana1, text="Traer al frente", command=lambda: bring_to_front(ventana1))
button1.pack()

button2 = tk.Button(ventana1, text="Traer al frente", command=lambda: bring_to_front(ventana2))
button2.pack()

button3 = tk.Button(ventana1, text="Traer al frente", command=lambda: bring_to_front(ventana3))
button3.pack()

# Iniciar el bucle de eventos
ventana1.mainloop()