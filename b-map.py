#!/usr/bin/env python3

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
        print("%s %d" % (mes.upper(), monto))
