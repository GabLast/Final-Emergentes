#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Mes con Mayor y Menor Venta
    line = line.strip()
    ciudad, mes, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if mes:
        print("%s %d" % (mes, monto))
