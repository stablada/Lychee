import customtkinter as ctk

from MainUI import MainUI


def openMain():
    MainUI()

class SelFolder:
    def __init__(self):

        # Scan Lychee directory for vault Folders
        profiles = []
        #find dir and add to array

        # Create new instance
        sel = ctk.CTk()
        sel.geometry("400x280")
        sel.title("Select Folder")
        sel.resizable(False, False)
        sel.iconbitmap("LycheeLogo.ico")

        # Elements
        frame = ctk.CTkFrame(master=sel)
        frame.pack()

        selLabel = ctk.CTkLabel(master=frame, justify=ctk.CENTER, font=("Mooli", 32), text="Lychee")
        selLabel.pack(pady=10, padx=10)

        newProfile = ctk.CTkButton(master=frame, text="New", command=lambda: open())
        newProfile.pack(pady=5, padx=5)

        scrollProf = ctk.CTkScrollableFrame(master=frame)
        scrollProf.pack(pady=5, padx=5)

        #update scrollProf to include values in Profiles[]

        sel.mainloop()