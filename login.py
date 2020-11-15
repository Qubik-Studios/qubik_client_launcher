import tkinter as tk
import center_tk_window
import minecraft_launcher_lib as ml
from tkinter import messagebox
import subprocess as sub
import threading
from pypresence import Presence
import time


login = tk.Tk()
debug = True
login.minsize(height=500, width=350)
login.maxsize(height=500, width=350)
login.title("Qubik Client - LogIn")
login.iconphoto(False, tk.PhotoImage(file="images/login/logo.png"))
center_tk_window.center_on_screen(login)

tk.Canvas(login, bg="blue")
lbackimg = tk.PhotoImage(file="images/login/login_window.png")
lbackground_label = tk.Label(login, image=lbackimg)
lbackground_label.place(x=0, y=0, relwidth=1, relheight=1)

if debug is False:
    version = "ui.0.0.1.7.151120 | be.0.0.1.1.121120"
else:
    version = "ui.0.0.1.7.151120 | be.0.0.1.1.121120 | Debug Mode"
version_label = tk.Label(login, text=version)
version_label.config(bg="#404040")
version_label.place(x=0, y=480)

# mojang status
path = "C:/Qubik Client Data/server_status.json"
color = tk.StringVar(login)

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

authindicator_label = tk.Label(login, text="●")
authindicator_label.config(bg="#404040",
                           fg=color.get())
authindicator_label.place(x=335, y=480)


# backend checks


def login_check():
    data_path = "C:/Qubik Client Data/player_data.json"
    username, password = uservar.get(), passwordvar.get()
    logincheck.set("DISABLED")
    if key == keyvar.get():
        print("Beta key correct!")
        print("Proceed with Login..")
        access_tokenvar = tk.StringVar()
        access_tokenvar.set(ml.account.login_user(username, password))
        with open(path, "w") as b:
            b.write("")
        with open(data_path, "w") as i:
            i.write(access_tokenvar.get())
        fo = open(data_path, "r+")
        astr = fo.readline()
        astr = astr[17:325]
        fo.close()
        print(ml.account.validate_access_token(access_token=astr))
        if ml.account.validate_access_token(access_token=astr) is True:
            proceed_to_launcher()
            logincheck.set("NORMAL")
        else:
            print("Login data wrong!")
            messagebox.showerror("Something went wrong!",
                                 "A Error occoured while loggin in your Mojang Account!\nMaby the Password was wrong?")
            logincheck.set("NORMAL")
    else:
        print("Beta key incorrect!")
        messagebox.showerror("Something went wrong!",
                             "A Error occoured while checking your Beta-Key!\nMaby the key was wrong?")
        logincheck.set("NORMAL")

# Client Token: 344:377
# Access Token:  17:325
# Access + Client Token: 1:377


def debug_to_launcher():
    print("Warning! You started the Launcher in Debug Mode!")
    print("Please aware your self that you can't play in Debug Mode")
    print("Minecraft!")
    print("DEBUG >> Proceed to Launcher")
    proceed_to_launcher()


def proceed_to_launcher():
    threading.Timer(0.0, open_launcher).start()
    threading.Timer(0.6, close_login).start()


def open_launcher():
    try:
        sub.call(["launcher.py"])
    except WindowsError:
        sub.call(['launcher.py'], shell=True)


def close_login():
    login.destroy()

# Variable


if debug is False:
    key = "zNDsBNx5jH1n"
else:
    key = "test"
keyvar = tk.StringVar(login)
uservar = tk.StringVar(login)
passwordvar = tk.StringVar(login)
correkt_betak = tk.StringVar(login)
logincheck = tk.StringVar(login)
logincheck.set("active")

# Login ++ Beta

enteruser = tk.Entry(login, width=42, bd="0", textvariable=uservar)
enteruser.place(x=48.6, y=248)

enterpassword = tk.Entry(login, width=42, show="●", bd="0", textvariable=passwordvar)
enterpassword.place(x=48.6, y=295)

enterkey = tk.Entry(login, width=42, show="●", bd="0", textvariable=keyvar)
enterkey.place(x=48.6, y=372)

# Buttons

LogInbutton = tk.Button(login)
LogInbuttonimg = tk.PhotoImage(file="images/buttons/login.png")
LogInbutton.config(image=LogInbuttonimg,
                   command=login_check,
                   borderwidth=0,
                   bg="#404040",
                   activebackground="#404040",
                   cursor="hand2",
                   state=logincheck.get())
LogInbutton.place(x=98, y=420)

if debug is True:
    button = tk.Button(login)
    button.config(command=debug_to_launcher,
                  text="Debug")
    button.place(x=0, y=0)


login.mainloop()

client_id = "771856965214535712"
RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(large_image="qubik_logo",
           large_text="Launcher",
           state="Sitting in the Launcher",
           details="Redo everything to match Qubik Studios theme"
           )

while 1:
    time.sleep(15)
