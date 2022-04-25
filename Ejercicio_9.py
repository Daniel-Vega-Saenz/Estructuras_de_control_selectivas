"""
entradas
valor_compra--->float--->monto
Comprador--->str--->nombre
salidas
valor_final--->float--->precio_f

"""

#Entradas
monto=float(input("Ingrese el monto de la compra: "))
nombre=str(input("Ingrese su nombre: "))

#caja negra
if(monto<50000):
    precio_f=monto
elif(monto>50000 and monto<=100000):
    precio_f=monto-(monto*0.05)
elif(monto>100000 and monto<=700000):
    precio_f=monto-(monto*0.11)
elif(monto>700000 and monto<=1500000):
    precio_f=monto-(monto*0.18)
elif(monto>1500000):
    precio_f=monto-(monto*0.25)

#Salidas
print(f"Usuario {nombre}, el monto total de su compra fue de {monto} y el valor a pagar sera de {precio_f}")