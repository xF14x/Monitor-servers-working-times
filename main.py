# Programming By Sulaiman AL-Mohawis Twitter:f14commander Github:xF14x
import os
from list import list
from datetime import datetime

date = datetime.now()

FolderName = "Logs" # You Can Change The Folder Name For Save Logs Files

if not os.path.isdir(FolderName):
    os.makedirs(FolderName)
else:
    pass

for ping in list:
    response = os.system(f'ping -c 1 {ping}')

    if response == 0:
        with open(f'{FolderName}/{ping}.txt', 'a') as log:
            log.write(f'{FolderName}/{ping} is up in {date}\n')
    else:
        with open(f'{FolderName}/{ping}.txt', 'a') as log:
            log.write(f'{FolderName}/{ping} is down in {date}\n')