from tkinter import *

class ShowPasswordButton:
    def __init__(self,window,entrada:Entry,x:int,y:int):
        """
        Crea un botón para mostrar/ocultar el contenido de una entrada de contraseña.
        """
        # Botón Mostrar Contraseña
        self.show_password_button = Button(window, text="👁️", font=("normal",15), bg="#E6E6FA", activebackground="#E6E6FA", borderwidth=0, cursor="hand2")
        self.show_password_button.place(x=x,y=y)

        self.show_password_button.bind("<ButtonPress>", self.show_password)
        self.show_password_button.bind("<ButtonRelease>", self.hide_password)
        #Entrada
        self.entrada = entrada

    #METODOS PARA BOTON MOSTRAR O NO MOSTRAR CONTRASEÑA
    def show_password(self, event):
        if self.entrada.get():
            self.entrada.config(show="")

    def hide_password(self, event):
        self.entrada.config(show="*")