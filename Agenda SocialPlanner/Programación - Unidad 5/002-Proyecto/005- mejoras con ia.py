print("╔══════════════════════════════════════════╗")
print("║                                          ║")
print("║       ✨ SOCIAL MEDIA AGENDA ✨          ║")
print("║              VERSION 0.1                ║")
print("║                                          ║")
print("║          Creative tools for you          ║")
print("║                                          ║")
print("║           by Valentina Molina             ║")
print("║                                          ║")
print("╚══════════════════════════════════════════╝")

while True:
    print()
    print("┌──────────────────────────────────────────┐")
    print("│              💜 MENÚ PRINCIPAL           │")
    print("├──────────────────────────────────────────┤")
    print("│                                          │")
    print("│    [1] ✨  Añadir una empresa             │")
    print("│    [2] 📋  Ver agenda                     │")
    print("│                                          │")
    print("└──────────────────────────────────────────┘")

    opcion = input("  💫 Elige una opción: ")

    if opcion == "1":
        print()
        print("╭──────────────────────────────────────────╮")
        print("│           ✨ NUEVO REGISTRO               │")
        print("╰──────────────────────────────────────────╯")

        nombre_de_la_empresa = input("  🏢 Nombre de la empresa: ")
        contacto = input("  📩 Contacto: ")
        instagram = input("  📸 Instagram: ")

        archivo = open("agenda.csv", "a")
        archivo.write(nombre_de_la_empresa + "," + contacto + "," + instagram + "\n")
        archivo.close()

    elif opcion == "2":
        print()
        print("╭──────────────────────────────────────────╮")
        print("│             📋 TU AGENDA                  │")
        print("╰──────────────────────────────────────────╯")

        archivo = open("agenda.csv", "r")
        lineas = archivo.readlines()

        for linea in lineas:
            print("  ✦ " + linea)

        archivo.close()

