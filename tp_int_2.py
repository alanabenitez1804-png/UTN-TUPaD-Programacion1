#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

#usuario y contraseña predefinidos 
usuario="alumno"
contraseña="python123"

for i in range (1,3+1):
    
    u=input("ingrsar usuario: ")
    c=input("ingrear contraseña: ")
    
    if u==usuario and c==contraseña:
        print(f"intento {i}/3 - usuario: {u}")
        print(f"contraseña: {c}")
        print("acceso concedido ")
        break
    else:
        print(f"intento {i}/3 - usuario: {u}")
        print(f"contraseña: {c}")
        print("credenciales invalida")
        
    
    if i>=3: 
        print("cuenta bloqeada")
        

if u==usuario and c==contraseña:
    opcion= " "
         
    while opcion!="4":
        print("\n1-Ver estado de la inscripcion")
        print("2-Cambiar clave")
        print("3-Mostar mensaje motivacional")
        print("4-Salir") 
           
        
        opcion= (input("ingresar la opcion que desea:"))
    
    
        while not opcion.isdigit() or int(opcion)<1 or int(opcion)>4 :
            print("Error: ingrese un numero valido")
            opcion=input("ingresar la opcion que desea:")
        
        if opcion=="1":
            print("Inscripto")
        
        if opcion=="2":
            nc=input("ingrese la nueva clave")
            
            if len(nc)==6:
                v_nc=input("ingresa nuevamente la contraseña para verificación")
            
                if nc==v_nc:
                    print("Nueva contraseña creada")
            else:
                print("contraseña rechaza")
                
        if opcion=="3":
            print("Si puedes imaginarlo puedes programarlo ")
        
        
        
         

        
    
        
        
        
    
        
        