#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Total Ventas x Cada Mes
    line = line.strip()
    ciudad, mes, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if mes:
        print("%s %d" % (mes, monto))
