import re

import customtkinter as ctk
from tkinter import filedialog

from MainUI import MainUI

# Create new instance
sel = ctk.CTk()
sel.geometry("800x400")
sel.title("Select Folder")
sel.resizable(False, False)
sel.iconbitmap("LycheeLogo.ico")
sel.grid_rowconfigure(0, weight=1)
sel.grid_columnconfigure(0, weight=1)

fileAs = ctk.CTk()
fileAs.geometry("500x280")
fileAs.title("Select Folder")
fileAs.resizable(False, False)
fileAs.iconbitmap("LycheeLogo.ico")


def openMain(fileLoc):
    sel.destroy()
    MainUI(fileLoc)


def writeFile(fileName):
    f = open("profiles.txt", "a")
    f.write("X" + fileName + "Y")
    f.close()
    fileAs.destroy()
    openMain(fileName)


def new():
    fileName = filedialog.askdirectory()

    fileAsFrame = ctk.CTkFrame(master=fileAs)
    fileAsFrame.pack(pady=10, padx=10)

    fileLabel = ctk.CTkLabel(master=fileAsFrame, justify=ctk.CENTER, font=("Mooli", 10),
                             text="Import File: " + fileName + "?")
    fileLabel.pack(pady=10, padx=10)

    fileBtn = ctk.CTkButton(master=fileAsFrame, text="Create New Vault", command=lambda: writeFile(fileName))
    fileBtn.pack(pady=5, padx=10)

    closeBtn = ctk.CTkButton(master=fileAsFrame, text="Cancel", command=lambda: fileAs.destroy())
    closeBtn.pack(pady=5, padx=10)

    fileAs.mainloop()


class SelFolder:
    def __init__(self):

        # Scan Lychee directory for vault Folders
        try:
            with open("profiles.txt", "r") as file:
                data = file.read().replace('\n', '')
            profiles = list(filter(None, re.split("X|Y", data)))
        except:
            openF = open("profiles.txt", "x")
            openF.close()
            profiles = []

        # Elements
        frame = ctk.CTkFrame(master=sel, border_width=1, border_color="#bfbfbf")
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        selLabel = ctk.CTkLabel(master=frame, justify=ctk.CENTER, font=("Mooli", 32), text="Profiles")
        selLabel.pack(pady=10, padx=10)

        newProfile = ctk.CTkButton(master=frame, text="New", command=lambda: new())
        newProfile.pack(pady=5, padx=5)

        scrollProf = ctk.CTkScrollableFrame(master=frame,width=780, height=380)
        scrollProf.pack(pady=5, padx=5)

        if (len(profiles) > 0):
            for name in profiles:
                button = ctk.CTkButton(master=scrollProf, text=name, command=lambda: openMain(name))
                button.pack(pady=5, padx=10)
        else:
            noneLabel = ctk.CTkLabel(master=scrollProf, justify=ctk.CENTER, font=("Mooli", 16),
                                     text="No Profiles found")
            noneLabel.pack(pady=5, padx=5)

        sel.mainloop()
