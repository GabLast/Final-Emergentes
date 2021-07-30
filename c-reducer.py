#!/usr/bin/env python

# import sys
#
# mesActual = None
# montoActual = 0
# mesNext = None
#
# mesMayor = None
# montoMesMayor = 0
# mesMenor = None
# montoMesMenor = 0
# flag = False
#
# for line in sys.stdin:
#     # Mes con Mayor y Menor Venta
#     line = line.strip()
#     mesNext, monto = line.split(" ")
#
#     try:
#         monto = int(monto)
#     except ValueError:
#         continue
#
#     if mesActual == mesNext:
#         montoActual += monto
#     else:
#         if mesActual:
#             if not flag:
#                 montoMesMenor = montoActual
#                 montoMesMayor = montoActual
#
#                 mesMayor = mesActual
#                 mesMenor = mesActual
#
#                 flag = True
#             elif montoActual > montoMesMayor:
#                 montoMesMayor = montoActual
#                 mesMayor = mesActual
#
#             elif montoActual < montoMesMenor:
#                 montoMesMenor = montoActual
#                 mesMenor = mesActual
#
#         montoActual = monto
#         mesActual = mesNext
#
#
# if mesMayor and mesMenor:
#     print("Mes y monto mayor: %s\t\t\t%d\n"
#           "Mes y monto menor: %s\t\t\t%d" % (mesMayor, montoMesMayor, mesMenor, montoMesMenor))

import sys

mes_actual = None
mes_mayor = None
mes_menor = None
monto_actual = 0
monto_mayor = 0
monto_menor = 0
mes = None
primero = True

for line in sys.stdin:
    line = line.strip()
    mes, monto = line.split(" ")

    try:
        monto = int(monto)
    except ValueError:
        continue

    if mes_actual == mes:
        monto_actual += monto
    else:
        if mes_actual:
            if primero:
                monto_mayor = monto_actual
                monto_menor = monto_actual
                mes_mayor = mes_actual
                mes_menor = mes_actual
                primero = False
            elif monto_actual > monto_mayor:
                monto_mayor = monto_actual
                mes_mayor = mes_actual
            elif monto_actual < monto_menor:
                monto_menor = monto_actual
                mes_menor = mes_actual

        mes_actual = mes
        monto_actual = monto

if mes_actual == mes:
    print("Menor: %s %d\tMayor: %s %d" % (mes_menor, monto_menor, mes_mayor, monto_mayor))
