from classEstudiante import *

alumno = Estudiantes(input("Ingrese su nombre: "),
                    input("ingrese su edad: "),
                    input("ingrese su carrera: "),
                    input("ingrese su año de ingreso: "),
                    input("ingrese su promedio: "))

def menu():
    print("sistema universitario")
    print("1 regustrar estudiantes")
    print("2 consultar estudiante")
    print("3 actualizar promedio")
    print ("4 cambiar carrera")
    print("5 salir")



while True:
    menu()
    opcion= input("elegi una opcion")
    if opcion == 1:
        nombre= input("ingrese su nombre")
        while True:
            edad=int(input("ingrese su edad"))
            if edad >=17:
        else:
            print("erro, debe tener 17 años o mas")
     carrera = input("Ingrese su carrera")
        anio = int(input("Ingrese su año de ingreso"))
        promedio = float(input("ingrese su promedio"))
        alumno = Estudiantes(nombre, edad, carrera, año, promedio)
        print("Estudiante registrado correctamente.")
    elif opcion == "2":

        if alumno != "":
            alumno.consultar()
        else:
            print("No hay estudiantes registrados.")
    elif opcion == "3":
        if alumno != "":
            nuevo = float(input("ingrese el nuevo promedio: "))
            alumno.actualizar_promedio(nuevo)
        else:
            print("primero registre un estudiante.")
    elif opcion == "4":
        if alumno != "":
            nueva = input("ingrese la nueva carrera: ")
            alumno.cambiar_carrera(nueva)
        else:
            print("primero registre un estudiante.")
    elif opcion == "5":
        print("saliendo")
    else:
        print("opcion incorrecta")
