#Ejercicio 3 (Alta) — “Agenda de Turnos con 
#Nombres (sin listas)”
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha():
    print("Error: solo letras")
    operador = input("Ingrese el nombre del operador: ")

opcion = ""

while opcion != "5":
    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Salir") 
    
    opcion = input("Opción: ")
    
    while not opcion.isdigit() or int(opcion) < 1 or int():
        print("Error: opción inválida")
        opcion = input("Opción: ")
    
    if opcion == "1":
        dia = input("Día (1=Lunes, 2= Martes): ")
        
        while not dia.isdigit() or int(dia) not in [1,2]:
            print("ERROR")
            dia = input("Día (1=Lunes, 2= Martes): ")
            
        nombre=input("Nombre del paciente: ")
        
        while not nombre.isalpha():
            print("Error: solo letras")
            nombre=input("Nombre del paciente: ")
        
        repetido = False

        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                repetido = True
        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                repetido = True

        if repetido:
            print("Error: paciente ya existe")
        else:
            if dia == "1":
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay cupos en Lunes")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay cupos en Martes")
    elif opcion == "2":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre a cancelar: ")

        while not nombre.isalpha():
            print("Error")
            nombre = input("Nombre a cancelar: ")     
            
        encontrado = False

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado")
        else:
            print("No se encontró el paciente")              
    elif opcion == "3":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error")
            dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")
    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("Lunes ocupados:", ocupados_lunes, "Disponibles:", 4 - ocupados_lunes)
        print("Martes ocupados:", ocupados_martes, "Disponibles:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")
    