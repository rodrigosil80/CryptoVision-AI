import customtkinter as ctk


class Header(ctk.CTkFrame):

    TITLE_FONT = ("Segoe UI", 22, "bold")

    def __init__(self, master):

        super().__init__(
            master,
            height=70,
            corner_radius=0,
            fg_color="#1A1F2B"
        )

        self.grid_propagate(False)

        self.create_widgets()

    def create_widgets(self):

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="CryptoVision AI",
            font=self.TITLE_FONT,
            text_color="white"
        )

        self.title_label.grid(
            row=0,
            column=0,
            padx=25,
            pady=20,
            sticky="w"
        )