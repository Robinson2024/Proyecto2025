#desafios

#1. Crear un programa que le pida al usuario su nombre 
# y edad, y luego imprima esos datos en la consola.

def print_name_age(name, age):
    print(name, age)
    return print_name_age

print_name_age("Juan", 30) 

#2. Crear un programa que le pida al usuario ingresar 3 números enteros,
# y luego imprima el promedio de los tres números.

def promedio_tres_numeros(num1, num2, num3):
    return (num1 + num2 + num3) / 3
print(promedio_tres_numeros(10, 20, 30))

#3. Crear un programa que le pida al usuario la longitud
# de los dos catetos de un triángulo rectángulo, 
# y luego muestre en la consola el valor de la hipotenusa.

def hipotenusa(cateto1, cateto2):
    return (cateto1 ** 2 + cateto2 ** 2) ** 0.5 #formula de pitagoras
print(hipotenusa(3, 4))

#4. Crear un programa que le pida al usuario el radio de un círculo
# y luego muestre en la consola el área y el perímetro del círculo.

def area_perimetro_circulo(radio):
    pi = 3.1416
    area = pi * radio ** 2
    perimetro = 2 * pi * radio
    return area, perimetro
print(area_perimetro_circulo(5))

#5. Crear un programa que le pida al usuario el valor de la base y la altura
# de un triángulo, y luego muestre en la consola el área del triángulo.

def area_triangulo(base, altura):
    return (base * altura) / 2
print(area_triangulo(10, 5))

#6. Crear un programa que le pida al usuario el precio de un producto,
# el porcentaje de descuento, y luego muestre en la consola el precio final
# con el descuento aplicado.

def precio_final(precio, descuento):
    return precio - (precio * descuento / 100) #formula de descuento
print(precio_final(100, 10))

#7. Crear un programa que le pida al usuario el precio de un producto y la cantidad 
# que desea llevar, y luego muestre en la consola el monto total de la compra.

def monto_total(precio, cantidad):
    return precio * cantidad
print(monto_total(100, 5))

#8. Crear un programa que le pida al usuario tres números y luego muestre en la consola
# el mayor de los tres.

def mayor_de_tres(num1, num2, num3):
    return max(num1, num2, num3)
print(mayor_de_tres(10, 20, 30))

#9. Crear un programa que le pida al usuario tres números y luego muestre en la consola
# el menor de los tres.

def menor_de_tres(num1, num2, num3):
    return min(num1, num2, num3)
print(menor_de_tres(10, 20, 30))

#10. Crear un programa que le pida al usuario un número y luego muestre en la consola
# si el número es par o impar.

def par_impar(num):
    if num % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"
print(par_impar(5))
print(par_impar(10))

#11. Crear un programa que le pida al usuario un número y luego muestre en la consola
# si el número es primo o no.

def es_primo(num):
    if num < 2:
        return "No es primo"
    for i in range(2, num):
        if num % i == 0:
            return "No es primo"
    return "Es primo"
print(es_primo(5))
print(es_primo(10))

#12. Crear un programa que le pida al usuario una palabra y luego muestre en la consola
# una a una las letras de la palabra introducida.

def letras_palabra(palabra_por_recibir): # Recibe "Hola"
    letras = [letra for letra in palabra_por_recibir]  # Lista de letras de la palabra "Hola"
    return letras  # Devuelve ['H', 'o', 'l', 'a']

print(letras_palabra("Hola"))  # ['H', 'o', 'l', 'a']

#13. Crear un programa que le pida al usuario una palabra y luego muestre en la consola
# la palabra invertida.

def palabra_invertida(palabra_por_recibir): # Recibe "Hola"
    palabra_invertida = palabra_por_recibir[::-1]  # Invierte la palabra "Hola" tecnica de slicing
    return palabra_invertida  # Devuelve "aloH"

#14. Crear un programa que le pida al usuario una palabra y luego muestre en la consola
# el número de vocales que tiene esa palabra.

def contar_vocales(palabra_por_recibir): # Recibe "Hola"
    vocales = [letra for letra in palabra_por_recibir if letra in "aeiouAEIOU"]  # Lista de vocales de la palabra "Hola"
    return len(vocales)  # Devuelve 2
print(contar_vocales("Hola"))  

#15. Crear un programa que le pida al usuario una palabra y luego muestre en la consola
# el número de consonantes que tiene esa palabra.

def cont_consonantes(palabra_por_recibir):
    consonantes = [letra for letra in palabra_por_recibir if letra not in "aeiouAEIOU"]
    return len(consonantes)
print(cont_consonantes("Hola"))

#16. Crear un programa que le pida al usuario una palabra y luego muestre en la consola
# la misma palabra con todas las vocales reemplazadas por la letra "i".

def reemplazar_vocales(palabra_por_recibir):
    vocales = "aeiouAEIOU"
    for vocal in vocales:
        palabra_por_recibir = palabra_por_recibir.replace(vocal, "i")
    return palabra_por_recibir
print(reemplazar_vocales("Hola"))

#17. Crear un programa que le pida al usuario una palabra y luego muestre en la consola
# la misma palabra con todas las consonantes en mayúsculas.

def consonantes_mayusculas(palabra_por_recibir):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for consonante in consonantes:
        palabra_por_recibir = palabra_por_recibir.replace(consonante, consonante.upper())
    return palabra_por_recibir
print(consonantes_mayusculas("Hola"))


#haz una calculadora que sume, reste, multiplique y divida

def calculadora(operacion, num1, num2):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 == 0:
            return "Error: No se puede dividir por 0"
        return num1 / num2
    else:
        return "Operación no válida"
# Pruebas
print(calculadora("suma", 10, 5))             # Salida: 15
print(calculadora("resta", 10, 5))            # Salida: 5
print(calculadora("multiplicacion", 10, 5))   # Salida: 50
print(calculadora("division", 10, 5))         # Salida: 2.0
print(calculadora("division", 10, 0))         # Salida: Error: No se puede dividir por 0
print(calculadora("potencia", 10, 5))         # Salida: Operación no válida

#haz fibonacci 

def fibonacci(n): # Recibe 10
    a, b = 0, 1 
    for i in range(n): # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        print(a, end=" ") # Imprime a y un espacio
        a, b = (b, a + b )
    print() # Imprime un salto de línea
# Pruebas
fibonacci(10)  # Salida: 0 1 1 2 3 5 8 13 21 34
