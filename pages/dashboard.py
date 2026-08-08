import customtkinter as ctk
from ui.components import card
from ui.components.card import Card
from services.coingecko_service import CoinGeckoService


class Dashboard(ctk.CTkFrame):

    def __init__(self, master, decision_engine):

        super().__init__(
            master,
            fg_color="transparent"
        )
        
        self.engine = decision_engine
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        
         ids = [
       "bitcoin",
       "ethereum",
       "solana"
]
       
            
         self.cards_frame = ctk.CTkFrame(
         self,
         fg_color="transparent"
)

         self.cards_frame.pack(
         fill="x",
         padx=20,
         pady=20
)
        
         for coluna, coin_id in enumerate(ids):
             
          analise = self.engine.analisar(coin_id)
          
          card = Card(
          self.cards_frame,
          titulo=analise["nome"],
          valor=f'R$ {analise["preco"]:,.2f}',
          icone="🪙",
          variacao=f'{analise["variacao"]:+.2f}%',
          cor_variacao="#00D26A" if analise["variacao"] >= 0 else "#FF4D4D"
  )
          
          card.grid(
          row=0,
          column=coluna,
          padx=15,
          pady=15,
          sticky="nsew"
    )
         
                 
         for coluna in range(3):
            self.cards_frame.grid_columnconfigure(
            coluna,
            weight=1
    )
            
         