def suma_dos_numeros(first_number, second_number):
    first_number = int(first_number)  # Convierte first_number a entero
    second_number = int(second_number)  # Convierte second_number a entero
    result = first_number + second_number  # Realiza la suma
    print("La suma es:", result)  # Imprime el resultado
    return result  # Devuelve el resultado

suma_dos_numeros(100, 1)

def sum_dosnumeros_con_return(first_number, second_number):
    return first_number + second_number

result = sum_dosnumeros_con_return(100, 50)
print("La suma es:", result)

def saludar():
    print("¡Hola, mundooo!")
    return saludar
# Llamada a la función
saludar()

def suma():
    numero_1 = 1000
    numero_2 = 20
    resultado = numero_1 + numero_2
    return resultado
print(suma())
    
def print_name (name, surname):
    print(name, surname)
    return print_name
print_name("Juan", "Perez")

def print_texto(*text): # *text es un argumento de longitud variable que se convierte en una tupla
    print(text)
    return print_texto
print_texto("Hola, mundo!")
print_texto("Hola", "mundo", "cruel")  
print_texto("Hola", "mundo", "cruel", "y", "despiadado", "jajaja")

