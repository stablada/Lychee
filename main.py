import customtkinter as ctk

# System Themes and colouring
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# App setup
app = ctk.CTk()
app.geometry("400x280")
app.title("SebaPlanner")
app.resizable(False, False)
app.iconbitmap("icon.ico")

# Methods
def query():
    print("querying")

# Elements
frame1 = ctk.CTkFrame(master=app)
frame1.pack(pady=20, padx=20, fill="both", expand=False, )

titleLabel = ctk.CTkLabel(master=frame1, justify=ctk.CENTER, font=("Arial", 25), text="SebaPlanner")
titleLabel.pack(pady=10, padx=10)

createBtn = ctk.CTkButton(master=frame1, text="New")
createBtn.pack(pady=5, padx=5)

queryBtn = ctk.CTkButton(master=frame1, text="Query")
queryBtn.pack(pady=5, padx=5)

exitBtn = ctk.CTkButton(master=frame1, text="Exit", command=lambda: exit(-1))
exitBtn.pack(pady=5, padx=5)

# Data Storage as CSV
app.mainloop()