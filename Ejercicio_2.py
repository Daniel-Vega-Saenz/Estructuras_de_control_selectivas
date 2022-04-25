"""
entradas
Salario bruto--->float---> S
salida
Salario final--->float---> Sf

"""
# Entradas
s=float(input("Ingrese su salario bruto: "))
#Caja negra
s1=s*0.15
s2=s*0.12
if(s<900000):
    sf=s+s1
else:
    sf=s+s2
#Salidas
print(f"su salario final sera de: {sf}")