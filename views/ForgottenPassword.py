from tkinter import *

from controllers.ShowPasswordButton import ShowPasswordButton
from views.Register import *

class ForgottenPassword:
    def __init__(self, forgotten_password_window, login_w, usuarios_guardados, contraseñas_guardadas,correos_guardados):
        self.forgotten_password_window = forgotten_password_window
        self.login_w = login_w
        self.usuarios_guardados = usuarios_guardados
        self.contraseñas_guardadas = contraseñas_guardadas
        self.correos_guardados = correos_guardados
        #Ventana
        self.forgotten_password_window = forgotten_password_window
        self.forgotten_password_window .geometry("600x480")
        self.forgotten_password_window.resizable(0,0)
        self.forgotten_password_window.title("Contraseña Olvidada")
        self.forgotten_password_window.config(bg="#E6E6FA") 
        self.forgotten_password_window.iconbitmap("images/icon.ico")

        #Guardar ventana Login
        self.login_w = login_w

        # Título
        Label(forgotten_password_window, text="MINUTEROS S.A.S - Gestor de Almacenes", font=("Helvetica", 18, "bold"), bg="#E6E6FA").pack(pady=10)

        # Subtítulo
        Label(forgotten_password_window, text="¿Haz Olvidado Tú Contraseña?", font=("Helvetica", 18), bg="#E6E6FA").pack(pady=10)

        #Etiqueta Usuario
        Label(forgotten_password_window, text="Usuario:", font=("Helvetica", 10), bg="#E6E6FA").place(x=100,y=142)

        self.user_entry = Entry(forgotten_password_window, width=45)
        self.user_entry.place(x=175,y=145)

        self.user_error = Label(forgotten_password_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.user_error.place(x=175, y=165)

        #Etiqueta Correo:
        Label(forgotten_password_window, text="Correo Electrónico:", font=("Helvetica", 10), bg="#E6E6FA").place(x=40,y=207)

        self.mail_entry = Entry(forgotten_password_window, width=45)
        self.mail_entry.place(x=175,y=210)

        self.mail_error = Label(forgotten_password_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.mail_error.place(x=175, y=230)

        ## Etiqueta & Entrada Contraseña Nueva
        Label(forgotten_password_window, text="Contraseña Nueva:", font=("Helvetica", 10), bg="#E6E6FA").place(x=40,y=277)

        self.new_password_entry = Entry(forgotten_password_window, width=45,show="*")
        self.new_password_entry.place(x=175,y=280)

        self.new_password_error = Label(forgotten_password_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.new_password_error.place(x=175, y=300)
        #Boton Mostrar/Ocultar Contraseña Nueva
        ShowPasswordButton(forgotten_password_window,self.new_password_entry,x=450,y=270)

        ## Etiqueta & Entrada Repetir Contraseña Nueva
        Label(forgotten_password_window, text="Repetir Contraseña\nNueva:", font=("Helvetica", 10), bg="#E6E6FA",justify="left").place(x=40,y=340)

        self.repeat_newpass_entry = Entry(forgotten_password_window, width=45, show="*")
        self.repeat_newpass_entry.place(x=175,y=350)

        self.repeat_newpass_error = Label(forgotten_password_window, text="", font=("Helvetica", 8), fg="red", bg="#E6E6FA")
        self.repeat_newpass_error.place(x=175, y=370)
        #Boton Mostrar/Ocultar Repetir Contraseña Nueva
        ShowPasswordButton(forgotten_password_window,self.repeat_newpass_entry,x=450,y=340)

        # Boton Confirmar
        self.button_confirm = Button(forgotten_password_window, text="Confirmar", width=10, bg="#333", fg="white",command=self.confirm_button)
        self.button_confirm.place(x=270,y=405)

        # Etiqueta ir a Registrarse & Login"
        register_label = Label(forgotten_password_window, text="Si no tiene cuenta. Registrese", font=("Helvetica", 8, "underline"), fg="blue", bg="#E6E6FA", cursor="hand2")

        login_label = Label(forgotten_password_window, text="Si tiene una regrese a Iniciar Sesión", font=("Helvetica", 8, "underline"), fg="blue", bg="#E6E6FA", cursor="hand2")

        # Interacción para abrir la ventana de registro
        register_label.bind("<Button-1>",self.show_register_window)
        # Interacción para abrir la ventana de olvide mi contraseña
        login_label.bind("<Button-1>",self.show_login_window)

        #Posicionar Etiquetas Registrarse & Login
        register_label.place(x=150,y=445)

        login_label.place(x=310,y=445)

    def show_register_window(self, event):
        self.forgotten_password_window.destroy()
        Register(Toplevel(self.login_w), self.login_w,self.usuarios_guardados,self.contraseñas_guardadas,self.correos_guardados)

    def show_login_window(self, event):
        self.forgotten_password_window.destroy()
        self.login_w.deiconify()

    def confirm_button(self):
        global correos_guardados

        self.user_error.config(text="")
        self.mail_error.config(text="")
        self.new_password_error.config(text="")
        self.repeat_newpass_error.config(text="")

        all_fields_filled = True

        if not self.user_entry.get():
            self.user_error.config(text="Este campo es obligatorio")
            all_fields_filled = False

        if not self.mail_entry.get():
            self.mail_error.config(text="Este campo es obligatorio")
            all_fields_filled = False

        if not self.new_password_entry.get():
            self.new_password_error.config(text="Este campo es obligatorio")
            all_fields_filled = False

        if not self.repeat_newpass_entry.get():
            self.repeat_newpass_error.config(text="Este campo es obligatorio")
            all_fields_filled = False

        elif self.new_password_entry.get() != self.repeat_newpass_entry.get():
            self.repeat_newpass_error.config(text="Las contraseñas no coinciden")
            all_fields_filled = False

        if not all_fields_filled:
            return

        usuario = self.user_entry.get()
        correo = self.mail_entry.get()

        if usuario in self.usuarios_guardados:
            index_usuario = self.usuarios_guardados.index(usuario)
        else:
            self.user_error.config(text="Nombre de usuario incorrecto")
            return

        if correo in self.correos_guardados:
            index_correo = self.correos_guardados.index(correo)
        else:
            self.mail_error.config(text="Correo Electrónico incorrecto")
            return

        # Verificar si el correo corresponde al usuario
        if index_usuario != index_correo:
            self.mail_error.config(text="Correo no corresponde al usuario")
            return

        # Actualizar la contraseña
        nueva_contraseña = self.new_password_entry.get()
        self.contraseñas_guardadas[index_usuario] = nueva_contraseña
        print(f"Contraseña actualizada: {self.contraseñas_guardadas}")

        # Regresar a la ventana de login después de actualizar
        self.show_login_window(None)