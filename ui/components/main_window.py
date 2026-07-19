import customtkinter as ctk

from .header import Header
from .sidebar import Sidebar
from .statusbar import StatusBar


class MainWindow:

    def __init__(self, master):

        self.master = master

        self.configure_window()

        self.create_layout()


    def configure_window(self):

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)


    def create_layout(self):

        self.header = Header(self.master)

        self.sidebar = Sidebar(self.master)

        self.statusbar = StatusBar(self.master)

        self.content = ctk.CTkFrame(
            self.master,
            fg_color="#101418",
            corner_radius=0

        )

        self.header.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="nsew"
)
        
        self.sidebar.grid(
        row=1,
        column=0,
        sticky="nsew"
)
        
        self.content.grid(
        row=1,
        column=1,
        sticky="nsew"
)
        
        self.statusbar.grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="nsew"
)