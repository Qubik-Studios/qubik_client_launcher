from AnimatedGIF import *
import tkinter as tk
import center_tk_window
import subprocess as sub
import threading
import os
import mojang_api as ma

loading = tk.Tk()
loading.overrideredirect(1)
loading.minsize(height=350, width=331)
loading.maxsize(height=350, width=331)
loading.title("Qubik Client - Loading")
loading.iconphoto(False, tk.PhotoImage(file="images/login/logo.png"))

# Create File Directory


path = "C:/Qubik Client Data/"
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

path_status = "C:/Qubik Client Data/server_status.json"


def status():
    server_status = tk.StringVar()
    server_status.set(ma.get_status())
    with open(path_status, "w") as f:
        f.write(server_status.get())
    print(ma.get_status())


status()

center_tk_window.center_on_screen(loading)

tk.Canvas(loading, bg="blue")
loadingscreen = tk.PhotoImage(file="images/loading/loadingwindow.png")
loadingscreen_label = tk.Label(loading, image=loadingscreen)
loadingscreen_label.place(x=0, y=0, relwidth=1, relheight=1)

loadingbars = AnimatedGif(loading, "images/loading/loading_bars.gif", 0.025)
loadingbars.config(borderwidth=0)
loadingbars.place(x=260, y=282)
loadingbars.start()


def open_login():
    try:
        sub.call(["login.py"])
    except WindowsError:
        sub.call(['login.py'], shell=True)


def close_loading():
    loading.destroy()


threading.Timer(5.0, open_login).start()
threading.Timer(5.6, close_loading).start()

loading.mainloop()

try:
    sub.call(["discordrp.py"])
except WindowsError:
    sub.call(['discordrp.py'], shell=True)