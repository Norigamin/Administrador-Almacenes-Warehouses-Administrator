class Section:
    def __init__(self, id, nombre, tipo_producto, detalles):
        self.id = id
        self.nombre = nombre
        self.tipo_producto = tipo_producto
        self.detalles = detalles
        self.productos = []

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def gettipo_producto(self):
        return self.tipo_producto

    def settipo_producto(self, tipo_producto):
        self.tipo_producto = tipo_producto

    def getProductos(self):
        return self.productos

    def agregarProducto(self, producto):
        self.productos.append(producto)
