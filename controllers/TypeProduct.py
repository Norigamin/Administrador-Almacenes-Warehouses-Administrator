from tkinter import ttk, messagebox, Label, Tk

class TypeProduct:
    def __init__(self, ventana, x_desplegable: int, y_desplegable: int):
        self.ventana = ventana
        self.x_desplegable = x_desplegable
        self.y_desplegable = y_desplegable

        self.widgets_dinamicos = []
        # Titulo
        Label(ventana, text="Tipo de Producto:").place(x=x_desplegable - 3, y=y_desplegable - 30)
        # Lista de opciones 
        self.lista_tipo_producto = ["Alimento", "Tecnología", "Ropa"]

        # Crear Combobox de tipo de producto
        self.desplegable_tipo_producto = ttk.Combobox(ventana, values=self.lista_tipo_producto, state="readonly", width=12)
        self.desplegable_tipo_producto.place(x=x_desplegable, y=y_desplegable)

        self.desplegable_tipo_producto.bind("<<ComboboxSelected>>", self.tipo_producto)

        # Atributos para los comboboxes dinámicos
        self.desplegable_talla = None
        self.desplegable_garantia = None
        self.desplegable_dia = None
        self.desplegable_mes = None
        self.desplegable_anio = None

    def eliminar_widgets(self):
        for widget in self.widgets_dinamicos:
            widget.destroy()
        self.widgets_dinamicos.clear()
        
    def tipo_producto(self, event):
        y_desplegable = self.y_desplegable
        x_desplegable = self.x_desplegable

        seleccion = self.desplegable_tipo_producto.get()
        self.eliminar_widgets()

        # Inicializar los Combobox dinámicos según el tipo de producto seleccionado
        if seleccion == "Tecnología":
            label = Label(self.ventana, text="¿Este Producto Tiene Garantía?")
            label.place(x=x_desplegable - 3, y=y_desplegable + 50)
            self.widgets_dinamicos.append(label)

            self.desplegable_garantia = ttk.Combobox(self.ventana, values=["SI", "NO"], state="readonly", width=3)
            self.desplegable_garantia.place(x=x_desplegable, y=y_desplegable + 80)
            self.widgets_dinamicos.append(self.desplegable_garantia)

        elif seleccion == "Ropa":
            ropa_label = Label(self.ventana, text="Elija la talla:")
            ropa_label.place(x=x_desplegable - 3, y=y_desplegable + 50)
            self.widgets_dinamicos.append(ropa_label)

            self.desplegable_talla = ttk.Combobox(self.ventana, values=["S", "M", "L", "XL", "XXL"], state="readonly", width=6)
            self.desplegable_talla.place(x=x_desplegable, y=y_desplegable + 80)
            self.widgets_dinamicos.append(self.desplegable_talla)

        elif seleccion == "Alimento":
            alimento_label = Label(self.ventana, text="Elija la fecha de caducidad DD/MM/AA:")
            alimento_label.place(x=x_desplegable - 15, y=y_desplegable + 50)
            self.widgets_dinamicos.append(alimento_label)

            self.desplegable_dia = ttk.Combobox(self.ventana, values=[dia for dia in str(range(1, 32)) if dia < 10 in dia], state="readonly", width=3)
            self.desplegable_dia.place(x=x_desplegable, y=y_desplegable + 80)
            self.widgets_dinamicos.append(self.desplegable_dia)
            
            self.desplegable_mes = ttk.Combobox(self.ventana, values=[mes for mes in range(1, 13)], state="readonly", width=3)
            self.desplegable_mes.place(x=x_desplegable + 60, y=y_desplegable + 80)
            self.widgets_dinamicos.append(self.desplegable_mes)

            self.desplegable_anio = ttk.Combobox(self.ventana, values=[anio for anio in range(2024, 2100)], state="readonly", width=6)
            self.desplegable_anio.place(x=x_desplegable + 120, y=y_desplegable + 80)
            self.widgets_dinamicos.append(self.desplegable_anio)
            
if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry("300x200")
    TypeProduct(ventana, 50, 50)
    ventana.mainloop()