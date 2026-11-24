class Estudiantes:
    def __init__(self, nombre, edad, carera, año_de_ingreso, promedio):
        self.nombre=nombre
        self.edad=edad
        self.carera=carera
        self.año_de_ingreso=año_de_ingreso
        self.promedio=promedio

    def consultar(self):
        print("datos del estudiante")
        print("nombre", self.nombre)
        print("edad", self.nombre)
        print("carrera", self.carera)
        print("año de ingreso", self.año_de_ingreso)
        print("promedio",self.promedio)

    def actualizar_promedio(self, nuevo):
        self.promedio= nuevo
        print("promedio actualizado")
        
    def cambiar_carrera(self, nuevo):
        self.carrera=nuevo
        print("carrera actualizada")
