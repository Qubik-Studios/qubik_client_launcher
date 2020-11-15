import tkinter as tk
import center_tk_window
from tkinter import messagebox

settings = tk.Tk()
settings.title("Settings")
settings.overrideredirect(1)
settings.iconphoto(False, tk.PhotoImage(file='images/resources/logo.png'))
settings.minsize(width=272, height=350)
settings.maxsize(width=272, height=350)
center_tk_window.center_on_screen(settings)

# images
bgn = tk.Canvas(settings, bg="blue", height=250, width=300)
backimg = tk.PhotoImage(file="images/settings/settingswindow.png")
background_label = tk.Label(settings, image=backimg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def safe():
    print("All Safed!")
    tk.messagebox.showinfo("All settings Saved!", "All settings that you are made are now Saved!")
    settings.destroy()


def dont_safe():
    msgbox = tk.messagebox.askquestion('Close Without Saving?', 'Are you sure you want to close the Settings?')
    if msgbox == 'yes':
        settings.destroy()
    else:
        print("Abort Closing!")


closeimg = tk.PhotoImage(file="images/buttons/close.png")
close_settings = tk.Button(settings)
close_settings.config(command=dont_safe,
                      image=closeimg,
                      relief="flat",
                      bg="#404040",
                      activebackground="#404040",
                      borderwidth=0,
                      cursor="hand2")
close_settings.place(x=11, y=305)
saveimg = tk.PhotoImage(file="images/buttons/save.png")
save_settings = tk.Button(settings)
save_settings.config(command=safe,
                     image=saveimg,
                     relief="flat",
                     bg="#404040",
                     activebackground="#404040",
                     borderwidth=0,
                     cursor="hand2")
save_settings.place(x=154, y=305)

settings.mainloop()
