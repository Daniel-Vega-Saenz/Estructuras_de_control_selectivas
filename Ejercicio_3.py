"""
entradas:
Valor1-->int---> A
Valor2-->int---> B
Valor3-->int---> C
Valor4-->int---> D
Saladas:
operacion--->int--->Resul

"""

#Entradas
A=int(input("Digite A: "))
B=int(input("Digite B: "))
C=int(input("Digite C: "))
D=int(input("Digite D: "))
#caja negra
if(D>=0):
    Resul=((A-C)**2)
else:
    Resul=((A-B)**3/D)
#Salidas
print(f"El resultado de las expresiones ingresadas es: {Resul}")