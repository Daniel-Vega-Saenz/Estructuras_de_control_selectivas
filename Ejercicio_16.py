import math

#Entradas
a=float(input("Digite A: "))
b=float(input("Digite B: "))
c=float(input("Digite C: "))
#Caja negra
d=b**2-(4*a*c)
if(d<0):
    x1=(-b+math.sqrt(b**2-4*a*c)/2*a)
    x2=(-b-math.sqrt(b**2-4*a*c)/2*a)
if(d==0):
    x1=-b/(2*a)
    x2=x1
if(d>0):
    print("No tiene solucion en los reales")
