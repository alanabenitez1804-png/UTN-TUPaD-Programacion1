#Ejercicio 4 — “Escape Room: La Bóveda”}
# VARIABLES INICIALES
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# NOMBRE DEL AGENTE
nombre = input("Nombre del agente: ")

while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Nombre del agente: ")

print("\n--- INICIO DEL JUEGO ---")

# BUCLE PRINCIPAL
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print("\nEnergía:", energia, "| Tiempo:", tiempo, "| Cerraduras:", cerraduras_abiertas)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: opción inválida")
        opcion = input("Opción: ")

 
    # OPCIÓN 1: FORZAR
   
    if opcion == "1":
        racha_forzar += 1

        # Regla anti-spam
        if racha_forzar == 3:
            energia -= 20
            tiempo -= 2
            alarma = True
            print("¡La cerradura se trabó! Alarma activada")
        else:
            energia -= 20
            tiempo -= 2

            # Riesgo de alarma si energía baja
            if energia < 40:
                num = input("Riesgo! Elegí número 1-3: ")

                while not num.isdigit() or int(num) not in [1, 2, 3]:
                    print("Error")
                    num = input("Riesgo! Elegí número 1-3: ")

                if num == "3":
                    alarma = True
                    print("¡Se activó la alarma!")

            # Abrir cerradura si no hay alarma
            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura")

    # ========================
    # OPCIÓN 2: HACKEAR
    # ========================
    elif opcion == "2":
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        for i in range(4):
            print("Hackeando...")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura")

     # OPCIÓN 3: DESCANSAR
        elif opcion == "3":
            racha_forzar = 0
            tiempo -= 1
            energia += 15

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("La alarma te afecta, pierdes energía extra")

     
    # BLOQUEO POR ALARMA
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nSistema bloqueado por alarma")
        break

 # RESULTADO FINAL
print("\n--- FIN DEL JUEGO ---")

if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
else:
    print("DERROTA (bloqueo)")
        