import customtkinter as ctk
from ui.components.main_window import MainWindow
from engine.decision_engine import DecisionEngine
from services.coingecko_service import CoinGeckoService


class AppController:
    
    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")    

        self.app = ctk.CTk()

        self.app.title("CryptoVision AI")

        self.app.geometry("1400x800")

        self.app.minsize(1200,700)
        
        self.market_service = CoinGeckoService()
        
        self.decision_engine = DecisionEngine(self.market_service)
        
        self.main_window = MainWindow(
        self.app,
        self.decision_engine
)



    def run(self):

        self.app.mainloop()
        

       