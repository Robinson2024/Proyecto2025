#excepciones

numero = 1
numero_2 = "5"
numero_3 = 10

try:
    print(numero + numero_2)
    print("no se ha producido error")    
except:
    print("No se puede sumar un número con una cadena")
else:
    print("La suma se ha realizado correctamente")
finally:
    print("la ejecucion continua")
    
    
#excepciones 2

numero = 11
numero_2 = "5"
numero_3 = 10

try:
    print(numero + numero_2)
    print("no se ha producido error")    
except ValueError:
    print("error value error")
except TypeError as error: #se puede guardar el error en una variable
    print(error) 
finally:
    print("la ejecucion continua")
