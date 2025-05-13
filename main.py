from datetime import date, datetime
from tkinter import *
from tkinter import ttk

# tkinter básico
root = Tk()
root.title("Diario personal")
ttk.Button(root, text="Añadir nota").grid(column=1, row=2)
root.mainloop()


# Llamada a la fecha y el ahora
today = date.today()
now = datetime.now()

# Programa visible
print(now)
print("¿Cómo estás hoy?")
respuesta = input()

# Escribiendo en el archivo
archivo = open("diario.txt", "a")
archivo.write("\n" + str(now) + "\n" + respuesta + "\n")

archivo.close()
