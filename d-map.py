#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Ciudad con Mayor Venta
    line = line.strip()
    ciudad, mes, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if ciudad:
        print("%s %d" % (ciudad, monto))
