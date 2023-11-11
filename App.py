from PIL import Image, ImageTk
import customtkinter
import tkinter
import requests

print("██╗███╗░░██╗░░░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░██╗░░██╗\n██║████╗░██║░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝\n██║██╔██╗██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝░╚███╔╝░\n██║██║╚████║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗░██╔██╗░\n██║██║░╚███║╚█████╔╝███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║██╔╝╚██╗\n╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝")

# Plain GUI
app = customtkinter.CTk() # create CTk window like you do with the Tk window
app.geometry("650x325") # Tk Window Size
app.title("Injector X v0.1")
# Apperance
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#Make the window resizable false
app.resizable(False,False) # Makes the window size unable to change

def Execute_function():
    code_input_text = CodeInput.get("1.0", tkinter.END)  # Get the text from the CodeInput widget
    print(code_input_text)

def Attach_function():
    print("Attached To Client")

def ScriptHub_function():
    print("Loading Up Script Hub")

# Execute Button
Executebutton = customtkinter.CTkButton(master=app, fg_color="#5A5A5A")
Executebutton = customtkinter.CTkButton(master=app, text="Execute", command=Execute_function, width=140, height=40)
Executebutton.place(x=565, y=295, anchor=customtkinter.CENTER)

# Attach Button
Attachbutton = customtkinter.CTkButton(master=app, fg_color="#5A5A5A")
Attachbutton = customtkinter.CTkButton(master=app, text="Attach", command=Attach_function, width=140, height=40)
Attachbutton.place(x=410, y=295, anchor=customtkinter.CENTER)

# ScriptHub Button
ScriptHubbutton = customtkinter.CTkButton(master=app, fg_color="#5A5A5A")
ScriptHubbutton = customtkinter.CTkButton(master=app, text="Script Hub", command=ScriptHub_function, width=140, height=40)
ScriptHubbutton.place(x=255, y=295, anchor=customtkinter.CENTER)

# Top Main Label
MainLabel = customtkinter.CTkLabel(master=app, text="InjectorX v0.1", width=240, height=50, corner_radius=8)
MainLabel.place(x=325, y=20, anchor=tkinter.CENTER)
MainLabel.configure(font=("Arial", 25))

# Text Input
CodeInput = customtkinter.CTkTextbox(master=app, width=550, height=220)
CodeInput.place(x=290, y=150, anchor=tkinter.CENTER)
CodeInput.configure(font=("Arial", 14))

TopBar = customtkinter.CTkFrame(master=app, width=50, height=30)

app.mainloop()