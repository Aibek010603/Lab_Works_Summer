import json

file_path = r"c:\Users\toleg\OneDrive\Рабочий стол\PP2_Sum_Aibek\Lab_Works_Summer\Lab_4\sample-data.json"


with open(file_path, "r") as f:
    data = json.load(f)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in range(len(data["imdata"])):
    a = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    b = data["imdata"][i]["l1PhysIf"]["attributes"]["descr"]
    c = data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    d = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print("{:<49}{:<23}{:<7}  {}".format(a, b, c, d))
