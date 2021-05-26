#!/usr/bin/env python3

import time
import os


#provede akci 20x
for x in range (20):
#zapisuje data z cpu do souboru text.txt
    os.system('sensors >> text.txt')
    
#cte radek po radku a vyvrari seznam z jednotlivych radku
    with open('text.txt') as file:
        lines=file.readlines()
#vyberek radek cislo 4 kde je zapsana teplota a zapise cely radek do souboru teplota.txt spolu s casem         
    count=0    
    for line in lines:
        count+=1
        if count ==3:
            print(line)
            with open('teplota.txt', 'a') as text:
                text.write(time.strftime('%H:%M:%S '))            
                text.write(line)

#vymaze data z souboru text.txt
    with open('text.txt', 'w') as text:
        text.write('')
#pocka 60 sekund nez se zacne cela akce opakovat        
    time.sleep(60)



