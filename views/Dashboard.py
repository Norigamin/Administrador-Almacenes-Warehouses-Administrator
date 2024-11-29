from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from models.Warehouse import Warehouse
from models.Section import Section
from models.Product import Product
from controllers.TypeProduct import TypeProduct

class Dashboard:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("MINUTEROS S.A.S - Gestor de Almacenes")
        self.ventana.geometry("1000x650")
        self.ventana.iconbitmap("images/icon.ico")
        self.ventana.resizable(0, 0)

        # Variable
        self.almacenes = []
        self.section_data = {}
        self.warehouse_window_open = False
        self.section_window_open = False 
        self.product_window_open = False 

        # Contadores para IDs
        self.warehouse_id_counter = 1
        self.section_id_counter = 1
        self.product_id_counter = 1

        # Título
        Label(ventana, text="Almacenes", font=("Helvetica", 20, "bold")).place(x=180, y=20)

        # Botones
        Button(ventana, text="Agregar Almacén", command=self.add_warehouse_window).place(x=150, y=310)
        Button(ventana, text="Eliminar Almacén", command=self.delete_warehouse).place(x=260, y=310)
        Button(ventana, text="Agregar Sección", command=self.add_section_window).place(x=600, y=310)
        Button(ventana, text="Eliminar Sección", command=self.delete_section).place(x=700, y=310)
        Button(ventana, text="Buscar Sección",command=self.search_section_window).place(x=800, y=310)

        Button(ventana, text="Agregar Producto",command=self.add_product_window).place(x=230, y=610)
        Button(ventana, text="Eliminar Producto", command=self.delete_product).place(x=340, y=610)
        Button(ventana, text="Buscar Producto",command=self.search_product_window).place(x=450, y=610)
        Button(ventana, text="Editar Producto",command=self.edit_product).place(x=553, y=610)
        Button(ventana, text="Detalles Producto",command=self.mostrarDetalles).place(x=650, y=610)

        # Tabla Almacen
        self.almacen_table = ttk.Treeview(ventana, columns=("ID Almacén", "Nombre", "Ubicación"), show="headings", height=10)
        self.almacen_table.heading("ID Almacén", text="ID Almacén")
        self.almacen_table.heading("Nombre", text="Nombre")
        self.almacen_table.heading("Ubicación", text="Ubicación")
        self.almacen_table.column("ID Almacén", width=100, anchor="center")
        self.almacen_table.column("Nombre", width=180, anchor="center")
        self.almacen_table.column("Ubicación", width=180, anchor="center")
        self.almacen_table.place(x=20, y=70)

        # Apartado SECCIONES
        Label(ventana, text="Secciones", font=("Helvetica", 20, "bold")).place(x=670, y=20)

        self.section_table = ttk.Treeview(ventana, columns=("ID Sección", "Nombre", "Tipo de Producto", "Almacén"), show="headings", height=10)
        self.section_table.heading("ID Sección", text="ID Sección")
        self.section_table.heading("Nombre", text="Nombre")
        self.section_table.heading("Tipo de Producto", text="Tipo de Producto")
        self.section_table.heading("Almacén", text="Almacén")
        self.section_table.column("ID Sección", width=100, anchor="center")
        self.section_table.column("Nombre", width=120, anchor="center")
        self.section_table.column("Tipo de Producto", width=120, anchor="center")
        self.section_table.column("Almacén", width=120, anchor="center")
        self.section_table.place(x=510, y=70)

        # Apartado PRODUCTOS
        Label(ventana, text="Productos", font=("Helvetica", 20, "bold")).place(x=420, y=360)

        self.product_table = ttk.Treeview(ventana, columns=("ID Producto", "Nombre", "Precio","Cantidad de Productos", "Descripción", "Almacén", "Sección"), show="headings", height=8)
        self.product_table.heading("ID Producto", text="ID Producto")
        self.product_table.heading("Nombre", text="Nombre")
        self.product_table.heading("Precio", text="Precio")
        self.product_table.heading("Cantidad de Productos", text="Cantidad de Productos")
        self.product_table.heading("Descripción", text="Descripción")
        self.product_table.heading("Almacén", text="Almacén")
        self.product_table.heading("Sección", text="Sección")
        self.product_table.column("ID Producto", width=100, anchor="center")
        self.product_table.column("Nombre", width=150, anchor="center")
        self.product_table.column("Precio", width=150, anchor="center")
        self.product_table.column("Cantidad de Productos", width=150, anchor="center")
        self.product_table.column("Descripción", width=200, anchor="center")
        self.product_table.column("Sección", width=100, anchor="center")
        self.product_table.column("Almacén", width=100, anchor="center")

        self.product_table.place(x=20, y=410)

    def add_warehouse_window(self):
        if self.warehouse_window_open:
            return

        self.warehouse_window = Toplevel(self.ventana)
        self.warehouse_window.title("MINUTEROS S.A.S")
        self.warehouse_window.geometry("300x230")
        self.warehouse_window.iconbitmap("images/icon.ico")
        self.warehouse_window.resizable(0, 0)
        self.warehouse_window.transient(self.ventana)
        self.warehouse_window.grab_set()
        self.warehouse_window_open = True

        Label(self.warehouse_window, text="Agregar Almacén", font=("Helvetica", 20, "bold")).place(x=30, y=10)
        Label(self.warehouse_window, text="Nombre del Almacén:").place(x=45, y=70)
        self.almacen_nombre = Entry(self.warehouse_window, width=30)
        self.almacen_nombre.place(x=50, y=100)

        Label(self.warehouse_window, text="Ubicación del Almacén:").place(x=45, y=130)
        self.almacen_ubicacion = Entry(self.warehouse_window, width=30)
        self.almacen_ubicacion.place(x=50, y=160)

        Button(self.warehouse_window, text="Agregar", command=self.add_warehouse_button).place(x=120, y=190)

        def window_close():
            self.warehouse_window_open = False
            self.warehouse_window.destroy()

        self.warehouse_window.protocol("WM_DELETE_WINDOW", window_close)

    def add_warehouse_button(self):
        nombre = self.almacen_nombre.get().strip()
        ubicacion = self.almacen_ubicacion.get().strip()

        if not nombre or not ubicacion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        if not nombre.replace(" ", "").isalpha() or "  " in nombre or not ubicacion.replace(" ", "").isalpha() or "  " in ubicacion:
            messagebox.showerror("Error", "Los campos no deben contener números, símbolos o más de un espacio.")
            return

        if nombre and ubicacion:
            nuevo_almacen = Warehouse(self.warehouse_id_counter, nombre, ubicacion)
            self.almacenes.append(nuevo_almacen)
            self.warehouse_id_counter += 1

            messagebox.showinfo("Éxito", "Almacén creado con éxito.")
            self.almacen_table.insert("", "end", values=(nuevo_almacen.id, nuevo_almacen.nombre, nuevo_almacen.ubicacion))
            self.warehouse_window.destroy()
            self.warehouse_window_open = False


    def delete_warehouse(self):
        selected_item = self.almacen_table.selection()
        if not selected_item:
            messagebox.showwarning("Eliminar Almacén", "Seleccione un almacén para eliminar.")
            return
    
        confirm = messagebox.askyesno("Eliminar Almacén", "¿Está seguro de que desea eliminar este almacén?")
        if confirm:
            for item in selected_item:
                warehouse_id = int(self.almacen_table.item(item, "values")[0])
                self.almacenes = [almacen for almacen in self.almacenes if almacen.id != warehouse_id]
                self.almacen_table.delete(item)

    def add_section_window(self):
        if self.section_window_open:
            return

        selected_warehouse = self.almacen_table.selection()

        if not selected_warehouse:
            messagebox.showwarning("Agregar Sección", "Seleccione o Agregue un almacén")
            return
        else:
            self.section_window = Toplevel(self.ventana)
            self.section_window.title("MINUTEROS S.A.S")
            self.section_window.geometry("300x370")
            self.section_window.iconbitmap("images/icon.ico")
            self.section_window.resizable(0, 0)
            self.section_window.transient(self.ventana)
            self.section_window.grab_set()
            self.section_window_open = True

            Label(self.section_window, text="Agregar Sección", font=("Helvetica", 20, "bold")).place(x=30, y=10)
            Label(self.section_window, text="Nombre de la Sección:").place(x=45, y=70)
            self.section_nombre = Entry(self.section_window, width=30)
            self.section_nombre.place(x=50, y=100)

            self.lista_tipo_producto = TypeProduct(self.section_window,50,180)

            Button(self.section_window, text="Agregar", command=self.add_section_button).place(x=120, y=320)

            def window_close():
                self.section_window_open = False
                self.section_window.destroy()

            self.section_window.protocol("WM_DELETE_WINDOW", window_close)

    def add_section_button(self):
        # Validar selección del almacén
        selected_warehouse = self.almacen_table.selection()
        if not selected_warehouse:
            messagebox.showerror("Error", "Debe seleccionar un almacén.")
            return

        # Validar el nombre de la sección
        nombre = self.section_nombre.get().strip()
        if not nombre or not nombre.replace(" ", "").isalpha() or "  " in nombre:
            messagebox.showerror("Error", "El campo 'Nombre de la Sección' no debe estar vacío, contener caracteres no válidos o más de un espacio consecutivo.")
            return

        # Obtener el tipo de producto seleccionado
        lista_tipo_producto = self.lista_tipo_producto.desplegable_tipo_producto.get()
        if not lista_tipo_producto:
            messagebox.showerror("Error", "Debe seleccionar un tipo de producto.")
            return

        # Validar valores dinámicos de ListaTipoProducto según el tipo
        detalles_tipo_producto = {}
        if lista_tipo_producto == "Tecnología":
            desplegable_garantia = self.lista_tipo_producto.desplegable_garantia.get() if self.lista_tipo_producto.desplegable_garantia else None
            if not desplegable_garantia:
                messagebox.showerror("Error", "Debe seleccionar la garantía.")
                return
            detalles_tipo_producto["garantia"] = desplegable_garantia

        elif lista_tipo_producto == "Ropa":
            desplegable_talla = self.lista_tipo_producto.desplegable_talla.get() if self.lista_tipo_producto.desplegable_talla else None
            if not desplegable_talla:
                messagebox.showerror("Error", "Debe seleccionar la talla.")
                return
            detalles_tipo_producto["talla"] = desplegable_talla

        elif lista_tipo_producto == "Alimento":
            desplegable_dia = self.lista_tipo_producto.desplegable_dia.get() if self.lista_tipo_producto.desplegable_dia else None
            desplegable_mes = self.lista_tipo_producto.desplegable_mes.get() if self.lista_tipo_producto.desplegable_mes else None
            desplegable_anio = self.lista_tipo_producto.desplegable_anio.get() if self.lista_tipo_producto.desplegable_anio else None
            if not desplegable_dia or not desplegable_mes or not desplegable_anio:
                messagebox.showerror("Error", "Debe seleccionar una fecha de caducidad completa.")
                return
            detalles_tipo_producto["fecha_caducidad"] = {
                "dia": desplegable_dia,
                "mes": desplegable_mes,
                "anio": desplegable_anio
            }

        # Guardar datos en section_data antes de cerrar la ventana
        self.section_data = {
            "nombre": nombre,
            "tipo_producto": lista_tipo_producto,
            "detalles": detalles_tipo_producto
        }

        # Identificar el almacén seleccionado
        warehouse_data = self.almacen_table.item(selected_warehouse[0], "values")
        current_warehouse_id = int(warehouse_data[0])

        almacen_seleccionado = next((almacen for almacen in self.almacenes if almacen.id == current_warehouse_id), None)
        if not almacen_seleccionado:
            messagebox.showerror("Error", "Almacén no encontrado.")
            return

        # Crear y agregar la nueva sección al almacén
        nueva_seccion = Section(
            self.section_id_counter,
            self.section_data["nombre"],
            self.section_data["tipo_producto"],
            self.section_data["detalles"]
        )
        almacen_seleccionado.agregarSeccion(nueva_seccion)
        self.section_id_counter += 1

        # Agregar la sección a la tabla
        self.section_table.insert("", "end", values=(
            nueva_seccion.id,
            nueva_seccion.nombre,
            nueva_seccion.tipo_producto,
            almacen_seleccionado.nombre
        ))

        # Mostrar mensaje de éxito y cerrar la ventana
        messagebox.showinfo("Éxito", "Sección creada con éxito.")
        self.section_window.destroy()
        self.section_window_open = False
        self.almacen_table.selection_remove(self.almacen_table.selection())

    def delete_section(self):
        selected_item = self.section_table.selection()
        if not selected_item:
            messagebox.showwarning("Eliminar Sección", "Seleccione una sección para eliminar.")
            return

        confirm = messagebox.askyesno("Eliminar Sección", "¿Está seguro de que desea eliminar esta sección?")
        if confirm:
            for item in selected_item:
                section_id = int(self.section_table.item(item, "values")[0])
                for almacen in self.almacenes:
                    almacen.secciones = [seccion for seccion in almacen.getSecciones() if seccion.id != section_id]
                self.section_table.delete(item)

    def search_section_window(self):
        self.search_section_w = Toplevel(self.ventana)
        self.search_section_w.title("MINUTEROS S.A.S")
        self.search_section_w.geometry("280x150")
        self.search_section_w.iconbitmap("images/icon.ico")
        self.search_section_w.resizable(0, 0)
        #Deshabilitar Interaccion con la ventana principal
        self.search_section_w.transient(self.ventana)
        self.search_section_w.grab_set()

        # Búsqueda & Marco de etiqueta Secciones
        self.search_section_label_frame = LabelFrame(self.search_section_w, text="Búsqueda De Secciones", width=300, height=120)
        self.search_section_label_frame.pack()

        Label(self.search_section_label_frame, text="Buscar por Nombre o ID:").place(x=60, y=10)

        self.search_section_entry = Entry(self.search_section_label_frame, width=30)
        self.search_section_entry.place(x=45, y=40)

        Label(self.search_section_w, text="Darle ENTER para continuar").place(x=70, y=120)

        self.search_section_entry.bind("<Return>",self.search_section)

    def search_section(self,event=None):
        search = self.search_section_entry.get().strip()

        if not search:
            messagebox.showwarning("Error", "Por favor ingrese un ID o Nombre para buscar.")
            return

        resultados = []
        # Recorrer los almacenes y sus secciones
        for almacen in self.almacenes:
            for seccion in almacen.getSecciones():
                # Buscar por ID o Nombre de la sección
                if str(seccion.id) == search or seccion.nombre.lower() == search.lower():
                    resultados.append({
                        "ID": seccion.id,
                        "Nombre": seccion.nombre,
                        "Tipo de Producto": seccion.tipo_producto,
                        "Almacén": almacen.nombre
                    })

        if len(resultados) > 0:
            # Mostrar los resultados encontrados
            resultado_texto = ""
            for resultado in resultados:
                resultado_texto += (
                    f"ID: {resultado['ID']}\n"
                    f"Nombre: {resultado['Nombre']}\n"
                    f"Tipo de Producto: {resultado['Tipo de Producto']}\n"
                    f"Almacén: {resultado['Almacén']}\n\n"
                )
            simpledialog.messagebox.showinfo("Resultado de la Búsqueda", resultado_texto.strip())
            self.search_section_w.destroy()
        else:
            messagebox.showwarning("Sin Resultados", "No se encontró ninguna sección con ese ID o Nombre.")

    def add_product_window(self, product_to_edit=None):
        if self.product_window_open:
            return

        # Si se está editando un producto, obtener datos seleccionados
        if product_to_edit:
            producto_id, nombre, precio, cantidad, descripcion = product_to_edit

        selected_section = self.section_table.selection()

        if not selected_section and not product_to_edit:
            messagebox.showwarning("Agregar Producto", "Seleccione o Agrege una sección.")
            return

        # Obtener datos de la sección seleccionada
        section_data = self.section_table.item(selected_section[0], "values") if not product_to_edit else None
        current_section_id = int(section_data[0]) if section_data else None

        # Crear la ventana para agregar o editar el producto
        self.product_window = Toplevel(self.ventana)
        self.product_window.title("MINUTEROS S.A.S")
        self.product_window.geometry("480x300")
        self.product_window.iconbitmap("images/icon.ico")
        self.product_window.resizable(0, 0)
        self.product_window.transient(self.ventana)
        self.product_window.grab_set()
        self.product_window_open = True

        # Etiquetas y campos de entrada
        title = "Editar Producto" if product_to_edit else "Agregar Producto"
        Label(self.product_window, text=title, font=("Helvetica", 20, "bold")).place(x=120, y=10)

        Label(self.product_window, text="Nombre del Producto:").place(x=45, y=70)
        self.product_nombre = Entry(self.product_window, width=20)
        self.product_nombre.place(x=50, y=100)
        if product_to_edit:
            self.product_nombre.insert(0, nombre)

        Label(self.product_window, text="Precio del Producto:").place(x=45, y=170)
        self.product_precio = Entry(self.product_window, width=20)
        self.product_precio.place(x=50, y=200)
        if product_to_edit:
            self.product_precio.insert(0, precio)

        Label(self.product_window, text="Cantidad de Productos:").place(x=250, y=170)
        self.product_cantidad = Entry(self.product_window, width=25)
        self.product_cantidad.place(x=250, y=200)
        if product_to_edit:
            self.product_cantidad.insert(0, cantidad)

        Label(self.product_window, text="Descripción del Producto:").place(x=250, y=70)
        self.product_descripcion = Text(self.product_window, width=25, height=3, font=("Helvetica", 10))
        self.product_descripcion.place(x=250, y=100)
        if product_to_edit:
            self.product_descripcion.insert('1.0', descripcion)

        def save_product():
            nombre = self.product_nombre.get().strip()
            precio = self.product_precio.get().strip()
            cantidad = self.product_cantidad.get().strip()
            descripcion = self.product_descripcion.get('1.0', 'end-1c').strip()

            if not nombre or not precio or not cantidad or not descripcion:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if not nombre.replace(" ", "").isalpha() or "  " in nombre:
                messagebox.showerror("Error", "El campo 'Nombre del Producto' no debe contener más de un espacio, números o caracteres no válidos.")
                return

            if not precio.replace(".", "", 1).isdigit():
                messagebox.showerror("Error", "El campo 'Precio' solo debe tener números positivos.")
                return

            if not cantidad.isdigit() or int(cantidad) < 0:
                messagebox.showerror("Error", "El campo 'Cantidad de Productos' solo debe tener números enteros y positivos.")
                return

            if product_to_edit:
                # Actualizar producto existente en la tabla y en la sección
                for item in self.product_table.get_children():
                    item_values = self.product_table.item(item, "values")
                    if int(item_values[0]) == producto_id:
                        # Actualizar tabla de productos
                        self.product_table.item(item, values=(producto_id, nombre, precio, cantidad, descripcion, item_values[5], item_values[6]))

                        # Actualizar producto en la sección correspondiente
                        for almacen in self.almacenes:
                            for seccion in almacen.getSecciones():
                                for producto in seccion.getProductos():
                                    if producto.id == producto_id:
                                        producto.nombre = nombre
                                        producto.precio = float(precio)
                                        producto.cantidad = int(cantidad)
                                        producto.descripcion = descripcion
                                        break
                        break
                messagebox.showinfo("Éxito", "Producto actualizado con éxito.")
            else:
                # Crear nuevo producto
                nuevo_producto = Product(self.product_id_counter, nombre, float(precio), int(cantidad), descripcion)
                for almacen in self.almacenes:
                    for seccion in almacen.getSecciones():
                        if seccion.id == current_section_id:
                            seccion.agregarProducto(nuevo_producto)
                            self.product_id_counter += 1
                            self.product_table.insert("", "end", values=(nuevo_producto.id, nombre, precio, cantidad, descripcion, almacen.nombre, seccion.nombre))
                            messagebox.showinfo("Éxito", "Producto creado con éxito.")
                            break
                        
            self.product_window_open = False
            self.product_window.destroy()

        Button(self.product_window, text="Guardar Producto", command=save_product).place(x=190, y=250)

        def window_close():
            self.product_window_open = False
            self.product_window.destroy()

        self.product_window.protocol("WM_DELETE_WINDOW", window_close)

    def edit_product(self):
        selected_item = self.product_table.selection()
        if not selected_item:
            messagebox.showwarning("Editar Producto", "Seleccione un producto para editar.")
            return

        item_values = self.product_table.item(selected_item[0], "values")
        product_to_edit = (int(item_values[0]), item_values[1], item_values[2], item_values[3], item_values[4])
        self.add_product_window(product_to_edit=product_to_edit)

    def add_product_button(self):
        nombre = self.product_nombre.get().strip()
        precio = self.product_precio.get().strip()
        descripcion = self.product_descripcion.get('1.0', 'end-1c')
        cantidad = self.product_cantidad.get().strip() 
        # Obtener datos de la sección seleccionada
        selected_section = self.section_table.selection()
        section_data = self.section_table.item(selected_section[0], "values")
        current_section_id = int(section_data[0])

        if not nombre or not precio or not cantidad or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        if not nombre.replace(" ", "").isalpha() or " " in nombre:
            messagebox.showerror("Error", "El campo 'Nombre del Producto' no debe contener más de un espacio, números o caracteres no válidos.")
            return
        
        if not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
            messagebox.showerror("Error", "El campo 'Precio' debe ser un número positivo.")
            return
        
        if not cantidad.isdigit() or int(cantidad) < 0:
            messagebox.showerror("Error", "El campo 'Cantidad de Productos' debe ser un número entero positivo.")
            return
        
        # Crear el producto
        nuevo_producto = Product(self.product_id_counter, nombre, float(precio), int(cantidad), 
        descripcion)
        # Buscar la sección por ID
        for almacen in self.almacenes:
            for seccion in almacen.getSecciones():
                if seccion.id == current_section_id:
                    seccion.agregarProducto(nuevo_producto)
                    self.product_id_counter += 1
                    self.product_table.insert("", "end", values=(nuevo_producto.id,nuevo_producto.nombre,nuevo_producto.precio,nuevo_producto.cantidad,nuevo_producto.descripcion,almacen.nombre,seccion.nombre))
                    messagebox.showinfo("Éxito", "Producto creado con éxito.")
                    self.product_window.destroy()
                    self.product_window_open = False
                    return

    def delete_product(self):
        selected_item = self.product_table.selection()
        if not selected_item:
            messagebox.showwarning("Eliminar Producto", "Seleccione un producto para eliminar.")
            return

        confirm = messagebox.askyesno("Eliminar Producto", "¿Está seguro de que desea eliminar este producto?")
        if confirm:
            for item in selected_item:
                product_id = int(self.product_table.item(item, "values")[0])
                for almacen in self.almacenes:
                    for seccion in almacen.getSecciones():
                        seccion.productos = [producto for producto in seccion.getProductos() if producto.id != product_id]
                self.product_table.delete(item)

    def search_product_window(self):
        self.search_product_w = Toplevel(self.ventana)
        self.search_product_w.title("MINUTEROS S.A.S")
        self.search_product_w.geometry("280x150")
        self.search_product_w.iconbitmap("images/icon.ico")
        self.search_product_w.resizable(0, 0)
        # Deshabilitar Interacción con la ventana principal
        self.search_product_w.transient(self.ventana)
        self.search_product_w.grab_set()

        # Marco de etiqueta para la búsqueda de productos
        self.search_product_label_frame = LabelFrame(self.search_product_w, text="Búsqueda De Productos", width=300, height=120)
        self.search_product_label_frame.place(x=0, y=0)

        Label(self.search_product_label_frame, text="Buscar por Nombre o ID:").place(x=60, y=10)

        self.search_product_entry = Entry(self.search_product_label_frame, width=30)
        self.search_product_entry.place(x=45, y=40)

        Label(self.search_product_w, text="Darle ENTER para continuar").place(x=70, y=120)

        self.search_product_entry.bind("<Return>", self.search_product)

    def search_product(self, event=None):
        search = self.search_product_entry.get().strip()

        if not search:
            messagebox.showwarning("Error", "Por favor ingrese un ID o Nombre para buscar.")
            return

        resultados = []
        # Recorrer los almacenes y sus secciones para encontrar productos
        for almacen in self.almacenes:
            for seccion in almacen.getSecciones():
                for producto in seccion.getProductos():
                    # Buscar por ID o Nombre del producto
                    if str(producto.id) == search or producto.nombre.lower() == search.lower():
                        resultados.append({
                            "ID": producto.id,
                            "Nombre": producto.nombre,
                            "Precio": producto.precio,
                            "Cantidad Productos": producto.cantidad,
                            "Descripción": producto.descripcion,
                            "Sección": seccion.nombre,
                            "Almacén": almacen.nombre
                        })

        if len(resultados) > 0:
            # Mostrar los resultados encontrados
            resultado_texto = ""
            for resultado in resultados:
                resultado_texto += (
                    f"ID: {resultado['ID']}\n"
                    f"Nombre: {resultado['Nombre']}\n"
                    f"Precio: {resultado['Precio']}\n"
                    f"Cantidad Productos: {resultado['Cantidad Productos']}\n"
                    f"Descripción: {resultado['Descripción']}\n"
                    f"Sección: {resultado['Sección']}\n"
                    f"Almacén: {resultado['Almacén']}\n\n"
                )
            simpledialog.messagebox.showinfo("Resultado de la Búsqueda", resultado_texto.strip())
            self.search_product_w.destroy()
        else:
            messagebox.showwarning("Sin Resultados", "No se encontró ningún producto con ese ID o Nombre.")

    def mostrarDetalles(self):
        selected_item = self.product_table.selection()
        if not selected_item:
            messagebox.showwarning("Detalles del Producto", "Seleccion un Producto para mostrar los detalles.")
            return

        selected_values = self.product_table.item(selected_item[0], 'values')
        if not selected_values:
            return

        product_id = selected_values[0]

        for almacen in self.almacenes:
            for seccion in almacen.getSecciones():
                for producto in seccion.getProductos():
                    if str(producto.id) == product_id:
                        # Obtener información adicional desde los detalles de la sección
                        detalles_seccion = seccion.detalles
                        info_adicional = ""

                        if seccion.tipo_producto == "Tecnología":
                            garantia = detalles_seccion.get("garantia", "N/A")
                            info_adicional = f"Tipo de Producto: {seccion.tipo_producto}\nGarantía: {garantia}\n"
                        elif seccion.tipo_producto == "Ropa":
                            talla = detalles_seccion.get("talla", "N/A")
                            info_adicional = f"Tipo de Producto: {seccion.tipo_producto}\nTalla: {talla}\n"
                        elif seccion.tipo_producto == "Alimento":
                            fecha_caducidad = detalles_seccion.get("fecha_caducidad", {})
                            dia = fecha_caducidad.get("dia", "N/A")
                            mes = fecha_caducidad.get("mes", "N/A")
                            anio = fecha_caducidad.get("anio", "N/A")
                            info_adicional = f"Tipo de Producto: {seccion.tipo_producto}\nFecha de Caducidad: {dia}/{mes}/{anio}\n"

                        # Construir y mostrar el mensaje con los detalles
                        resultado_texto = (
                            f"ID: {producto.id}\n"
                            f"Nombre: {producto.nombre}\n"
                            f"Precio: {producto.precio}\n"
                            f"Cantidad Productos: {producto.cantidad}\n"
                            f"{info_adicional}"
                            f"Descripción: {producto.descripcion}\n"
                            f"Sección: {seccion.nombre}\n"
                            f"Almacén: {almacen.nombre}"
                        )
                        messagebox.showinfo("Detalles del Producto", resultado_texto)
                        return