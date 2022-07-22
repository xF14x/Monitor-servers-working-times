from os import system

hostname = "google.com"

response = system(f'ping -c 1 {hostname}')

if response == 0:
    print(f'{hostname} is up')
else:
    print(f'{hostname} is down')