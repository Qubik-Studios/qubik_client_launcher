import tkinter as tk
import webbrowser
import center_tk_window
import subprocess as sub
import threading
from tkinter import messagebox

# variable

version_simple = "Alpha 0.0.1.6"
version_userinterface = "ui.0.0.1.7.151120"
version_backend = "be.0.0.1.3.151120"
version_client = "id.0.0.0.0.000000"

# start of the windwo

root = tk.Tk()
root.minsize(width=900, height=550)
root.maxsize(width=900, height=550)
root['background'] = '#404040'
root.title("Qubik Client - Launcher - " + version_simple)
root.iconphoto(False, tk.PhotoImage(file='images/resources/logo.png'))
center_tk_window.center_on_screen(root)


# images
bgn = tk.Canvas(root, bg="blue", height=250, width=300)
backimg = tk.PhotoImage(file="images/resources/backimg.png")
background_label = tk.Label(root, image=backimg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# mojang status
path = "C:/Qubik Client Data/server_status.json"
auth_indicator = tk.StringVar()
color = tk.StringVar(root)

f = open(path,  "r")
strToFind = "{'authserver.mojang.com': 'green'}"
whattoReturn = "None"
if strToFind in f.read():
    whattoReturn = strToFind
if whattoReturn == "{'authserver.mojang.com': 'green'}":
    print("Connected to the Mojang server!")
    color.set("#4CFF00")
else:
    print("Connection to the Mojang server does not exist!")
    color.set("#FF0000")


auth_label = tk.Label(root, text="Auth Server:")
auth_label.config(bg="#404040")
auth_label.place(x=380, y=530)

auth_indicator = tk.Label(root, text="●")
auth_indicator.config(bg="#404040",
                      fg=color.get())
auth_indicator.place(x=447, y=530)

# buttoncmd


def qubikclientweb():

    print("Opened Website!")
    new = 1
    url = "http://qubik-studios.net"
    webbrowser.open(url, new=new)


def clientstart():
    print("Client start")
    try:
        sub.call(["start_client.py"])
    except WindowsError:
        sub.call(['start_client.py'], shell=True)



def getversion():
    print("Current Version: " + version_userinterface + " | " + version_backend)
    messagebox.showinfo("Qubik Client Version",
                        "Current UI Version: " + version_userinterface + "\n\nCurrent Backend Version: "
                        + version_backend + "\n\nCurrent Client Version: " + version_client)


def settingsmenu():
    threading.Timer(0.1, open_settings).start()


def open_settings():
    try:
        sub.call(["settings.py"])
    except WindowsError:
        sub.call(['settings.py'], shell=True)


def proceed_to_login():
    print("Logged Out!")
    threading.Timer(0.0, open_login).start()
    threading.Timer(0.6, close_launcher).start()


def open_login():
    try:
        sub.call(["login.py"])
    except WindowsError:
        sub.call(['login.py'], shell=True)


def close_launcher():
    root.destroy()


# buttons

ext = tk.Button(root)
exitimg = tk.PhotoImage(file="images/buttons/exit.png")
ext.config(image=exitimg,
           command=proceed_to_login,
           relief="flat",
           bg="#404040",
           activebackground="#404040",
           borderwidth=0,
           cursor="hand2")
ext.place(x=852, y=5)

version = tk.Button(root)
versionimg = tk.PhotoImage(file="images/buttons/version_info.png")
version.config(image=versionimg,
               command=getversion,
               relief="flat",
               bg="#404040",
               activebackground="#404040",
               borderwidth=0,
               cursor="hand2")
version.place(x=6, y=8)

ply = tk.Button(root)
playimg = tk.PhotoImage(file="images/buttons/launch.png")
ply.config(image=playimg,
           command=clientstart,
           relief="flat",
           bg="#404040",
           activebackground="#404040",
           borderwidth=0,
           cursor="hand2")
ply.place(x=593, y=447)

stg = tk.Button(root)
settingsimg = tk.PhotoImage(file="images/buttons/settings.png")
stg.config(image=settingsimg,
           command=settingsmenu,
           relief="flat",
           bg="#404040",
           activebackground="#404040",
           borderwidth=0,
           cursor="hand2")
stg.place(x=6, y=443)

web = tk.Button(root)
websiteimg = tk.PhotoImage(file="images/buttons/web.png")
web.config(image=websiteimg,
           command=qubikclientweb,
           relief="flat",
           bg="#404040",
           activebackground="#404040",
           borderwidth=0,
           cursor="hand2")
web.place(x=6, y=480)


root.mainloop()
