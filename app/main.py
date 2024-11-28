import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tkinter import Tk
from views.Login import Login

if __name__ == "__main__":
    ventana = Tk()
    login_window = Login(ventana)
    ventana.mainloop()