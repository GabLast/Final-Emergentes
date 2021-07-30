#!/usr/bin/env python

import sys

mesActual = None
montoActual = 0
mesNext = None

mesMayor = None
montoMesMayor = 0
mesMenor = None
montoMesMenor = 0
flag = False

for line in sys.stdin:
    # Mes con Mayor y Menor Venta
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
            if not flag:
                montoMesMenor = montoActual
                montoMesMayor = montoActual

                mesMayor = mesActual
                mesMenor = mesActual

                flag = True
            elif montoActual > montoMesMayor:
                montoMesMayor = montoActual
                mesMayor = mesActual

            elif montoActual < montoMesMenor:
                montoMesMenor = montoActual
                mesMenor = mesActual

        montoActual = monto
        mesActual = mesNext


if mesMayor and mesMenor:
    print("Mes y monto mayor: %s\t%d\n"
          "Mes y monto menor: %s\t%d" % (mesMayor, montoMesMayor, mesMenor, montoMesMenor))
