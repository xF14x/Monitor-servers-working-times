# Programming By Sulaiman AL-Mohawis Twitter:f14commander Github:xF14x
from os import system
from list import list
from datetime import datetime

date = datetime.now()

# Programming Bot
# By SaLeH | insta @8_wvu | github @S75XD | Twitter @S75XD

import requests

def send(msg):
    ID = '' # [!] Your telegram id
    token = '' # [!] Token Your Bot

    tl = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}''') # [?] Get msg
    re = requests.post(tl) # [?] post requests 

# Check Server if up or down

for ping in list:
    response = system(f'ping -c 1 {ping}')

    if response == 0:
        send(f'{ping} is up in {date}\n')
    else:
        send(f'{ping} is down in {date}\n')