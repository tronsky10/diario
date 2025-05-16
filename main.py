from datetime import date, datetime
from tkinter import *
from tkinter import ttk


def guardar_nota():
    """
    Función para guardar la nota del textarea en un archivo.
    """
    now = datetime.now()
    fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")  # Formato de fecha y hora
    respuesta = textarea.get("1.0", END)  # Obtiene el texto del textarea
    # El índice "1.0" significa desde el primer carácter de la primera línea
    # END es una constante que significa "hasta el final" del texto.

    try:
        with open("diario.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"\n{fecha_hora}\n{respuesta}\n")
        print("Nota guardada correctamente.")  # Para feedback en la consola
    except Exception as e:
        print(f"Error al guardar la nota: {e}")  # Manejo de errores

    # Borra el contenido del textarea después de guardar
    textarea.delete("1.0", END)


# tkinter básico
root = Tk()
root.title("Diario personal")
root.geometry("600x400")

# Usamos un Frame para organizar mejor los widgets
content = ttk.Frame(root, padding=(3, 3, 12, 12))
content.grid(column=0, row=0, sticky=(N, W, E, S))  # El Frame se expande con la ventana

# Configuración para que la ventana se redimensione correctamente
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)  # La columna del textarea se expande
content.rowconfigure(1, weight=1)  # La fila del textarea se expande

# Añadimos el widget Text, que es el equivalente al textarea
textarea = Text(content, wrap=WORD)  # wrap=WORD hace que el texto se ajuste a la línea
textarea.grid(column=0, row=1, sticky=(N, W, E, S))  # El textarea se expande

# Añadimos el botón "Añadir nota"
boton_guardar = ttk.Button(content, text="Guardar", command=guardar_nota)
boton_guardar.grid(column=0, row=2, sticky=(S))  # El botón se alinea abajo

# Llamada a la fecha y la hora (ya no es necesario imprimir en la consola)
today = date.today()
now = datetime.now()
root.mainloop()
