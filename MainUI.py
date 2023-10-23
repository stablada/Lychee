import re

import customtkinter as ctk
import tkinter as tk

# Create CTk instances
root = ctk.CTk()
root.geometry("1000x800")
root.title("Lychee")
root.resizable(False, False)
root.iconbitmap("LycheeLogo.ico")
root.minsize(300, 200)

# Grid Config
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=5)
root.grid_columnconfigure(1, weight=3)

def manageTheme():
    print("To be implemented")


def newTask(task, fileLoc):
    f = open("/tasks.txt", "a")
    f.write("X" + task + "Y")
    f.close()


def refresh(fileLoc):
    taskList = []
    try:
        with open(fileLoc + "/tasks.txt", "r") as file:
            data = file.read().replace('\n', '')
        taskList = list(filter(None, re.split("X|Y", data)))
    except:
        openF = open("/tasks.txt", "x")
        openF.close()
        taskList = []


class MainUI:
    def __init__(self, fileLoc):
        contentFrame = ctk.CTkFrame(master=root).grid(row=0, column=0, sticky="nsew")
        taskFrame = ctk.CTkFrame(master=root, fg_color="gray").grid(row=0, column=1, sticky="nsew")




        root.mainloop()