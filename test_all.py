import subprocess as sub

try:
    sub.call(["login.py"])
    sub.call(["loading.py"])
    sub.call(["start_client.py"])
    sub.call(["launcher.py"])
    sub.call(["discordrp.py"])
except WindowsError:
    sub.call(['login.py'], shell=True)
    sub.call(["loading.py"], shell=True)
    sub.call(["start_client.py"], shell=True)
    sub.call(["launcher.py"], shell=True)
    sub.call(["discordrp.py"], shell=True)
