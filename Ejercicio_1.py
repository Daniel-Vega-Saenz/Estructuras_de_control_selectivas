"""
entradas:
COP-->float--->dinero
interes-->int--->tasa
salida:
resultado--->float--->interes
"""
#Entradas
dinero=float(input("Ingrese la cantidad de dinero que va a invertir:"))
tasa=int(input("Ingrese la tasa de interes en porcentaje: "))
#caja negra
interes=dinero*(tasa/100)
if(interes>100000):
    print(f"Usted genero {interes} asi que su dinero sera reinverido")
else:
    print(f"Usted genero {interes} asi que su dinero no sera reinvertido")
