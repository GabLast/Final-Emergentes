#!/usr/bin/env python3

import sys

mesActual = None
montoActual = 0
mesNext = None

for line in sys.stdin:
    # Mostrar el Total Ventas para los Meses Enero y Marzo en la Ciudades de
    # Santiago, La_Vega y Moca.
    line = line.strip()
    mesNext, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if mesActual == mesNext:
        montoActual += monto
    else:
        if mesActual:
            print("%s\t%s\t%d" % (mesActual, montoActual))
        montoActual = monto
        mesActual = mesNext

#last case for last output
if mesActual == mesNext:
    print("%s\t%s\t%d" % (mesActual, montoActual))
