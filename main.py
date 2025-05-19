from datetime import date, datetime
from tkinter import *
from tkinter import ttk

# tkinter básico
root = Tk()
root.title("Diario personal")
root.geometry("400x400")

# Configurando la posición de los elementos
content = ttk.Frame(root, padding=(50, 50, 40, 40))
content.grid(column=0, row=0, sticky=(N, W, E, S))


root.mainloop()
