#!/usr/bin/env python

import sys

ciudadActual = None
montoActual = 0
ciudadNext = None

ciudadMayor = None
montoCiudadMayor = 0

flag = False

for line in sys.stdin:
    # Ciudad con Mayor Venta
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
            if not flag:
                montoCiudadMayor = montoActual
                ciudadMayor = ciudadActual

            if montoActual > montoCiudadMayor:
                montoCiudadMayor = montoActual
                ciudadMayor = ciudadActual

        montoActual = monto
        ciudadActual = ciudadNext


if ciudadMayor:
    print("Ciudad de Monto Mayor: %s\t\t\t%d" % (ciudadMayor, montoCiudadMayor))
