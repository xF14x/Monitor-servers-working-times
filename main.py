# Programming By Sulaiman AL-Mohawis Twitter:f14commander Github:xF14x
from os import system
from list import list
from datetime import datetime

date = datetime.now()

for ping in list:
    response = system(f'ping -c 1 {ping}')

    if response == 0:
        with open(f'{ping}.txt', 'a') as log:
            log.write(f'{ping} is up in {date}\n')
    else:
        with open(f'{ping}.txt', 'a') as log:
            log.write(f'{ping} is down in {date}\n')