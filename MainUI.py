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


class MainUI:
    def __init__(self, fileLoc):
        menubar = tk.Menu(root)

        settingMenu = tk.Menu(root, tearoff=0)
        settingMenu.add_command(label="Manage Theme", command=lambda: manageTheme())
        settingMenu.add_command(label="Exit", command=lambda: exit(-1))

        newTask = ctk.CTkButton(master=root, text="New Task", command=lambda: print("new task"))
        newTask.grid(row=0, column=0, columnspan=2, sticky="nsew")
        newLog = ctk.CTkButton(master=root, text="New Task", command=lambda: print("new log"))
        newLog.grid(row=0, column=0, columnspan=2, sticky="nsew")

        contentFrame = ctk.CTkFrame(master=root).grid(row=0, column=0, sticky="nsew")

        taskFrame = ctk.CTkFrame(master=root, fg_color="gray").grid(row=0, column=1, sticky="nsew")

        root.mainloop()