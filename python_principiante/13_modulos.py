#modulos
import python_principiante.modulo as modulo


modulo.sum(10, 20, 30)
modulo.printValue("Hola, mundo!")

from python_principiante.modulo import sum, printValue #importar funciones especificas de un modulo

sum(1000, 20, 30)
printValue("Hola, mundo importado!")