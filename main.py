from datetime import date, datetime

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
