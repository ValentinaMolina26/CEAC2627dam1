print("Social Media Agenda v0.1")
print("Valentina Molina")

while True:
    print("Escoge una opcion")
    print("1.-Insertar un registro")
    print("2.-Listado de registros")
    
    opcion = input("Indica tu opción: ")
    
    if opcion == "1":
        nombre_de_la_empresa = input("Introduce nombre de la empresa: ")
        contacto = input("Introduce unos contactos: ")
        instagram = input("Introduce un instagram: ")
        
        archivo = open("agenda.csv", "a")
        archivo.write(nombre_de_la_empresa + "," + contacto + "," + instagram + "\n")
        archivo.close()
        
    elif opcion == "2":
        archivo = open("agenda.csv", "r")
        lineas = archivo.readlines()
        
        for linea in lineas:
            print(linea)
            
        archivo.close()
