import requests
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

api_url = "https://www.proxy-list.download/api/v1/get?type=http&anon=elite"
response = requests.get(api_url)
proxies = response.text.strip().split('\n')

with open("secound.txt", "a") as file:
    for proxy in proxies:
        ip, port = proxy.split(':')
        response = os.system(f"ping -n 1 {ip} >nul 2>&1")
        if response == 0:
            print(f"{Fore.RED}[+]{Style.RESET_ALL} The proxy ip is online{Fore.LIGHTBLACK_EX} {ip}:{port} {Style.RESET_ALL}")
            file.write(f"{ip}:{port}\n")
        else:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} This proxy ip didn't respond{Fore.LIGHTBLACK_EX} {ip}:{port} {Style.RESET_ALL}")
