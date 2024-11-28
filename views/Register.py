from tkinter import *

from controllers.ShowPasswordButton import ShowPasswordButton

class Register:
    def __init__(self, register_window, login_w, usuarios_guardados, contraseñas_guardadas,correos_guardados):
        self.register_window = register_window
        self.login_w = login_w
        self.usuarios_guardados = usuarios_guardados
        self.contraseñas_guardadas = contraseñas_guardadas
        self.correos_guardados = correos_guardados
        #Ventana
        self.register_window = register_window
        self.register_window.geometry("600x500")
        self.register_window.resizable(0, 0)
        self.register_window.title("Registro")
        self.register_window.config(bg="#E6E6FA") 
        self.register_window.iconbitmap("images/icon.ico")

        Label(register_window, text="MINUTEROS S.A.S - Gestor de Almacenes", font=("Helvetica", 18, "bold"), bg="#E6E6FA").pack(pady=10)
        Label(register_window, text="Regístrate", font=("Helvetica", 18, "bold"), bg="#E6E6FA").pack(pady=10)

        Label(register_window, text="Nombre de Usuario:", font=("Helvetica", 10), bg="#E6E6FA").place(x=40, y=137)
        self.usuario_entry = Entry(register_window, width=41)
        self.usuario_entry.place(x=175, y=140)
        self.usuario_error = Label(register_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.usuario_error.place(x=175, y=165)

        Label(register_window, text="Correo Electrónico:", font=("Helvetica", 10), bg="#E6E6FA").place(x=40, y=197)
        self.correo_entry = Entry(register_window, width=41)
        self.correo_entry.place(x=175, y=200)
        self.correo_error = Label(register_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.correo_error.place(x=175, y=225)

        Label(register_window, text="Contraseña:", font=("Helvetica", 10), bg="#E6E6FA").place(x=40, y=258)
        self.password_entry = Entry(register_window, width=41, show="*")
        self.password_entry.place(x=175, y=260)
        self.password_error = Label(register_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.password_error.place(x=175, y=285)
        ShowPasswordButton(register_window, self.password_entry, x=430, y=250)

        Label(register_window, text="Repetir Contraseña:", font=("Helvetica", 10), bg="#E6E6FA").place(x=40, y=318)
        self.repeat_pass_entry = Entry(register_window, width=41, show="*")
        self.repeat_pass_entry.place(x=175, y=320)
        self.repeat_pass_error = Label(register_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.repeat_pass_error.place(x=175, y=345)
        ShowPasswordButton(register_window, self.repeat_pass_entry, x=430, y=310)

        self.register_button = Button(register_window, text="Registrarse", width=30, bg="#333", fg="white", command=self.register_button)
        self.register_button.place(x=188, y=375)

        Label(register_window, text="Al registrarte, aceptas nuestras Condiciones de uso y\nPolítica de privacidad", font=("Helvetica", 8), bg="#E6E6FA").place(x=165, y=420)

        login_label = Label(register_window, text="¿Ya tienes una cuenta? Iniciar Sesión", font=("Helvetica", 8, "underline"), fg="blue", bg="#E6E6FA", cursor="hand2")
        login_label.bind("<Button-1>", self.show_login_window)
        login_label.place(x=205, y=460)

    def register_button(self):
        self.usuario_error.config(text="")
        self.correo_error.config(text="")
        self.password_error.config(text="")
        self.repeat_pass_error.config(text="")

        all_fields_filled = True

        if self.usuario_entry.get() in self.usuarios_guardados:
            self.usuario_error.config(text="Este usuario ya existe")
            all_fields_filled = False

        if not self.usuario_entry.get():
            self.usuario_error.config(text="Este campo es obligatorio")
            all_fields_filled = False
        if not self.correo_entry.get():
            self.correo_error.config(text="Este campo es obligatorio")
            all_fields_filled = False
        if not self.password_entry.get():
            self.password_error.config(text="Este campo es obligatorio")
            all_fields_filled = False
        if not self.repeat_pass_entry.get():
            self.repeat_pass_error.config(text="Este campo es obligatorio")
            all_fields_filled = False
        elif self.password_entry.get() != self.repeat_pass_entry.get():
            self.repeat_pass_error.config(text="Las contraseñas no coinciden")
            all_fields_filled = False

        if all_fields_filled:
            self.usuarios_guardados.append(self.usuario_entry.get())
            self.contraseñas_guardadas.append(self.password_entry.get())
            self.correos_guardados.append(self.correo_entry.get())  

            print(self.correos_guardados)  
            self.show_login_window(None)

    def show_login_window(self, event):
        self.register_window.destroy()
        self.login_w.deiconify()
