"""
entradas:
valores--->int--->P
Valores--->int--->Q

salidas:
resultado--->int--->res
valores--->int--->P
Valores--->int--->Q

"""

#Entradas
P=int(input("digite un valor: "))
Q=int(input("digite el segundo valor: "))
#Caja negra
res=P**3+Q**4-2*P**2
if(res>680):
    print(f"P y Q satisfacen la expresion: {P} y {Q}")
else:
    print(f"P y Q no satisfacen la expresion:{P} y {Q}")
    