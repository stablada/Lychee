import customtkinter as ctk
from tkinter import filedialog

from MainUI import MainUI


# Create new instance
sel = ctk.CTk()
sel.geometry("400x280")
sel.title("Select Folder")
sel.resizable(False, False)
sel.iconbitmap("LycheeLogo.ico")


def openMain(fileLoc):
    sel.destroy()
    MainUI(fileLoc)

def writeFile(fileName):
    f = open("profiles.txt", "a")
    f.write("}" + fileName)
    f.close()

def new():
    fileAs = ctk.CTk()
    fileAs.geometry("400x280")
    fileAs.title("Select Folder")
    fileAs.resizable(False, False)
    fileAs.iconbitmap("LycheeLogo.ico")

    fileName = filedialog.askdirectory()

    fileAsFrame = ctk.CTkFrame(master=fileAs)
    fileAsFrame.pack(pady=10, padx=10)

    fileLabel = ctk.CTkLabel(master=fileAsFrame, justify=ctk.CENTER, font=("Mooli", 32), text="Import File: " + fileName + "?")
    fileLabel.pack(pady=10, padx=10)

    fileBtn = ctk.CTkButton(master=fileAsFrame, text="Create New Vault", command=lambda: writeFile(fileName))
    fileBtn.pack(pady=5, padx=10)

    closeBtn = ctk.CTkButton(master=fileAsFrame, text="Cancel", command=lambda: fileAs.destroy())
    closeBtn.pack(pady=5, padx=10)


class SelFolder:
    def __init__(self):

        # Scan Lychee directory for vault Folders
        #for loop
        #scan for "}" until next "}"
        #add substring to array
        profiles = []

        # Elements
        frame = ctk.CTkFrame(master=sel)
        frame.pack()

        selLabel = ctk.CTkLabel(master=frame, justify=ctk.CENTER, font=("Mooli", 32), text="Lychee")
        selLabel.pack(pady=10, padx=10)

        newProfile = ctk.CTkButton(master=frame, text="New", command=lambda: new())
        newProfile.pack(pady=5, padx=5)

        scrollProf = ctk.CTkScrollableFrame(master=frame)
        scrollProf.pack(pady=5, padx=5)

        #for objects in profiles[]
        #create button in scrollProf with text profiles[i] with onclick open with param profiles[i]

        sel.mainloop()