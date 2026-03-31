#Ejercicio 5 — “Escape Room:"La Arena del 
#Gladiador"

# PASO 1: NOMBRE
 

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

print("\n=== INICIO DEL COMBATE ===")

# PASO 2: VARIABLES

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_jugador = True

# PASO 3: COMBATE

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("\n1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido")
        opcion = input("Opción: ")

    # ACCIÓN 1: ATAQUE PESADO
    if opcion == "1":
        danio = danio_base

        if vida_enemigo < 20:
            danio = danio_base * 1.5

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    # ACCIÓN 2: RÁFAGA VELOZ
    # ========================
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # ACCIÓN 3: CURAR
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 HP")
        else:
            print("¡No quedan pociones!")

    # TURNO DEL ENEMIGO

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")

# PASO 4: RESULTADO FINAL

print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")