from os import system
from list import list
from datetime import datetime

date = datetime.now()

for ping in list:
    response = system(f'ping -c 1 {ping}')

    if response == 0:
        print(f'{ping} is up in {date}')
    else:
        print(f'{ping} is down in {date}')