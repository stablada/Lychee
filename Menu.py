import customtkinter as ctk

from SelFolder import SelFolder


## Methods ##
# Open Settings UI
def settings():
    cnfg = ctk.CTk()
    cnfg.geometry("280x400")
    cnfg.title("Settings")
    cnfg.resizable(False, False)
    cnfg.iconbitmap("LycheeLogo.ico")

    setlabel = ctk.CTkLabel(master=cnfg, justify=ctk.CENTER, font=("Mooli", 24), text="Setings")
    setlabel.pack(pady=10, padx=10)
    themeScroll = ctk.CTkScrollableFrame(master=cnfg)
    themeScroll.pack(pady=5, padx=5)
    cnfg.mainloop()


# Open Folder Selection menu
def open():
    SelFolder()


class Menu:
    # System Themes and colouring
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    # App setup
    app = ctk.CTk()
    app.geometry("400x280")
    app.title("Lychee")
    app.resizable(False, False)
    app.iconbitmap("LycheeLogo.ico")

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
