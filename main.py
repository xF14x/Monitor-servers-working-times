from os import system
from list import list

for ping in list:
    response = system(f'ping -c 1 {ping}')

    if response == 0:
        print(f'{ping} is up')
    else:
        print(f'{ping} is down')