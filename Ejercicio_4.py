"""
entradas:
Valor compra--->float--->precio

salidas:
valor empresa--->float--->empresa
valor fabricante--->float--->fabricante
interes fabricante--->float--->total_din
valor banco--->float--->banco

"""

#Entradas
precio=float(input("Ingrese el monto total de la compra: "))
#Caja negra
if(precio>=5000000):
    Empresa=precio*0.55
    banco=precio*0.30
    fabricante=precio*0.15
    interes=fabricante*0.20
    total_din=fabricante+interes
else:
    Empresa=precio*0.70
    banco=0
    fabricante=precio*0.30
    interes=fabricante*0.20
    total_din=fabricante+interes
#salidas
print(f"la cantidad a invertir de los fondos de la empresa es de:{Empresa}")
print(f"La cantidad de dinero que prestara el fabricante sera de: {fabricante}")
print(f"El total de dinero que se devolvera al fabricante sera de: {total_din}")
if(banco!=0):
    print(f"El dinero que prestara el banco sera de: {banco}")

