import customtkinter as ctk
from ui.components.main_window import MainWindow


class AppController:
    
    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")    

        self.app = ctk.CTk()

        self.app.title("CryptoVision AI")

        self.app.geometry("1400x800")

        self.app.minsize(1200,700)

        self.main_window = MainWindow(self.app)


    def run(self):

        self.app.mainloop()
        

       