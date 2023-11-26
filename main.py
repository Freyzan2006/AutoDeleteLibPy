import os
import time


list_pip = []

command = "pip freeze>temp.txt"
result2 = os.system(command)
with open('temp.txt', 'r') as f:


    while True:

        line = f.readline()
        if not line:
            break

        list_pip.append(line.strip())


for el in list_pip:
    print(el)
    time.sleep(0.1)
    os.system(f"pip uninstall -y {el}")
    time.sleep(1)
    

    









