import customtkinter as ctk

from SelFolder import SelFolder


## Create Root Instance ##

# App setup
app = ctk.CTk()
app.geometry("400x280")
app.title("Lychee")
app.resizable(False, False)
app.iconbitmap("LycheeLogo.ico")


## Methods ##

# Theme Update
def tUpdate(bg, ac):
    ctk.set_appearance_mode(bg)
    ctk.set_default_color_theme()

# Open Settings UI
def settings():
    cnfg = ctk.CTk()
    cnfg.geometry("280x400")
    cnfg.title("Settings")
    cnfg.resizable(False, False)
    cnfg.iconbitmap("LycheeLogo.ico")

    setlabel = ctk.CTkLabel(master=cnfg, justify=ctk.CENTER, font=("Mooli", 24), text="Setings")
    setlabel.pack(pady=10, padx=10)

    tBgL = ctk.CTkLabel(master=cnfg, justify=ctk.LEFT, font=("Mooli", 16), text="Background Mode")
    tBgL.pack(pady=5, padx=5)
    bgColor = ctk.CTkOptionMenu(master=cnfg, values=["Dark","Light"])
    bgColor.pack(pady=5, padx=5)

    tAcL = ctk.CTkLabel(master=cnfg, justify=ctk.LEFT, font=("Mooli", 16), text="Accent Color")
    tAcL.pack(pady=5, padx=5)
    acColor = ctk.CTkEntry(master=cnfg)
    acColor.pack(pady=5, padx=5)

    tBtn = ctk.CTkButton(master=cnfg, text="Update Theme", command=lambda: tUpdate(bgColor.get(), acColor.get()))
    tBtn.pack(pady=5, padx=5)

    cnfg.mainloop()


# Open Folder Selection menu
def open():
    app.destroy()
    SelFolder()


## TODO: Add direct-to-default vault option, in which user can skip
## the main menu upon startup and go directly to startup
class Menu:
    # System Themes and colouring
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    # Elements
    frame1 = ctk.CTkFrame(master=app)
    frame1.pack(pady=20, padx=20, fill="both", expand=False)

    titleLabel = ctk.CTkLabel(master=frame1, justify=ctk.CENTER, font=("Mooli", 32), text="Lychee")
    titleLabel.pack(pady=10, padx=10)

    createBtn = ctk.CTkButton(master=frame1, text="Open", command=lambda: open())
    createBtn.pack(pady=5, padx=5)

    queryBtn = ctk.CTkButton(master=frame1, text="Settings", command=lambda: settings())
    queryBtn.pack(pady=5, padx=5)

    exitBtn = ctk.CTkButton(master=frame1, text="Exit", command=lambda: exit(-1))
    exitBtn.pack(pady=5, padx=5)

    app.mainloop()

