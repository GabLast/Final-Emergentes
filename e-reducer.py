#!/usr/bin/env python

import sys

ciudadActual = None
ciudadNext = None
mesActual = None
montoActual = 0
mesNext = None

for line in sys.stdin:
    # Mostrar el Total Ventas para los Meses Enero y Marzo en la Ciudades de
    # Santiago, La_Vega y Moca.
    line = line.strip()
    ciudadNext, mesNext, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if mesActual == mesNext:
        if ciudadActual == ciudadNext:
            montoActual += monto
    else:
        if mesActual and ciudadActual:
            print("%s\t%s\t%d" % (mesActual, ciudadActual, montoActual))
        montoActual = monto
        ciudadActual = ciudadNext
        mesActual = mesNext

#last case for last output
if ciudadActual == ciudadNext and mesActual == mesNext:
    print("%s\t%s\t%d" % (mesActual, ciudadActual, montoActual))
