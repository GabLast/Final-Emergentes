#!/usr/bin/env python

# import sys
#
# ciudadActual = None
# montoActual = 0
# ciudadNext = None
#
# ciudadMayor = None
# montociudadMayor = 0
#
# flag = False
#
# for line in sys.stdin:
#     # Ciudad con Mayor Venta
#     line = line.strip()
#     ciudadNext, monto = line.split(" ")
#
#     try:
#         monto = int(monto)
#     except ValueError:
#         continue
#
#     if ciudadActual == ciudadNext:
#         montoActual += monto
#     else:
#         if ciudadActual:
#             if not flag:
#                 montociudadMayor = montoActual
#                 ciudadMayor = ciudadActual
#
#             elif montoActual > montociudadMayor:
#                 montociudadMayor = montoActual
#                 ciudadMayor = ciudadActual
#
#         montoActual = monto
#         ciudadActual = ciudadNext
#
#
# if ciudadMayor:
#     print("Ciudad de Monto Mayor: %s\t\t\t%d" % (ciudadMayor, montociudadMayor))
import sys

ciudad_actual = None
ciudad_mayor = None
monto_actual = 0
monto_mayor = 0
ciudad = None
primero = True

for line in sys.stdin:
    line = line.strip()
    ciudad, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if ciudad_actual == ciudad:
        monto_actual += monto
    else:
        if ciudad_actual:
            if primero:
                monto_mayor = monto_actual
                ciudad_mayor = ciudad_actual
            elif monto_actual > monto_mayor:
                monto_mayor = monto_actual
                ciudad_mayor = ciudad_actual
            primero = False

        ciudad_actual = ciudad
        monto_actual = monto

if ciudad_actual == ciudad:
    print
    "%s %d" % (ciudad_mayor, monto_mayor)