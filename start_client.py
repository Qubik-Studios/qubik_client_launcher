import minecraft_launcher_lib as ml
import os

print("Starting with Download...")


def printProgressBar (iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def maximum(max_value, value):
    max_value[0] = value


max_value = [0]

callback = {
    "setStatus": lambda text: print(text),
    "setProgress": lambda value: printProgressBar(value, max_value[0]),
    "setMax": lambda value: maximum(max_value, value)
}

version = "1.16.4"
directory = '%s\\.QubikClient\\' % os.environ['APPDATA']

ml.install.install_minecraft_version(version, directory, callback=callback)
print("Download Finished! Continue with Starting process...")
data_path = "C:/Qubik Client Data/player_data.json"

fo = open(data_path, "r")
astr = fo.readline()
astr = astr[0:551]
fo.close()
print(astr)
login_data = astr

options = {
    "token": login_data['accessToken'],
    "username": login_data['selectedProfile']["name"],
    "uuid": login_data['selectedProfile']["id"]
}
minecraft_command = ml.command.get_minecraft_command(version, directory, options)
