import requests
from colorama import Fore,init
init(autoreset = True)
asciiart = f"""{Fore.RED}
  _______    _                _  ___ _ _           
 |__   __|  | |              | |/ (_) | |          
    | | ___ | | _____ _ __   | ' / _| | | ___ _ __ 
    | |/ _ \| |/ / _ \ '_ \  |  < | | | |/ _ \ '__|
    | | (_) |   <  __/ | | | | . \| | | |  __/ |   
    |_|\___/|_|\_\___|_| |_| |_|\_\_|_|_|\___|_|                                                                                                   
"""

print(asciiart)
token = input("inserisci il token: ")
invito = input("inserisci l'inivto: ")


headrs = {
    "authorization" : token
}

while True: 
    requests.post(f'https://discordapp.com/api/v9/invites/{invito}', headers=headrs)
