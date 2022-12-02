#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, date, time, timedelta
import calendar

formato1 = "%d-%m-%Y"
cadena_inicio = "01-12-2020"
fecha_inicio = datetime.strptime(cadena_inicio, formato1)
ahora = datetime.now()  # Obtiene fecha y hora actual
hoy = date.today()
print("Fecha y Hora:", ahora)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow())  # Muestra fecha/hora UTC
print("Dia:",ahora.day)  # Muestra dia
print("Mes:",ahora.month)  # Muestra mes
print("ANIO:",ahora.year)  # Muestra aNIo
print("Hora:", ahora.hour)  # Muestra hora
print("Minutos:",ahora.minute)  # Muestra minuto
#print("Segundos:", ahora.second)  # Muestra segundo
#print("Microsegundos:",ahora.microsecond)  # Muestra microsegundo
diferencia = ahora - fecha_inicio
print("Diferencia: ", diferencia)
objeto_datetime = datetime.strptime(cadena_inicio, formato1)
print("strptime de fecha Inicio:", fecha_inicio.strftime(formato1))
print("Cadena inicio", cadena_inicio)
print("#####################")
# Asigna datetime de la fecha actual
fecha1 = datetime.now()

# Asigna datetime específica
fecha2 = datetime(2020, 12, 01, 06, 00, 00)
diferencia = ahora - fecha2
print("Fecha1:", fecha1)
print("Fecha2:", fecha2)
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay ", 
      diferencia.days, 
      "días y ", 
      diferencia.seconds, 
      "seg.")
print("Otra dif:", float((datetime.now()-datetime(2020, 12, 01, 06, 00, 00)).days))