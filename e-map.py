#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Mostrar el Total Ventas para los Meses Enero y Marzo en la Ciudades de
    # Santiago, La_Vega y Moca.
    line = line.strip()
    ciudad, mes, monto = line.split(" ")

    try:
        monto = int(monto)
        ciudadUp = ciudad.upper()
        mesUp = mes.upper()
    except ValueError:
        continue

    if mesUp == 'ENERO' or mesUp == 'MARZO':
        if ciudadUp == 'SANTIAGO' or ciudadUp == 'LA_VEGA' or ciudadUp == 'MOCA':
            print("%s %s %d" % (ciudad, mes, monto))
