import pywhatkit
import keyboard
import time
from datetime import datetime

contatos =['celphonenumber0', 'celphone']
while len(contatos) >=2:
    pywhatkit.sendwhatmsg(contatos[0],'oi tudo bem?',datetime.now().hour, datetime.now().minute + 2)
    pywhatkit.sendwhatmsg(contatos[1],'oi tudo bem?',datetime.now().hour, datetime.now().minute + 4)
    del contatos[0,1]
    time.sleep(60)