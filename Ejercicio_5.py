"""
entradas:
valor_ventas1--->float--->VentasDp1
valor_ventas2--->float--->VentasDp2
Valor_ventas3--->float--->VentasDp3
Salida:
total_sueldo1--->float--->total1
total_sueldo2--->float--->total2
total_sueldo3--->float--->total3

"""

#entradas
sueldo=1000000
ventasDp1=float(input("ingrese el valor total de las ventas realizas en el departamento 1: "))
ventasDp2=float(input("ingrese el valor total de las ventas realizas en el departamento 2: "))
ventasDp3=float(input("ingrese el valor total de las ventas realizas en el departamento 3: "))
#Caja negra
Ventas_total=ventasDp1+ventasDp2+ventasDp3
porcentaje=Ventas_total*0.33
if(ventasDp1>porcentaje):
    total1=sueldo+(sueldo*0.20)
else:
    total1=sueldo
if(ventasDp2>porcentaje):
    total2=sueldo+(sueldo*0.20)
else:
    total2=sueldo
if(ventasDp3>porcentaje):
    total3=sueldo+(sueldo*0.20)
else:
    total3=sueldo

#Salidas
print(f"El sueldo del departamento 1 es de {total1}")
print(f"El sueldo del departamento 1 es de {total2}")
print(f"El sueldo del departamento 1 es de {total3}")