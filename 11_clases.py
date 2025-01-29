#clases

class MyEmptyPerson: #clase vacia
    pass #permite que no de error si no hay nada en la clase, para implementar despues.

print(MyEmptyPerson())

class Persona:
    def __init__(self, nombre, edad, nacimiento):  # Constructor de la clase
        self.nombre = nombre  # Se guarda el nombre en el objeto
        self.edad = edad      # Se guarda la edad en el objeto
        self.nacimiento = nacimiento # Se guarda el nacimiento en el objeto
        
    def walk(self):  # Método de la clase
        print(f"{self.nombre} {self.edad} está caminando")# Imprime el nombre del objeto y el mensaje
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nacimiento: {self.nacimiento}")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 25, 1995)
persona2 = Persona("Ana", 30, 1990)

# Llamar al método mostrar_info para ver los datos
persona1.mostrar_info()  
persona2.mostrar_info()
Persona.walk(persona1)  # Llamar al método walk del objeto persona1
Persona.walk(persona2)  # Llamar al método walk del objeto persona2

