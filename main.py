import os
os.system('pip install colorama')
os.system('pip install requests')
os.system('cls')
from colorama.ansi import Fore
import requests, time
import random
import colorama
from colorama import Fore
print(f"""{Fore.MAGENTA}
    
 ██▀███   ██▓ ██▓███  
▓██ ▒ ██▒▓██▒▓██░  ██▒
▓██ ░▄█ ▒▒██▒▓██░ ██▓▒
▒██▀▀█▄  ░██░▒██▄█▓▒ ▒
░██▓ ▒██▒░██░▒██▒ ░  ░
░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░
  ░▒ ░ ▒░ ▒ ░░▒ ░     
  ░░   ░  ▒ ░░░       
   ░      ░           
                      

    """)

def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    print(f"{Fore.MAGENTA}[{Fore.RED}+{Fore.MAGENTA}]'{plbra}'Enviado Correctamente. {r.status_code}[{Fore.RED}+{Fore.MAGENTA}]")

channel=int(input(f'{Fore.LIGHTMAGENTA_EX}Canal:{Fore.RESET} '))
plbra=input(f'{Fore.LIGHTMAGENTA_EX}Palabra para spamear:{Fore.RESET} ')
if not plbra:
    plbra='@everyone'

sendMessage("ingresar token", channel,plbra)
sendMessage("ingresar token", channel,plbra)
sendMessage("ingresar token", channel,plbra)
sendMessage("ingresar token", channel,plbra)
sendMessage("ingresar token", channel,plbra)
sendMessage("ingresar token", channel,plbra)


#Ingresa los tokens donde dice, cuando este list copia y pega:
# sendMessage("ingresar token", channel,plbra)
# Con Los tokens y listo, ejecuta el script, ingresa ID y palabra y disfruta.





             #Token                                                    "channel ID/id de canal"   palabra a spamear


