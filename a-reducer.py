#!/usr/bin/env python3

import sys

ciudadActual = None
montoActual = 0
ciudadNext = None

for line in sys.stdin:
    # Total Ventas x Cada Ciudad en los meses de Mayo, Julio y Diciembre.
    line = line.strip()
    ciudadNext, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if ciudadActual == ciudadNext:
        montoActual += monto
    else:
        if ciudadActual:
            print("%s\t%d" % (ciudadActual, montoActual))
        montoActual = monto
        ciudadActual = ciudadNext

#last case for last output
if ciudadActual == ciudadNext:
    print("%s\t%d" % (ciudadActual, montoActual))
