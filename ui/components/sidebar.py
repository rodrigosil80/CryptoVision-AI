import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=220,
            fg_color="#1A1F2B",
            corner_radius=0
        )

        self.grid_propagate(False)