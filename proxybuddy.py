import requests
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

api_url = "https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=1&sort_by=lastChecked&sort_type=desc"

response = requests.get(api_url)
data = response.json()

proxies = data.get("data", [])

with open("data.txt", "a") as file:
    for proxy in proxies:
        ip = proxy.get("ip")
        port = proxy.get("port")
        if ip and port:
            response = os.system(f"ping -n 1 {ip} >nul 2>&1")
            if response == 0:
                print(f"{Fore.RED}[+]{Style.RESET_ALL} The proxy ip is online{Fore.LIGHTBLACK_EX} {ip}:{port} {Style.RESET_ALL}")
                file.write(f"{ip}:{port}\n")
            else:
                print(f"{Fore.RED}[-]{Style.RESET_ALL} This proxy ip didn't respond{Fore.LIGHTBLACK_EX} {ip}:{port} {Style.RESET_ALL}")
