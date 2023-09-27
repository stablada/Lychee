import customtkinter as ctk


root = ctk.CTk()
root.geometry("400x280")
root.title("Lychee")
root.resizable(False, False)
root.iconbitmap("LycheeLogo.ico")


class MainUI:
    def __init__(self, fileLoc):
        print("hi")