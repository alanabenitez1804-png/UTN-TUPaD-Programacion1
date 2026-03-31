#Ejercicio 1— “Caja del Kiosco”

nc=input("ingrese su nombre: ")

while not nc.isalpha():
    print("error, ingresar solo letras")
    nc=input("ingrese su nombre: ")

can_p=input("ingresar la cantidad de productos a comprar:")

while not can_p.isdigit() or int(can_p) == 0:
    print("error,ingrsar solo numeros")
    can_p=input("ingresar la cantidad de productos a comprar:")

can_p=int(can_p)

t_sin_desc=0
t_con_desc=0
desc=0
d=0
total=0
for i in range (1, can_p+1): 
    print(f"ingrese el precio del producto {i}")
    precio=float(input())
    resp=input("tiene descuento? (s/n):").lower()
    
    while resp not in ("s", "n"):
        print("error,ingrese s o n")
        resp=input("tiene descuento? (s/n):").lower()
    
    total +=precio
    
    if resp == "s":
        d=precio*0.10
        desc+=d
        t_con_desc += precio - d
    elif resp == "n":
        t_sin_desc += precio
    
    print(f"Producto {i} - precio: {precio} - Descuento (s/n): {resp}")
    
print("----------------------------------------------------------------------")

promedio =total/can_p

print (f"Total sin descuento: {t_sin_desc}")
print (f"Total con descuento: {t_con_desc}")
print (f"Ahorro total: {desc}")
print (f"Promedio por producto {promedio:.2f}")
