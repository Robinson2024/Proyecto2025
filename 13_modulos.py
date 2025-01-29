#modulos
import modulo


modulo.sum(10, 20, 30)
modulo.printValue("Hola, mundo!")

from modulo import sum, printValue #importar funciones especificas de un modulo

sum(1000, 20, 30)
printValue("Hola, mundo importado!")