#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Total Ventas x Cada Ciudad en los meses de Mayo, Julio y Diciembre.
    line = line.strip()
    ciudad, mes, monto = line.split(" ")

    try:
        monto = int(monto)
        mesUp = mes.upper()
    except ValueError:
        continue

    if mesUp == 'MAYO' or mesUp == 'JULIO' or mesUp == 'DICIEMBRE':
        print("%s %d" % (ciudad, monto))
