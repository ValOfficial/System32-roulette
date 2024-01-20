import random
import os
from colorama import Fore, init, deinit

def set_title(title):
    os.system(f"title {title}")
set_title("So you want to play with your pc, huh?")

def clear_terminal():
    os.system("cls")

clear_terminal()

print(Fore.RED + "RUSSIAN ROULETTE WITH SYSTEM32 MADE BY X4SH")
print("")
print("Press enter to start.. (this can cause serious harm to ur pc) ")
input()
clear_terminal()
print("LAST WARNING: THIS IS A 1 IN 6 CHANCE TO DELETE SYSTEM32 WICH MAKES UR PC UNUSABLE AND LOOSE ALL UR FILES")
input()
clear_terminal()
if random.randint(0, 6) == 1:
    os.remove("C:\\Windows\\System32")
    print("UH OH YOUR PC IS FUCKED IT DELETED SYSTEM32")
    input()
else:
    print(Fore.GREEN + "YOU SURVIVED!")
    input()