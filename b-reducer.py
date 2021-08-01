#!/usr/bin/env python3

import sys

mesActual = None
montoActual = 0
mesNext = None

for line in sys.stdin:
    # Total Ventas x Cada Mes
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
            print("%s\t%d" % (mesActual, montoActual))
        montoActual = monto
        mesActual = mesNext

#last case for last output
if mesActual == mesNext:
    print("%s\t\t\t%d" % (mesActual, montoActual))
