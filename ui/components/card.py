import customtkinter as ctk


class Card(ctk.CTkFrame):

        def __init__(
        self,
        master,
        titulo,
        valor,
        icone="",
        variacao="",
        cor_variacao="#00D26A"
):
         super().__init__(
         master,
         width=280,
         height=170,
         corner_radius=12,
         fg_color="#1A1F2B"
        
)

         self.grid_propagate(False)

         self.titulo = titulo
         self.valor = valor
         self.icone = icone
         self.variacao = variacao
         self.cor_variacao = cor_variacao

         self.create_widgets()

        def create_widgets(self):
            
            self.header_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
)

            self.header_frame.grid(
            row=0,
            column=0,
            padx=20,
            pady=(18, 0),
            sticky="w"
)
            
            self.icon_label = ctk.CTkLabel(
            self.header_frame,
            text=self.icone,
            font=("Segoe UI Symbol", 20)
)

            self.icon_label.pack(
            side="left",
            padx=(0, 8)
)

            self.title_label = ctk.CTkLabel(
            self.header_frame,
            text=self.titulo,
            font=("Segoe UI", 20, "bold"),
            text_color="white"
)

            self.title_label.pack(
            side="left"
)

            self.value_label = ctk.CTkLabel(
            self,
            text=self.valor,
            font=("Segoe UI", 28, "bold"),
            text_color="#00D26A"
    )

            self.value_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=(25, 0),
            sticky="w"
    )
            
            self.variation_label = ctk.CTkLabel(
            self,
            text=self.variacao,
            font=("Segoe UI", 16, "bold"),
            text_color=self.cor_variacao
)

            self.variation_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=(5,),
            sticky="w"
)