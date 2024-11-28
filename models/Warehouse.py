class Warehouse:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.secciones = []

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getSecciones(self):
        return self.secciones

    def agregarSeccion(self, seccion):
        self.secciones.append(seccion)
