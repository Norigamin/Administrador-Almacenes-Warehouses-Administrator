from tkinter import Label,Tk,Entry,Button,Toplevel

from views.Dashboard import Dashboard
from views.Register import *
from views.ForgottenPassword import ForgottenPassword

from controllers.ShowPasswordButton import ShowPasswordButton

usuarios_guardados = ["johan"]
contraseñas_guardadas = ["123"]
correos_guardados = ["johan@example.com"]

class Login:
    def __init__(self, login_window):
        self.login_window = login_window
        self.login_window.geometry("600x400")
        self.login_window.title("MINUTEROS S.A.S - Gestor de Almacenes")
        self.login_window.config(bg="#E6E6FA") 
        self.login_window.iconbitmap("images/icon.ico")
        self.login_window.resizable(0, 0)

        # Título
        Label(login_window, text="MINUTEROS S.A.S - Gestor de Almacenes", font=("Helvetica", 20, "bold"), bg="#E6E6FA").place(x=25, y=30)

        # Subtítulo
        Label(login_window, text="Bienvenido", font=("Helvetica", 18, "bold"), bg="#E6E6FA").place(x=240, y=100)

        # Usuario y contraseña
        Label(login_window, text="Usuario:", font=("Helvetica", 15, "bold"), bg="#E6E6FA").place(x=117, y=160)
        Label(login_window, text="Contraseña:", font=("Helvetica", 15, "bold"), bg="#E6E6FA").place(x=80, y=220)

        self.user_entry = Entry(width=33)
        self.user_entry.place(x=210, y=167)

        #Error user label
        self.user_error = Label(login_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.user_error.place(x=210, y=187)

        self.password_entry = Entry(width=33, show="*")
        self.password_entry.place(x=210, y=227)

        #Error password label
        self.password_error = Label(login_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.password_error.place(x=210, y=247)
        #Boton Mirar/Ocultar Contraseña
        ShowPasswordButton(login_window,self.password_entry,x=420,y=217)

        # Botón iniciar sesión
        self.button_login = Button(text="Iniciar Sesión", font=("Helvetica", 15),command=self.login_button)
        self.button_login.place(x=240, y=330)

        # Etiquetas "Registrarse" y "Olvide mi contraseña"
        register_label = Label(login_window, text="Registrarse", font=("Helvetica", 8, "underline"), fg="blue", bg="#E6E6FA", cursor="hand2")
        forgot_password_label = Label(login_window, text="Olvide mi contraseña", font=("Helvetica", 8, "underline"), fg="blue", bg="#E6E6FA", cursor="hand2")

        # Interacción para abrir la ventana de registro
        register_label.bind("<Button-1>", self.show_register_window)
        # Interacción para abrir la ventana de olvide mi contraseña
        forgot_password_label.bind("<Button-1>", self.show_forgot_password_window)

        # Posicionar etiquetas "Registrarse" y "Olvide mi contraseña"
        register_label.place(x=210, y=280)
        forgot_password_label.place(x=305, y=280)

    def show_register_window(self, event):
        self.login_window.withdraw()
        Register(Toplevel(self.login_window), self.login_window, usuarios_guardados, contraseñas_guardadas,correos_guardados)

    def show_forgot_password_window(self, event):
        self.login_window.withdraw()
        ForgottenPassword(Toplevel(self.login_window), self.login_window, usuarios_guardados, contraseñas_guardadas,correos_guardados)

    def show_dashboard(self):
        self.login_window.destroy()
        dashboard_window = Tk()
        Dashboard(dashboard_window)

    def login_button(self):
        #Campos obligatorios
        all_fields_filled = True

        self.user_error.config(text="")
        self.password_error.config(text="")

        if not self.user_entry.get():
            self.user_error.config(text="Este campo es obligatorio")
            all_fields_filled = False

        if not self.password_entry.get():
            self.password_error.config(text="Este campo es obligatorio")
            all_fields_filled = False

        if not all_fields_filled:
            return
        #Campos con informacion erronea y dashboard
        user_pass_filled = True

        usuarios = self.user_entry.get()
        contraseñas = self.password_entry.get()

        # Comprobar si el usuario está registrado
        if usuarios in usuarios_guardados:
            index = usuarios_guardados.index(usuarios)
            if contraseñas == contraseñas_guardadas[index]:
                self.show_dashboard()
            else:
                print(contraseñas_guardadas)
                self.password_error.config(text="Contraseña incorrecta")
                user_pass_filled = False
        else:
            self.user_error.config(text="Nombre de usuario incorrecto")
            user_pass_filled = False

        if not user_pass_filled:
            return