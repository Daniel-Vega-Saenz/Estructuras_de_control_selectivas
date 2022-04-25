"""
entradas
num--->int--->catg
salida
valor_salario--->float--->salario_F

"""

#Entradas
catg=int(input("Ingrese su categoria: "))
#caja negra
if(catg==1):
    Salario1=5000000*0.10
    salario_F=5000000+Salario1
if(catg==2):
    Salario2=4300000*0.15
    salario_F=4300000+Salario2
if(catg==3):
    Salario3=3600000*0.20
    salario_F=3600000+Salario3
if(catg==4):
    Salario4=2000000*0.40
    salario_F=2000000+Salario4
if(catg==5):
    Salario5=900000*0.60
    salario_F=900000+Salario5
#Salidas
print(f"con categoria {catg}, su salario es de: {salario_F}")