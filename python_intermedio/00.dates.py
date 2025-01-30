#dates
from datetime import datetime

ahora = datetime.now()
print(ahora) 

marcaDeTiempo = ahora.timestamp()
print("Timestamp:", marcaDeTiempo)


año_2100 = datetime(2100, 1, 1, 4, 5, 15)

año = datetime.now().year
mes = datetime.now().month
dia = datetime.now().day
hora = datetime.now().hour
print("Año:", año)
print("Mes:", mes)
print("Día:", dia)

print(año_2100)

from datetime import time

hora = time(10, 30, 15)
print(hora)

from datetime import date

print(date.today())
print(date.today().year)
print(date.today().month)
print(date.today().day)
