#manejo de ficheros
import os

with open("archivo.txt", "w") as f:
    f.write("Este es un archivo nuevo.\n")
    f.write("Cada ejecución borra el contenido anterior.\n")

with open("archivo.txt", "r") as f:
    contenido = f.read()  # Lee todo el contenido del archivo
    print(contenido)
    
with open("archivo.txt", "r") as f:
    for linea in f:
        print(linea.strip())  # strip() elimina saltos de línea extras

with open("archivo.txt", "r") as f:
    primera_linea = f.readline()  # Lee solo una línea
    print(primera_linea.strip())
    
with open("archivo.txt", "r") as f:
    lineas = f.readlines()  # Devuelve una lista con todas las líneas
    print(lineas)
    
    """
    if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")
    print("Archivo eliminado.")
else:
    print("El archivo no existe.")
    """
    


"""
import json
# Guardar datos en un archivo JSON
datos = {"nombre": "Juan", "edad": 30}

with open("datos.json", "w") as f:
    json.dump(datos, f, indent=4)  # `indent=4` para que sea más legible

# Leer datos de un archivo JSON
with open("datos.json", "r") as f:
    datos_cargados = json.load(f)

print(datos_cargados)
"""