from pypresence import Presence
import time as t

print("discord")


while 1:
    t.sleep(15)
    client_id = "771856965214535712"
    RPC = Presence(client_id=client_id)
    RPC.connect()

    RPC.update(large_image="qubik_logo",
               large_text="Launcher",
               state="Sitting in the Launcher",
               details="Redo everything to match Qubik Studios theme"
               )
